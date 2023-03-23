import subprocess
import time
import webbrowser
from datetime import datetime, timedelta
from math import ceil
from pathlib import Path
from typing import List


def validate_links(links: List[str]) -> List[str]:
    valid_links: List[str] = []
    for link in links:
        link = link.strip()

        if link.startswith("#") or len(link) == 0:
            continue

        if not link.startswith("http"):
            print(f"Invalid link: {link}")
            continue

        valid_links.append(link)
    return valid_links


def loading_bar(
    range_obj: range,
    prefix: str = "",
    suffix: str = "",
    length: int = 20,
    fill: str = "#",
):
    total = len(range_obj)

    for i, item in enumerate(range_obj, start=1):
        percent = f"{100 * (i / float(total)):.2f}"
        filled_length = int(length * i // total)
        bar = fill * filled_length + "-" * (length - filled_length)
        print(f"\r{prefix} |{bar}| {percent}% {suffix}", end="\r")

        yield item
    print()


def install_applications(wait_time: int):
    download_dir = Path.home() / "Downloads"

    for file_path in download_dir.glob("*.*"):
        if (
            file_path.stat().st_mtime
            > (datetime.now() - timedelta(seconds=60 + wait_time)).timestamp()
        ):
            print(f"Running {file_path.name}")
            subprocess.Popen(str(file_path), shell=True)
            time.sleep(5)


def main():
    # Check if the links file exists
    links_file_path = Path("links.txt")

    if not links_file_path.exists():
        print(f"Error: {links_file_path} does not exist.")
        return

    # loading the links
    with links_file_path.open() as links_file:
        links_lines = links_file.readlines()

    valid_links = validate_links(links_lines)

    if not valid_links:
        print("Error: No valid links found.")
        return

    try:
        wait_time = ceil(float(input("Please enter expected download time: ")))
    except ValueError:
        wait_time = 60
        print("Invalid input! Download time set to default value of 60 seconds.")

    # opening the links
    for link in valid_links:
        webbrowser.open(link)

    for _ in loading_bar(range(wait_time + 1), "Waiting:", "Completed"):
        time.sleep(1)

    # installing the applications
    install_applications(wait_time)


if __name__ == "__main__":
    main()
    print("Done! Closing in 5 seconds...")
    time.sleep(5)
