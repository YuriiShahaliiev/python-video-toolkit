from source.ffmpeg_runner import run_ffmpeg


def concat_audio(
    input_paths: list[str],
    output_path: str,
) -> None:
    if len(input_paths) < 2:
        raise ValueError("At least 2 audio files are required")

    inputs = []

    for path in input_paths:
        inputs.extend(["-i", path])

    streams = "".join(
        f"[{index}:a]"
        for index in range(len(input_paths))
    )

    filter_complex = (
        f"{streams}"
        f"concat=n={len(input_paths)}:v=0:a=1[aout]"
    )

    run_ffmpeg([
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "[aout]",
        "-c:a", "libmp3lame",
        output_path,
    ])
