from source.ffmpeg_runner import run_ffmpeg


def split_video(
    input_path: str,
    output_pattern: str,
    segment_duration: float,
) -> None:
    if segment_duration <= 0:
        raise ValueError("segment_duration must be greater than 0")

    run_ffmpeg([
        "-i", input_path,
        "-map", "0:v:0",
        "-an",
        "-c:v", "libx264",
        "-preset", "medium",
        "-force_key_frames",
        f"expr:gte(t,n_forced*{segment_duration})",
        "-f", "segment",
        "-segment_time", str(segment_duration),
        "-reset_timestamps", "1",
        output_pattern,
    ])
