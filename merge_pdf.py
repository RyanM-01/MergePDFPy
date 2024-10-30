#import necessary libraries
import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog
#create merge pdf function
def merge_pdfs(pdf_list, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog from tk to select multiple PDF file:
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_files:
        print("No files selected. Exiting.")
        exit()

    # Specify the fixed output directory
    output_directory = "Path/To/Your/Destination/File"  # Update this line with your choosing
    output_file = os.path.join(output_directory, "merged_file.pdf")

    # Merge PDFs
    merge_pdfs(pdf_files, output_file)

    print(f"Successfully Merged {len(pdf_files)} PDFs into '{output_file}'")
    print(f"Thank you for using this script")
