from flask import Flask, Response
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue
from gevent import monkey, spawn
import os
import time

# Patch standard library for gevent compatibility
monkey.patch_all()  

app = Flask(__name__)

# ===== CONFIGURATION =====

AUDIO_DIR = "./audios/"
PLAYLIST = sorted([os.path.join(AUDIO_DIR, f) for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")])
if not PLAYLIST:
    raise Exception("No MP3 files found in the audio directory")

# ===== GLOBAL STATE =====

current_song_index = 0
clients = []
chunk_queue = Queue(maxsize=10)

# ===== BACKGROUND STREAMING GREENLET =====

def audio_stream():
    """Continuously stream audio from the playlist."""
    global current_song_index

    while True:
        file_path = PLAYLIST[current_song_index]
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{timestamp} > [RADIO]: Now Streaming {file_path}")

        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                if chunk_queue.full():
                    chunk_queue.get()
                chunk_queue.put(chunk)
                time.sleep(0.1)  # Control playback speed (simulates real-time playback)
        
        # Move to the next song
        current_song_index = (current_song_index + 1) % len(PLAYLIST)

# Start the audio streaming in a greenlet
spawn(audio_stream)

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
    WSGIServer(("0.0.0.0", 5000), app).serve_forever()