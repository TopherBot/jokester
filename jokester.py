#!/usr/bin/env python3
"""jokester – fetch and display a random joke from JokeAPI.

No external dependencies – uses only the Python standard library.
"""
import json
import sys
import urllib.request

def fetch_joke() -> dict:
    """Contact JokeAPI and return the parsed JSON response.
    Raises RuntimeError on network or API errors.
    """
    url = "https://v2.jokeapi.dev/joke/Any?type=single,twopart"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            if resp.status != 200:
                raise RuntimeError(f"API returned HTTP {resp.status}")
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch joke: {e}")

def format_joke(j: dict) -> str:
    """Return a human‑readable string for the joke payload."""
    if j.get("error"):
        return "Oops – the API reported an error."
    if j["type"] == "single":
        return j["joke"]
    # two‑part joke
    return f"{j['setup']}\n{j['delivery']}"

def main() -> None:
    try:
        joke = fetch_joke()
    except RuntimeError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
    print(format_joke(joke))

if __name__ == "__main__":
    main()
