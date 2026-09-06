from source.ffmpeg_runner import run_ffmpeg


def change_brightness(
    input_path: str,
    output_path: str,
    value: float,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-vf", f"eq=brightness={value}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
