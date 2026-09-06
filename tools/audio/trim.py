from source.ffmpeg_runner import run_ffmpeg


def trim_audio(
    input_path: str,
    output_path: str,
    start: float,
    duration: float,
) -> None:
    if start < 0:
        raise ValueError("start must be 0 or greater")

    if duration <= 0:
        raise ValueError("duration must be greater than 0")

    run_ffmpeg([
        "-ss", str(start),
        "-i", input_path,
        "-t", str(duration),
        "-c:a", "libmp3lame",
        output_path,
    ])
