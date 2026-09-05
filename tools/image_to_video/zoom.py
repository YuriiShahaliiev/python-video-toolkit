from source.ffmpeg_runner import run_ffmpeg


def zoom_image(
    input_path: str,
    output_path: str,
    duration: int,
    zoom: float,
    fps: int = 30,
) -> None:
    frames = duration * fps

    run_ffmpeg([
        "-loop", "1",
        "-i", input_path,
        "-vf",
        f"zoompan=z='1+({zoom}-1)*on/{frames}':"
        f"d=1:s=1920x1080:fps={fps}",
        "-frames:v", str(frames),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
