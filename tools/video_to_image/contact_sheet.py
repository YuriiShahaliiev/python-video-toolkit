from pathlib import Path

from source.ffmpeg_runner import run_ffmpeg


def create_contact_sheet(
    input_path: str,
    output_path: str,
    interval: float = 1,
    columns: int = 4,
    width: int = 320,
) -> None:
    if interval <= 0:
        raise ValueError("interval must be greater than 0")

    if columns <= 0:
        raise ValueError("columns must be greater than 0")

    if width <= 0:
        raise ValueError("width must be greater than 0")

    temp_dir = Path("images/temp_contact_sheet")
    temp_dir.mkdir(parents=True, exist_ok=True)

    frame_pattern = temp_dir / "frame_%04d.jpg"

    run_ffmpeg([
        "-i", input_path,
        "-vf",
        f"fps=1/{interval},scale={width}:-1",
        "-q:v", "2",
        str(frame_pattern),
    ])

    frames = sorted(temp_dir.glob("frame_*.jpg"))

    if not frames:
        raise RuntimeError("No frames were extracted")

    rows = (len(frames) + columns - 1) // columns

    tile_input = str(frame_pattern)

    run_ffmpeg([
        "-framerate", "1",
        "-i", tile_input,
        "-vf", f"tile={columns}x{rows}",
        "-frames:v", "1",
        "-q:v", "2",
        output_path,
    ])

    for frame in frames:
        frame.unlink()

    try:
        temp_dir.rmdir()
    except OSError:
        pass
