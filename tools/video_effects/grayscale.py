from source.ffmpeg_runner import run_ffmpeg


def grayscale_video(
    input_path: str,
    output_path: str,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-vf", "hue=s=0",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
