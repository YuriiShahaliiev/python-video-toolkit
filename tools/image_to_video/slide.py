from source.ffmpeg_runner import run_ffmpeg


def slide_image(
    input_path: str,
    output_path: str,
    duration: int,
    direction: str,
    fps: int = 30,
    width=1080,
    height=1440
) -> None:
    if direction not in {"left", "right", "top", "bottom"}:
        raise ValueError(
            "direction must be 'left', 'right', 'top' or 'bottom'"
        )

    slide_time = duration

    if direction == "left":
        x = f"-w+(w*t/{slide_time})"
        y = "(H-h)/2"

    elif direction == "right":
        x = f"W-(w*t/{slide_time})"
        y = "(H-h)/2"

    elif direction == "top":
        x = "(W-w)/2"
        y = f"-h+(h*t/{slide_time})"

    else:
        x = "(W-w)/2"
        y = f"H-(h*t/{slide_time})"

    filter_complex = (
        f"color=black:s={width}x{height}:r={fps}[bg];"
        f"[0:v]"
        f"scale={width}:{height}:"
        f"force_original_aspect_ratio=decrease[fg];"
        f"[bg][fg]"
        f"overlay=x='{x}':y='{y}'"
    )

    run_ffmpeg([
        "-loop", "1",
        "-framerate", str(fps),
        "-i", input_path,
        "-filter_complex", filter_complex,
        "-t", str(duration),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
