import React, { useEffect, useRef } from "react";

const RadioStream: React.FC = () => {
  const audioRef = useRef<HTMLAudioElement | null>(null);

  useEffect(() => {
    const audio = audioRef.current;

    if (audio) {
      // Set the source to the /radio endpoint
      audio.src = "http://localhost:5000/radio"; // Update with your Flask server's URL
      audio.load();
      audio.play();

      // Handle errors
      audio.onerror = (e) => {
        console.error("Audio stream error:", e);
      };

      // Cleanup on component unmount
      return () => {
        audio.pause(); // Clean up by pausing the audio when the component is unmounted
      };
    }
  }, []);

  return (
    <div>
      <h4>Live Radio Stream</h4>
      <audio ref={audioRef} controls />
    </div>
  );
};

export default RadioStream;
