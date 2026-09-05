from source.ffmpeg_runner import run_ffmpeg


def remux_video(
    input_path: str,
    output_path: str,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-c", "copy",
        output_path,
    ])
