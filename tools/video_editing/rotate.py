from source.ffmpeg_runner import run_ffmpeg


def rotate_video(
    input_path: str,
    output_path: str,
    angle: int,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-vf", f"rotate={angle}*PI/180",
        "-an",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
