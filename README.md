# Markdown to PDF Converter

A simple command-line application that converts Markdown files to PDF format using Pandoc.

## Installation

1. Clone this repository or download the files
2. Install Pandoc (required):

```bash
# On macOS using Homebrew
brew install pandoc
```

No Python package dependencies are required for this version.

## Usage

Run the script with a Markdown file as an argument:

```bash
python md_to_pdf.py path/to/your/file.md
```

The script will generate a file named `output.pdf` in the same directory as the input Markdown file.

## Features

- Converts Markdown to beautifully formatted PDF using Pandoc
- Supports common Markdown features including:
  - Headers
  - Lists
  - Code blocks
  - Tables
  - Blockquotes
  - Images
- Simple command-line interface
- Outputs to a PDF file in the same directory as the input file
- Works reliably on macOS without complex dependencies

## Requirements

- Python 3.6 or higher
- Pandoc (installed via Homebrew or other package manager)

## Why Pandoc?

This tool uses Pandoc instead of WeasyPrint because:

1. Pandoc is easier to install and maintain on macOS
2. It has fewer system dependencies
3. It produces high-quality PDFs with excellent typography
4. It's actively maintained and widely used

Pandoc uses a LaTeX-based PDF engine by default, which produces professional-looking documents.
