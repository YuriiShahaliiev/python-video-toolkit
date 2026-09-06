from source.ffmpeg_runner import run_ffmpeg


def remove_audio(
    input_path: str,
    output_path: str,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-an",
        "-c:v", "copy",
        output_path,
    ])
