from source.ffmpeg_runner import run_ffmpeg


def extract_frames_from_video(
    input_path: str,
    output_pattern: str,  # For example: frame_%06d.jpg
    mode: str,
    value: float = 1,
) -> None:
    if mode not in {"all", "interval", "fps"}:
        raise ValueError(
            "mode must be 'all', 'interval' or 'fps'"
        )

    if value <= 0:
        raise ValueError("value must be greater than 0")

    if mode == "all":
        run_ffmpeg([
            "-i", input_path,
            "-fps_mode", "passthrough",
            output_pattern,
        ])

    elif mode == "interval":
        run_ffmpeg([
            "-i", input_path,
            "-vf", f"fps=1/{value}",
            output_pattern,
        ])

    elif mode == "fps":
        run_ffmpeg([
            "-i", input_path,
            "-vf", f"fps={value}",
            output_pattern,
        ])
