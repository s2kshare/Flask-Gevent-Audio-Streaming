import os
import random
import subprocess

from flask import Flask, Response, stream_with_context

app = Flask(__name__)

# Audio Directory
AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audios')
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

def get_audio_files():
    return [os.path.join(AUDIO_DIR, f) for f in os.listdir(AUDIO_DIR) if f.endswith('.mp3')]

def generate_audio():
    while True:
        audio_files = get_audio_files()
        if not audio_files:
            break

        random.shuffle(audio_files)

        for file in audio_files:
            process = subprocess.Popen(
                ["ffmpeg", "-re", "-i", file, "-f", "mp3", "-"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                bufsize=4096
            )
            try:
                while True:
                    chunk = process.stdout.read(4096)
                    if not chunk:
                        break
                    yield chunk
            finally:
                process.terminate()

@app.route('/stream')
def stream():
    return Response(stream_with_context(generate_audio()), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)