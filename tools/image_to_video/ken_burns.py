from source.ffmpeg_runner import run_ffmpeg


def ken_burns(
    input_path: str,
    output_path: str,
    duration: int,
    zoom: float,
    direction: str,
    fps: int = 30,
    width: int = 1080,
    height: int = 1440,
) -> None:
    if duration <= 0:
        raise ValueError("Duration must be greater than 0")

    if zoom <= 1:
        raise ValueError("Zoom must be greater than 1")

    if direction not in {"left", "right", "top", "bottom"}:
        raise ValueError(
            "Direction must be 'left', 'right', 'top' or 'bottom'"
        )

    frames = duration * fps

    run_ffmpeg([
        "-loop", "1",
        "-framerate", str(fps),
        "-i", input_path,
        "-vf",
        (
            f"scale="
            f"{width}*{zoom}:"
            f"{height}*{zoom}:"
            f"force_original_aspect_ratio=increase:"
            f"eval=frame,"
            f"crop={width}:{height}:"
            f"x='(iw-ow)*"
            f"{'t/' + str(duration) if direction == 'right' else '1-t/' + str(duration) if direction == 'left' else '0.5'}':"
            f"y='(ih-oh)*"
            f"{'t/' + str(duration) if direction == 'bottom' else '1-t/' + str(duration) if direction == 'top' else '0.5'}'"
        ),
        "-frames:v", str(frames),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
