import fitz
import os

def fill_certificate(input_pdf, output_folder, names, x, y, font_path):
    doc_template = fitz.open(input_pdf)

    for name in names:
        doc = fitz.open()
        doc.insert_pdf(doc_template)

        page = doc[0]

        fontname = "Bernard_MT_Condensed"
        page.insert_font(fontname=fontname, fontfile=font_path)

        page.insert_textbox((x, y, x + 400, y + 50), name,
                            fontsize=30,
                            fontname=fontname,
                            color=(1, 1, 1))

        output_pdf = os.path.join(output_folder, f"{name.replace(' ', '_')}.pdf")
        doc.save(output_pdf)
        doc.close()
        print(f"Certificate saved as {output_pdf}")

    doc_template.close()

input_pdf = r"C:\Users\KIIT\Desktop\GOC\GOC_Cert\CertificatesAA-1.pdf"
output_folder = r"C:\Users\KIIT\Desktop\GOC\AA_Participants_Cert"
font_path = r"C:\Windows\Fonts\BERNHC.ttf"
os.makedirs(output_folder, exist_ok=True)

names_list = [
    ""
]

fill_certificate(input_pdf, output_folder, names_list, x=200, y=292, font_path=font_path)
