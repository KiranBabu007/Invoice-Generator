import pdfkit

html_file = 'index.html'
output_pdf = 'invoice.pdf'

config = pdfkit.configuration(wkhtmltopdf='./wkhtmltopdf.exe')

with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

pdfkit.from_string(html_content, output_pdf, configuration=config, options={'margin-top': '10mm', 'margin-right': '10mm', 'margin-bottom': '10mm', 'margin-left': '10mm'})

