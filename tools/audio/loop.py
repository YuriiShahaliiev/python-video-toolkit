from source.ffmpeg_runner import run_ffmpeg


def loop_audio(
    input_path: str,
    output_path: str,
    loops: int,
) -> None:
    if loops < 1:
        raise ValueError("loops must be at least 1")

    run_ffmpeg([
        "-stream_loop", str(loops - 1),
        "-i", input_path,
        "-c:a", "libmp3lame",
        output_path,
    ])
