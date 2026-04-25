from pathlib import Path

from pypdf import PdfWriter


def merge_pdfs(pdf_files: list[str], output: str = "merged_output.pdf") -> None:
    writer = PdfWriter()

    for pdf in pdf_files:
        writer.append(pdf)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Saved: {output}")


def collect_pdf_files() -> list[str]:
    pdf_files: list[str] = []
    index = 1

    first_file = Path("file1.pdf")
    if not first_file.exists():
        raise FileNotFoundError("file1.pdf not found")

    while True:
        pdf_path = Path(f"file{index}.pdf")
        if not pdf_path.exists():
            break
        pdf_files.append(str(pdf_path))
        index += 1

    return pdf_files


def main():
    try:
        pdf_files = collect_pdf_files()
    except FileNotFoundError as error:
        print(f"Error: {error}")
        raise SystemExit(1) from error

    merge_pdfs(pdf_files)


if __name__ == "__main__":
    main()
