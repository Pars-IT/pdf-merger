from pypdf import PdfWriter


def merge_pdfs(pdf_files: list[str], output: str = "merged_output.pdf") -> None:
    writer = PdfWriter()

    for pdf in pdf_files:
        writer.append(pdf)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Saved: {output}")


def main():
    pdf_files = [
        "file1.pdf",
        "file2.pdf",
        "file3.pdf"
    ]

    merge_pdfs(pdf_files)


if __name__ == "__main__":
    main()
