from source.ffmpeg_runner import run_ffmpeg


def extract_scene_frames(
    input_path: str,
    output_pattern: str,  # For example: scene_%06d.jpg
    threshold: float = 0.3,
) -> None:
    if not 0 < threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    run_ffmpeg([
        "-i", input_path,
        "-vf", f"select='gt(scene,{threshold})'",
        "-fps_mode", "vfr",
        "-q:v", "2",
        "-pix_fmt", "yuvj420p",
        output_pattern,
    ])
