from source.ffmpeg_runner import run_ffmpeg


def fade_audio(
    input_path: str,
    output_path: str,
    fade_type: str,
    duration: float,
    start_time: float = 0,
) -> None:
    if fade_type not in {"in", "out"}:
        raise ValueError("fade_type must be 'in' or 'out'")

    if duration <= 0:
        raise ValueError("duration must be greater than 0")

    if start_time < 0:
        raise ValueError("start_time must be 0 or greater")

    run_ffmpeg([
        "-i", input_path,
        "-af", f"afade=t={fade_type}:st={start_time}:d={duration}",
        "-c:a", "libmp3lame",
        output_path,
    ])
