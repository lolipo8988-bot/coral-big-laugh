"""One-line entry for make.fun: a parrot, one corporate phrase, one promotion.

The program writes exactly one 81-character line to entry.txt and
nothing else. The first half sets up a pet learning a trick; the last
clause delivers the promotion — that single phrase alone is enough to
put him in charge of the whole office. No title, no preamble, and no
explanation of the joke is included in the output file.
"""

import os

LINE = 'I taught my parrot to say "per my last email," and now he runs the entire office.'


def write_entry() -> str:
    """Write the line to the output directory and return its path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
