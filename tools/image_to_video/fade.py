from source.ffmpeg_runner import run_ffmpeg


def fade_image(
    input_path: str,
    output_path: str,
    duration: int,
    fade_duration: float,
    fade_type: str,
    fps: int = 30,
    width: int = 1920,
    height: int = 1080,
) -> None:
    if fade_type not in {"in", "out"}:
        raise ValueError("fade_type must be 'in' or 'out'")

    if fade_duration <= 0 or fade_duration > duration:
        raise ValueError(
            "fade_duration must be greater than 0 and not exceed duration"
        )

    if fade_type == "in":
        start_time = 0
    else:
        start_time = duration - fade_duration

    run_ffmpeg([
        "-loop", "1",
        "-framerate", str(fps),
        "-i", input_path,
        "-vf",
        f"scale={width}:{height}:force_original_aspect_ratio=increase,"
        f"crop={width}:{height},"
        f"fade=t={fade_type}:st={start_time}:d={fade_duration}",
        "-t", str(duration),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
