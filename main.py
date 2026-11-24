"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt.
"""

import os

ENTRY_TEXT = "Tip: when the build bar stalls at 87%, don't refresh — my agent and I blame the 412-line npm log and wait to see who blinks first."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
