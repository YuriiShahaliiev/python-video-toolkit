from source.ffmpeg_runner import run_ffmpeg


def extract_frame_from_video(
    input_path: str,
    output_path: str,
    frame_number: int,
) -> None:
    if frame_number < 0:
        raise ValueError("frame_number must be 0 or greater")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"select='eq(n,{frame_number})'",
        "-frames:v", "1",
        output_path,
    ])
