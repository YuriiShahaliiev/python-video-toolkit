import json
import subprocess


def probe_video(input_path: str) -> None:
    command = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        input_path,
    ]

    result = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )

    info = json.loads(result.stdout)

    print(json.dumps(info, indent=2))
