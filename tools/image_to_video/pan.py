from source.ffmpeg_runner import run_ffmpeg


def pan_image(
    input_path: str,
    output_path: str,
    duration: int,
    zoom: float,
    direction: str,
    fps: int = 30,
) -> None:
    frames = duration * fps

    if zoom <= 1:
        raise ValueError("Zoom must be greater than 1")

    if direction == "left":
        x = f"(iw-iw/zoom)*on/{frames}"

    elif direction == "right":
        x = f"(iw-iw/zoom)*(1-on/{frames})"

    elif direction == "top":
        y = f"(ih-ih/zoom)*on/{frames}"
        x = "(iw-iw/zoom)/2"

    elif direction == "bottom":
        y = f"(ih-ih/zoom)*(1-on/{frames})"
        x = "(iw-iw/zoom)/2"

    else:
        raise ValueError(
            "Direction must be 'left', 'right', 'top' or 'bottom'"
        )

    if direction in ("left", "right"):
        y = "(ih-ih/zoom)/2"

    run_ffmpeg([
        "-loop", "1",
        "-i", input_path,
        "-vf",
        f"zoompan="
        f"z={zoom}:"
        f"x='{x}':"
        f"y='{y}':"
        f"d=1:"
        f"s=1920x1080:"
        f"fps={fps}",
        "-frames:v", str(frames),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
