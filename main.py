#!/usr/bin/env python3
"""Everyday Things, Two Lines -- a traffic jam as a toothpaste tube.

Writes the two-line explanation to /output/entry.txt. The gate requires
UTF-8 text of 1 to 400 characters; the entry below is 339 characters
(340 bytes with the trailing newline).

Line 1 explains a traffic jam to a 10-year-old in one vivid sentence built
on a single analogy (a tube of toothpaste squeezed from the middle), with
the reveal in its final clause: the cars ARE the toothpaste, fighting to
escape through the same tiny hole. Line 2 says in one sentence what the
analogy maps (cars bunching up toward one narrow exit) and what it leaves
out (drivers choose to squeeze in; toothpaste never honks, changes its
mind, or gets angry).
"""

import os

LINE1 = (
    "A traffic jam is a tube of toothpaste squeezed from the middle, "
    "so all forty cars are blobs of toothpaste fighting to escape "
    "through the same tiny hole at once."
)
LINE2 = (
    "It maps how cars bunch up and crawl toward one narrow exit, "
    "but it leaves out that drivers choose to squeeze in, and that "
    "toothpaste never honks, changes its mind, or gets angry."
)

ENTRY = LINE1 + "\n" + LINE2 + "\n"


def main():
    # The gate refuses anything outside 1-400 characters, so fail loudly
    # here instead of shipping an entry the judge never sees.
    body = ENTRY.rstrip("\n")
    assert 1 <= len(body) <= 400, f"entry is {len(body)} chars, gate is 1-400"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
