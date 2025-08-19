import { useState, useRef } from "react";
import { Play, Pause, SkipBack, SkipForward, Volume2, Star } from "lucide-react";

export default function MusicPlayer() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(24); // seconds
  const duration = 168; // 2:48 in seconds
  const audioRef = useRef(null);

  const togglePlay = () => {
    setIsPlaying(!isPlaying);
    if (audioRef.current) {
      isPlaying ? audioRef.current.pause() : audioRef.current.play();
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-rose-900 via-pink-800 to-rose-900">
      <div className="bg-rose-900/60 rounded-2xl shadow-lg p-6 w-[360px] text-white">
        {/* Album Cover */}
        <img
          src="https://i.scdn.co/image/ab67616d0000b273d8e080be47c54b9b78c7f7a4"
          alt="Album"
          className="rounded-xl mb-4"
        />

        {/* Song Info */}
        <div className="text-center mb-4">
          <h2 className="text-lg font-semibold">Junoon</h2>
          <p className="text-sm opacity-70">MITRAZ</p>
        </div>

        {/* Progress Bar */}
        <div className="flex items-center justify-between text-xs mb-2">
          <span>{Math.floor(progress / 60)}:{String(progress % 60).padStart(2, "0")}</span>
          <span>{Math.floor(duration / 60)}:{String(duration % 60).padStart(2, "0")}</span>
        </div>
        <input
          type="range"
          min="0"
          max={duration}
          value={progress}
          onChange={(e) => setProgress(Number(e.target.value))}
          className="w-full accent-white"
        />

        {/* Controls */}
        <div className="flex items-center justify-center gap-6 mt-4">
          <button><SkipBack size={28} /></button>
          <button
            onClick={togglePlay}
            className="bg-white text-rose-900 rounded-full p-3 shadow-lg"
          >
            {isPlaying ? <Pause size={28} /> : <Play size={28} />}
          </button>
          <button><SkipForward size={28} /></button>
        </div>

        {/* Bottom Row */}
        <div className="flex items-center justify-between mt-6">
          <Star size={22} />
          <div className="flex items-center gap-2">
            <Volume2 size={22} />
            <input type="range" min="0" max="100" className="w-24 accent-white" />
          </div>
        </div>
      </div>

      {/* Hidden Audio Element */}
      <audio ref={audioRef} src="/song.mp3" />
    </div>
  );
}
