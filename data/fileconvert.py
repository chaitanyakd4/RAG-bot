from pdfminer.high_level import extract_text

# Extract text from PDF
text = extract_text("chanty12.pdf")

# Save as Markdown
with open("chanty12.md", "w", encoding="utf-8") as md_file:
    md_file.write(text)
