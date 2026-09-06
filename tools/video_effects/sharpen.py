from source.ffmpeg_runner import run_ffmpeg


def sharpen_video(
    input_path: str,
    output_path: str,
    strength: float = 1,
) -> None:
    if strength < 0:
        raise ValueError("strength must be 0 or greater")
    elif strength > 5:
        raise ValueError("strength must be 5 or less")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"unsharp=5:5:{strength}:5:5:0",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        output_path,
    ])
