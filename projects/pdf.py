from fpdf import FPDF

class CreatePDFLetter():

    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
    
    def change_font(self):
        self.pdf.font_size = 20
    
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
        self.pdf.cell(200,margin_top, txt=text,border=20, ln=1, align="C")
        pass

    def write_center_underline(self,text,margin_top):
        self.pdf.set_font("Arial",size=12,style='U')
        self.pdf.cell(200,margin_top,txt=text,border=20,ln=1,align='C')
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
        self.pdf.line(10, 50, 200, 50)
        self.pdf.set_line_width(1)
        self.pdf.set_draw_color(255, 255, 255)
        self.pdf.line(20, 20, 100, 20)
        pass

    def generate_pdf(self,file_name):
        self.pdf.output(file_name)
    
    def normal_font(self):
        self.pdf.set_text_color(0,0,0)
    
    def write_red(self,text,margin_top):
        self.pdf.set_text_color(255,0,0)
        self.pdf.set_font("Arial", size=35,style='B')
        self.pdf.cell(200,margin_top, txt=text,border=20, ln=1, align="C")
        self.normal_font()
        pass