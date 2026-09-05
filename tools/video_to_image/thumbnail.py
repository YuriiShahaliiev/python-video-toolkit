from source.ffmpeg_runner import run_ffmpeg


def create_thumbnail(
    input_path: str,
    output_path: str,
    time: float,
) -> None:
    if time < 0:
        raise ValueError("time must be 0 or greater")

    run_ffmpeg([
        "-ss", str(time),
        "-i", input_path,
        "-frames:v", "1",
        "-q:v", "2",
        output_path,
    ])
