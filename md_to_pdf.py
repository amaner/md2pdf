#!/usr/bin/env python3
"""
Markdown to PDF Converter

This script converts a Markdown file to a PDF file named 'output.pdf' in the same directory.
It uses Pandoc, which is much more reliable on macOS than WeasyPrint.

Usage:
    python md_to_pdf.py path/to/markdown_file.md

The output PDF will be saved as 'output.pdf' in the same directory as the input file.

Dependencies:
    - pandoc: For converting Markdown to PDF (install with: brew install pandoc)
"""

import os
import sys
import argparse
import subprocess
import tempfile

def markdown_to_pdf(markdown_path):
    """
    Convert a Markdown file to PDF using Pandoc and save it as 'output.pdf' in the same directory.
    
    This function performs the following steps:
    1. Determine the output PDF path
    2. Call Pandoc to convert the Markdown file to PDF
    
    Args:
        markdown_path (str): The path to the Markdown file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Determine output path (same directory as input file)
        output_dir = os.path.dirname(os.path.abspath(markdown_path))
        output_path = os.path.join(output_dir, 'output.pdf')
        
        # Create a temporary CSS file for styling
        css_content = """
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            margin: 2em;
            max-width: 50em;
            margin-left: auto;
            margin-right: auto;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #333;
            margin-top: 1.5em;
        }
        code {
            background-color: #f5f5f5;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        }
        pre {
            background-color: #f5f5f5;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
        }
        blockquote {
            border-left: 4px solid #ddd;
            padding-left: 1em;
            color: #666;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        img {
            max-width: 100%;
        }
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.css', delete=False) as temp_css:
            temp_css.write(css_content)
            css_path = temp_css.name
        
        # Build the pandoc command
        # Using the default PDF engine which is typically LaTeX-based
        cmd = [
            'pandoc',
            markdown_path,
            '-o', output_path,
            '--css', css_path,
            '--standalone'
        ]
        
        # Execute the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Clean up the temporary CSS file
        os.unlink(css_path)
        
        if result.returncode == 0:
            print(f"Successfully converted {markdown_path} to {output_path}")
            return True
        else:
            print(f"Error running pandoc: {result.stderr}")
            return False
    
    except Exception as e:
        # Catch and handle any exceptions that might occur during conversion
        print(f"Error converting Markdown to PDF: {e}")
        return False

def main():
    """
    Main entry point for the script.
    
    Parses command line arguments, validates the input file,
    and calls the markdown_to_pdf function to perform the conversion.
    """
    # Set up argument parser for command line interface
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('markdown_file', help='Path to the Markdown file to convert')
    
    # Parse arguments from command line
    args = parser.parse_args()
    
    # Check if the specified file exists
    if not os.path.isfile(args.markdown_file):
        print(f"Error: File '{args.markdown_file}' does not exist")
        sys.exit(1)
    
    # Check if the file has a Markdown extension (.md or .markdown)
    if not args.markdown_file.lower().endswith(('.md', '.markdown')):
        print(f"Warning: File '{args.markdown_file}' may not be a Markdown file")
    
    # Check if pandoc is installed
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: Pandoc is not installed or not in PATH")
        print("Please install Pandoc using: brew install pandoc")
        sys.exit(1)
    
    # Convert Markdown to PDF
    success = markdown_to_pdf(args.markdown_file)
    
    # Exit with appropriate status code (0 for success, 1 for failure)
    sys.exit(0 if success else 1)

# Standard boilerplate to call the main() function
if __name__ == "__main__":
    main()
