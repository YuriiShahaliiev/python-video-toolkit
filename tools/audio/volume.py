from source.ffmpeg_runner import run_ffmpeg


def change_volume(
    input_path: str,
    output_path: str,
    volume: float,
) -> None:
    if volume < 0:
        raise ValueError("volume must be 0 or greater")
    elif volume > 20:
        raise ValueError("volume must be 20 or less")

    run_ffmpeg([
        "-i", input_path,
        "-af", f"volume={volume}",
        "-c:v", "copy",
        "-c:a", "aac",
        output_path,
    ])
