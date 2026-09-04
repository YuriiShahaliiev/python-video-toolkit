from source.ffmpeg_runner import run_ffmpeg


def merge_videos(
    input_paths: list[str],
    output_path: str,
) -> None:
    inputs = []

    for path in input_paths:
        inputs.extend(["-i", path])

    filter_inputs = "".join(
        f"[{i}:v]" for i in range(len(input_paths))
    )

    run_ffmpeg([
        *inputs,
        "-filter_complex",
        f"{filter_inputs}concat=n={len(input_paths)}:v=1:a=0[outv]",
        "-map", "[outv]",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
