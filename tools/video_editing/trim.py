from source.ffmpeg_runner import run_ffmpeg


def trim_video(
    input_path: str,
    output_path: str,
    start: float,
    duration: float,
) -> None:
    run_ffmpeg([
        "-ss", str(start),
        "-i", input_path,
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path,
    ])
