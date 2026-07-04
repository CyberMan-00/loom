#!/usr/bin/env python3
"""
Count tokens in a text file using OpenAI's tiktoken (cl100k_base encoding).

Usage:
    python3 count_tokens.py <filepath>

Outputs an integer token count to stdout.
"""
import sys
import tiktoken

def main():
    if len(sys.argv) < 2:
        print("Usage: count_tokens.py <filepath>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    enc = tiktoken.get_encoding("cl100k_base")
    count = len(enc.encode(text))
    print(count)

if __name__ == "__main__":
    main()
