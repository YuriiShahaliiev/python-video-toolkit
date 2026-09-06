from source.ffmpeg_runner import run_ffmpeg


def change_saturation(
    input_path: str,
    output_path: str,
    value: float,
) -> None:
    if value < 0:
        raise ValueError("saturation must be 0 or greater")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"eq=saturation={value}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
