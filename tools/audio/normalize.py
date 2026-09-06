from source.ffmpeg_runner import run_ffmpeg


def normalize_audio(
    input_path: str,
    output_path: str,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-af", "loudnorm",
        "-c:a", "libmp3lame",
        output_path,
    ])
