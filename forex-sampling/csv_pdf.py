import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.page import PageMargins, PrintOptions
import pdfkit
import os
import sys
from multiprocessing import Pool

def convert_csv_to_pdf(csv_path):
    # Get the name of the CSV file without extension
    csv_filename = os.path.splitext(os.path.basename(csv_path))[0]

    # Reading CSV and create Excel file with conversion
    df = pd.read_csv(csv_path)

    exchange_rate = 130
    df['AmountKES'] = df.apply(lambda x: (x['Amount'] * exchange_rate) if x['Currency'] == 'USD' else (x['Amount'] if x['Currency'] == 'KES' else 0), axis=1)

    initial_name = csv_filename + "_Conversion"
    excel_filename = f'./{initial_name}.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f'File {initial_name}.xlsx created successfully')

    # loading the workbook and configure page settings
    wb = load_workbook(excel_filename)
    ws = wb.active

    # Setting page margins
    margins = PageMargins(left=0.5, right=0.5, top=0.5, bottom=0.5, header=0.3, footer=0.3)
    ws.page_margins = margins

    # Setting print options and page setup
    ws.print_options = PrintOptions(horizontalCentered=True, verticalCentered=True)
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = 9  # 9 is A4

    # Fit to one page
    ws.page_setup.fitToHeight = 1
    ws.page_setup.fitToWidth = 1

    # Save the modified workbook
    wb.save(excel_filename)

    # Convert the Excel file to HTML
    html_content = pd.read_excel(excel_filename).to_html(index=False)
    html_filename = f'./{initial_name}.html'
    with open(html_filename, 'w') as f:
        f.write(html_content)

    # Convert HTML to PDF using pdfkit
    # set destination to save the pdf in ubuntu Documents (/home/simon/Documents)
    pdf_directory = '/home/simon/Documents/forexPdf'
    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory)

    pdf_filename = f'{pdf_directory}/{initial_name}.pdf'
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    pdfkit.from_file(html_filename, pdf_filename, configuration=pdfkit_config)

    # Delete the HTML file
    os.remove(html_filename)
    
    print(f'File {initial_name}.pdf created successfully')

def process_csv_files(csv_files):
    with Pool() as pool:
        pool.map(convert_csv_to_pdf, csv_files)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 convert_csv_to_pdf.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the specified folder.")
        sys.exit(1)

    process_csv_files(csv_files)
    print("Conversion process completed.")
