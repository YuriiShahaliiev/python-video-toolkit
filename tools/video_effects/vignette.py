from source.ffmpeg_runner import run_ffmpeg


def add_vignette(
    input_path: str,
    output_path: str,
    angle: float = 0.5,
) -> None:
    if angle <= 0:
        raise ValueError("angle must be greater than 0")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"vignette=PI/{angle}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
