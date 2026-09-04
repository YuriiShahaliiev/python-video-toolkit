from source.ffmpeg_runner import run_ffmpeg


def remove_cut(
    input_path: str,
    output_path: str,
    start: float,
    end: float,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-filter_complex",
        f"[0:v]trim=0:{start},setpts=PTS-STARTPTS[before];"
        f"[0:v]trim=start={end},setpts=PTS-STARTPTS[after];"
        "[before][after]concat=n=2:v=1:a=0[outv]",
        "-map", "[outv]",
        "-map", "0:a?",
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path,
    ])
