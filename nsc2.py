import tkinter as tk
from tkinter import messagebox

class BaseConverterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Base Converter")
        self.root.geometry("1200x800")
        self.create_widgets()

        

    def create_widgets(self):
    # Input fields

        self.logo = tk.PhotoImage(file="C:/Users/harsh/Desktop/Screenshot 2024-04-17 184226.png")  

        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.pack()




    
        self.number_label = tk.Label(self.root, text="Number:")
        self.number_label.pack()
        self.number_entry = tk.Entry(self.root)
        self.number_entry.pack()

        self.from_base_label = tk.Label(self.root, text="From Base:")
        self.from_base_label.pack()
        self.from_base_entry = tk.Entry(self.root)
        self.from_base_entry.pack()

        self.to_base_label = tk.Label(self.root, text="To Base:")
        self.to_base_label.pack()
        self.to_base_entry = tk.Entry(self.root)
        self.to_base_entry.pack()

    # Button to perform conversion
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.pack()

    # Result label
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.pack()
        self.result_text = tk.Text(self.root, height=1, width=20)
        self.result_text.pack()

        


    def convert(self):
        try:
            number = self.number_entry.get()
            from_base = int(self.from_base_entry.get())
            to_base = int(self.to_base_entry.get())

            if '.' in number:
                # Input is a decimal number
                decimal_number = float(number)
                converted_number = self.convert_decimal_to_base(decimal_number, to_base)
            else:
                # Input is a non-decimal number
                decimal_number = int(number, from_base)
                converted_number = self.convert_base(decimal_number, to_base)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, converted_number)
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid number and bases.")

    def convert_base(self, number, base):
        if number < 0:
            return '-' + self.convert_base(-number, base)
        else:
            digits = "0123456789ABCDEF"
            if number < base:
                return digits[number]
            else:
                return self.convert_base(number // base, base) + digits[number % base]

    def convert_decimal_to_base(self, number, base):
        integer_part = int(number)
        fractional_part = number - integer_part

        integer_part_str = self.convert_base(integer_part, base)
        
        fractional_part_str = ''
        if fractional_part != 0:
            fractional_part_str = '.'
            seen = set()
            while fractional_part != 0 and fractional_part not in seen:
                seen.add(fractional_part)
                fractional_part *= base
                digit = int(fractional_part)
                fractional_part_str += self.convert_base(digit, base)
                fractional_part -= digit
        
        return integer_part_str + fractional_part_str

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    converter = BaseConverterGUI()
    converter.run()
