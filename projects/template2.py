from pdf import CreatePDFLetter


if __name__ == "__main__":
    pdf_object = CreatePDFLetter()
    pdf_object.write_right_bold("Ph. No: (0) 0755-4901229",10)
    pdf_object.write_right_bold("Mob. : +91 94250 05975",5)
    pdf_object.write_red("ELITE WORKS",10)
    pdf_object.write_center_bold("Class - A, Electrical Contractor",5)
    pdf_object.write_center_bold("Resi.: F-42, Vaishnav Apartment, Surendra Palace, Bhopal-26",5)
    pdf_object.draw_line()
    pdf_object.write_left_bold("Ref : ...........................",25)
    pdf_object.write_right_bold("Date : ...........................",0)
    pdf_object.write_left_normal("EW/2020",10)
    pdf_object.write_center_underline("Tax Invoice",10)
    pdf_object.generate_pdf("Template2.pdf")