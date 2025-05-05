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
    "Jiya Jaiswal", "Shailaja Tewary", "Rudrangshu Roy", "Anindo Choudhury", "Asmit Saha", "Prapalin Mishra", "Akash Agarwal", "Mayank Mishra", "Ujjwal Singh", "Sayed Atique Ahmad", "Apoorva Deep", "Aryan Aggarwal", "Aditya Kumar Gupta", "Ayush Ranjan", "Ashmit Avash", "Sanskar Pandey", "Vinayak Tiwari", "Rishav Pattnaik", "Soham Mukherjee", "Utkarsh Jha", "Mukund Kushwaha", "Subhasmita Debata", "Sushree Priyadarshini Upadhyaya", "Meethi Saxena", "Shreyansh Satapathy", "Arya Roy", "Subham Shah", "Maanas Sehgal", "Monick Verma", "Saurabh", "Rudrani Dash", "Koushik Shaw", "Isha Rani", "Suyash Kumar Laur", "Rajat Shubhra D. Kumawat", "Souradip Saha", "Sarmistha Rout", "Shyam Goyal", "Sahil Singhal", "Shiva Krishna Yadav", "Kshitij Gupta", "Kumar Priyanshu", "Ashish Kumar", "Pranav Agrawal"
]

fill_certificate(input_pdf, output_folder, names_list, x=200, y=292, font_path=font_path)
