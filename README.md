# Jokester

`jokester` is a tiny Python script that pulls a random joke from the JokeAPI (https://v2.jokeapi.dev) and prints it to the terminal. Ideal for a quick laugh during coding sessions.

## Installation

```bash
# Clone the repo
git clone https://github.com/youruser/jokester.git
cd jokester
# Run directly with Python 3
python3 jokester.py
```

Or install via pip (once published):

```bash
pip install jokester
```

## Usage

```bash
python3 jokester.py   # prints a joke
```

## How it works

The script performs an HTTP GET request to `https://v2.jokeapi.dev/joke/Any?type=single,twopart` and formats the response.

## License

MIT – see LICENSE file.
