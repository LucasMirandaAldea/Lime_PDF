from pypdf import PdfWriter

route = "C:/Users/liman/Documents/Currículum y búsqueda de trabajo/"

pdfs = ['Certificado Universitario Titulo - Lucas Miranda Aldea.pdf',
        'Certificado Laboral Hospital Bulnes.pdf',
        'Certificado Desafio Latam - English for Developers & IT Professionals.pdf',
        'Certificado Desafio Latam - React en acción - De cero a experto en Desarrollo Front End.pdf',
        'Certificado Udemy - Excel.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(route + pdf)

merger.write(route + "result.pdf")
merger.close()