# CSV Cleaner

[绠€浣撲腑鏂嘳(README.zh-CN.md)

Trim cells, remove empty rows, and deduplicate CSV data using only the Python standard library.

## Highlights

- Python standard library only; no runtime dependencies.
- Command-line interface and automated tests included.
- Safe defaults and clear output.
- Windows, macOS, and Linux; Python 3.10+.

## Installation

```bash
git clone https://github.com/jellywong343-sys/csv-cleaner.git
cd csv-cleaner
python -m pip install -e .
```

Replace `jellywong343-sys` with your GitHub username.

## Usage

```bash
csv-clean messy.csv cleaned.csv
csv-clean messy.csv cleaned.csv --keep-duplicates
```

Run `csv-clean --help` to see every option.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
csv-cleaner/
鈹溾攢鈹€ src/csv_cleaner/
鈹溾攢鈹€ tests/
鈹溾攢鈹€ README.md
鈹溾攢鈹€ README.zh-CN.md
鈹溾攢鈹€ pyproject.toml
鈹斺攢鈹€ LICENSE
```

## Safety

Review command output before applying changes to important files. Keep backups of irreplaceable data.

## License

MIT

