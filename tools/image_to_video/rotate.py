from source.ffmpeg_runner import run_ffmpeg


def rotate_image(
    input_path: str,
    output_path: str,
    duration: int,
    angle: float,
    fps: int = 30,
    width: int = 1080,
    height: int = 1440,
) -> None:
    if duration <= 0:
        raise ValueError("Duration must be greater than 0")

    frames = duration * fps

    angle_expression = (
        f"{angle}*PI/180*t/{duration}"
    )

    run_ffmpeg([
        "-loop", "1",
        "-framerate", str(fps),
        "-i", input_path,
        "-vf",
        f"scale={width}:{height}:"
        f"force_original_aspect_ratio=increase,"
        f"crop={width}:{height},"
        f"rotate='{angle_expression}':"
        f"fillcolor=black",
        "-frames:v", str(frames),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
