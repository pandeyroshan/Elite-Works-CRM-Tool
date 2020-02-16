from fpdf import FPDF

class CreatePDF():

    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
    
    def write_left_bold(self,text,margin_top):
        self.pdf.set_font("Arial", size=12,style='B')
        self.pdf.cell(200, margin_top, txt=text,border=20, ln=1, align="L")
        pass

    def write_right_bold(self,text,margin_top):
        self.pdf.set_font("Arial", size=12,style='B')
        self.pdf.cell(200, margin_top, txt=text+"     ",border=20, ln=1, align="R")
        pass

    def write_center_bold(self,text,margin_top):
        self.pdf.set_font("Arial", size=12,style='B')
        self.pdf.cell(200, margin_top, txt=text,border=20, ln=1, align="C")
        pass

    def write_left_normal(self,text,margin_top):
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, margin_top, txt=text,border=20, ln=1, align="L")
        pass

    def write_right_normal(self,text,margin_top):
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, margin_top, txt=text,border=20, ln=1, align="R")
        pass

    def write_center_normal(self,text,margin_top):
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(150,margin_top, txt=text,border=20, ln=1, align="C")
        pass

    def write_normal(self,text,margin_top):
        self.pdf.set_font("Arial", size=12)
        self.pdf.write(margin_top,txt=text)
        pass

    def write_bold(self,text,margin_top):
        self.pdf.set_font("Arial", size=12,style='B')
        self.pdf.write(margin_top,txt=text)
        pass

    def draw_line(self):
        self.pdf.line(10, 10, 10, 100)
        self.pdf.set_line_width(1)
        self.pdf.set_draw_color(255, 255, 255)
        self.pdf.line(20, 20, 100, 20)
        pass

    def generate_pdf(self,file_name):
        self.pdf.output(file_name)

if __name__ == "__main__":

    pdf_object = CreatePDF()
    pdf_object.write_left_bold("EW/2020",10)
    pdf_object.write_right_bold("Date - Feb 16th, 2020",5)
    pdf_object.write_normal("To,\nThe Excutive Engineer\n400 KV Testing Division\nMPPTCL\nNagda",5)
    pdf_object.write_left_bold("Subject: Operation and Minor Operation work of 132 KV S/S Bhensola",30)
    pdf_object.write_left_normal("Respected Sir,",20)
    pdf_object.write_normal("Please find enclosed here with the bill in quadruplicate for the period of 11/02/2000 to 20/02/2020 in reference to order number 04-04/SE-II/TS-88/2019/2873 Dated 13/12/2019 from C.E. (T&C) Jabalpur\n",10)
    pdf_object.write_left_bold("Enclosures: ",10)
    pdf_object.write_left_normal("1. Covering Letter",5)
    pdf_object.write_left_normal("2. Bill",5)
    pdf_object.write_left_normal("3. Attendance Sheet",5)
    pdf_object.write_left_normal("4. Salary Sheet",5)
    pdf_object.write_left_normal("5. Statement",5)
    pdf_object.write_left_normal("6. Payment Reciept",5)
    pdf_object.write_left_normal("7. ERF",5)
    pdf_object.write_left_normal("8. ECR",5)
    pdf_object.write_left_normal("9. ESIC",5)
    pdf_object.write_left_normal("10. Payment Reciept",5)
    pdf_object.write_left_normal("11. ESIC Contribution",5)
    pdf_object.write_center_bold("Thanking You",20)
    pdf_object.write_right_normal('GST NO: 23ACMPK3187CIZR ',10)
    pdf_object.write_right_normal('PAN NO: ACMPK3187C',5)
    pdf_object.write_left_bold("M/s Elite Works",10)
    pdf_object.generate_pdf("sample.pdf")
    pass