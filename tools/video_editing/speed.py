from source.ffmpeg_runner import run_ffmpeg


def change_speed(
    input_path: str,
    output_path: str,
    speed: float,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-filter_complex",
        f"[0:v]setpts=PTS/{speed}[v]",
        "-map", "[v]",
        "-an",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
