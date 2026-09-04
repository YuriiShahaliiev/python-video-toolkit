from source.ffmpeg_runner import run_ffmpeg


def png_to_mp4_video(
    input_path: str,
    output_path: str,
    duration: int,
) -> None:
    run_ffmpeg([
        "-loop", "1",
        "-i", input_path,
        "-t", str(duration),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
