# PDF Merger

Small Python utility for merging multiple PDF files into a single output file using [`pypdf`](https://pypdf.readthedocs.io/).

## Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/)

## Installation

```bash
poetry install
```

## Project Structure

```text
src/pdf_merger/main.py
```

The main merge function is:

```python
merge_pdfs(pdf_files: list[str], output: str = "merged_output.pdf") -> None
```

## Usage

### Use as a Python function

```python
from pdf_merger.main import merge_pdfs

merge_pdfs(
    ["file1.pdf", "file2.pdf", "file3.pdf"],
    output="combined.pdf",
)
```

### Run the example script

The current `main()` function looks for sequential files in the working directory:

- `file1.pdf` is required
- `file2.pdf` through `fileN.pdf` are merged automatically while they exist

Run `main()` with:

```bash
poetry run start
```

This command runs the `main()` function in `src/pdf_merger/main.py`.

If `file1.pdf` does not exist, the script prints an error and exits.

## Output

By default, merged PDFs are written to:

```text
merged_output.pdf
```

You can change the destination by passing a different `output` path to `merge_pdfs(...)`.

## Example

```python
from pdf_merger.main import merge_pdfs

monthly_reports = [
    "jan.pdf",
    "feb.pdf",
    "mar.pdf",
]

merge_pdfs(monthly_reports, output="q1-report.pdf")
```
