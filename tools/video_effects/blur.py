from source.ffmpeg_runner import run_ffmpeg


def blur_video(
    input_path: str,
    output_path: str,
    strength: float = 5,
) -> None:
    if strength <= 0:
        raise ValueError("strength must be greater than 0")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"gblur=sigma={strength}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
