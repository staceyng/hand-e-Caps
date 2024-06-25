"""Test file for github actions"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run hand-e-caps for user:<name>")
    parser.add_argument(
        "--name", type=str, nargs="?", default="stacey", help="Name/Callsign"
    )
    args = parser.parse_args()

    print(f"Welcome {args.name}, Hello World!")
