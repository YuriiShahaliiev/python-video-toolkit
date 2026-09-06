from source.ffmpeg_runner import run_ffmpeg


def change_contrast(
    input_path: str,
    output_path: str,
    value: float,
) -> None:
    if value < 0:
        raise ValueError("contrast must be 0 or greater")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"eq=contrast={value}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
