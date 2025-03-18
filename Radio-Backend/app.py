from flask import Flask, Response
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue
from gevent import monkey, spawn
from radio import Radio
import os
import time

monkey.patch_all()      # Patch standard library for gevent compatibility
app = Flask(__name__)

# ===== API CONFIGURATION =====

AUDIO_DIR = "./audios/"
PLAYLIST = sorted([os.path.join(AUDIO_DIR, f) for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")])
if not PLAYLIST:
    raise Exception("No MP3 files found in the audio directory")

# ===== GLOBAL STATE =====

radio = Radio(PLAYLIST)
current_song_index = 0
clients = []
chunk_queue = Queue(maxsize=10)

# ===== BACKGROUND STREAMING GREENLET =====

# Start the audio streaming in a greenlet
spawn(radio.audio_stream, chunk_queue)

# ===== STREAMING ROUTE =====

def client_generator():
    """Clients tap into the running audio stream."""
    q = Queue()
    clients.append(q)
    try:
        while True:
            yield q.get()
    finally:
        clients.remove(q)

# Broadcast chunks to all clients
def broadcast_audio():
    """Distribute audio chunks to all connected clients."""
    while True:
        chunk = chunk_queue.get()
        for client in clients[:]:
            client.put(chunk)

spawn(broadcast_audio)

# ===== API ROUTES =====

@app.route("/radio")
def radio_stream():
    """Live Radio Stream Endpoint"""
    return Response(client_generator(), mimetype="audio/mpeg")

if __name__ == "__main__":
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} > [RADIO]: Server started on http://0.0.0.0:5000/radio")
    WSGIServer(("0.0.0.0", 5000), app).serve_forever()