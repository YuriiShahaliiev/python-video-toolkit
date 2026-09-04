import subprocess


def run_ffmpeg(args: list[str]) -> None:
    command = ["ffmpeg", *args]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as error:
        raise RuntimeError("FFmpeg processing failed") from error
