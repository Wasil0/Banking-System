from fpdf import FPDF

class PDF(FPDF):
    """
    Custom PDF class for creating tables with headers and data rows.
    """
    header_text = "NOVA BANKING"
    
    def header(self):
        """
        Method to create the header section of the PDF.
        """
        self.set_font("helvetica", "BUI", 40)
        self.set_text_color(147, 112, 219)
        self.set_fill_color(255, 255, 255)
        self.cell(0, 40, txt=PDF.header_text, align="C", fill=True)
        self.ln(40)
        
    def create_table(self, title: str, database: list):
        """
        Method to create a table in the PDF.
        
        Args:
            title (str): The title of the table.
            database (list): The data for the table.
        
        Returns:
            str: Error message if the title is not valid, otherwise None.
        """
    
        if title == "SavingAccountUsers":
            col_width = 32
            heading_font = 10
            font_size = 9
        
        elif title == "CheckingAccountUsers":
            col_width = 25.3
            heading_font = 8
            font_size = 6
        
        elif title == "LoanAccountUsers":
            col_width = 25.3
            heading_font = 8
            font_size = 6
        
        else:
            return "Set one of the user table to True, Only one of them."
        
        self.set_text_color(238, 130, 238)
        row_height = 10
        self.set_font("Times", "BIU", 25)
        self.cell(0, 10, title, align="C")
        self.ln(20)

        self.set_font("Times", "IB", heading_font)
        header = database[0]
        
        self.set_fill_color(200, 200, 200)
        self.set_text_color(0)
        
        # Header row
        for header_cell in header:
            self.cell(col_width, row_height, header_cell, border=1, align="C", fill=True)
        
        self.ln()
        self.set_font("helvetica", "I", font_size)
        self.set_fill_color(230, 230, 250)
        self.set_text_color(0)

        # Data rows
        for data_row in database[1:]:
            for datum in data_row:
                self.cell(col_width, row_height, str(datum), border=1, align="C", fill=True)
            self.ln()

        self.output(f"{title}.pdf")
