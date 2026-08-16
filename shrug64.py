#!/usr/bin/env python3

import argparse
import base64
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Encode or decode a file using Python's Base64."
    )

    mode = parser.add_mutually_exclusive_group(required=True)

    mode.add_argument(
        "-e", "--encode",
        action="store_true",
        help="Base64 Encode file contents"
    )

    mode.add_argument(
        "-d", "--decode",
        action="store_true",
        help="Base64 Decode file contents"
    )

    parser.add_argument(
        "file",
        help="File to encode/decode"
    )

    args = parser.parse_args()

    try:
        with open(args.file, "rb") as f:
            data = f.read()

        if args.encode:
            output = base64.b64encode(data)
            print(output.decode("ascii"))

        else:
            # Remove whitespace so normal Base64 files with
            # newlines/tabs/etc. can still be decoded.
            data = b"".join(data.split())

            # Strictly validate the remaining Base64 data.
            output = base64.b64decode(data, validate=True)

            sys.stdout.buffer.write(output)

            # If we're displaying directly in a terminal and the
            # decoded data doesn't already end with a newline,
            # add one so the shell prompt starts on a new line.
            if sys.stdout.isatty() and not output.endswith(b"\n"):
                sys.stdout.buffer.write(b"\n")

    except FileNotFoundError:
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
