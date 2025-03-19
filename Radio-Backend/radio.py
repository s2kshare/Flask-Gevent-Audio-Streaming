import time


class Radio:
    """
    A simple radio class that plays audio files from a playlist in sequence.
    """

    def __init__(self, playlist):
        self.playlist = playlist
        self.current_song_index = 0

    def next(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        return self.playlist[self.current_song_index]

    def prev(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
        return self.playlist[self.current_song_index]

    def current(self):
        return self.playlist[self.current_song_index]

    def audio_stream(self, chunk_queue):
        """
        Stream audio from the playlist.

        This method reads audio data from the current file in chunks and puts it
        in the chunk_queue. It moves to the next song when the current song is
        finished. The method runs forever.
        """
        while True:
            file_path = self.playlist[self.current_song_index]
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"{timestamp} > [RADIO]: Now Streaming {file_path}")

            with open(file_path, "rb") as f:
                while chunk := f.read(4096):
                    if chunk_queue.full():
                        chunk_queue.get()
                    chunk_queue.put(chunk)
                    time.sleep(0.1)  # Control playback speed

            # Move to the next song
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
