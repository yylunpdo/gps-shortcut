#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

One line of plain text, at most 200 characters: the GPS, in its own voice,
explaining why it sent the driver down the wrong road. Pure stdlib,
deterministic: the same line is printed on every run.
"""

ENTRY = (
    "the map swore it was a shortcut, so i believed it. the lake was not "
    "on my screen, the wedding was not on my calendar \u2014 and you did "
    "arrive, fashionably late, slightly damp, but scenic."
)


def main():
    print(ENTRY)
    # The harness expects the text at /output/entry.txt when that
    # directory exists; printing to stdout stays the primary output.
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
