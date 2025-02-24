import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")  # Set initial window size

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input Field
        self.input_frame = tk.Frame(master, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame,
                                     font=('arial', 18, 'bold'),
                                     textvariable=self.input_text,
                                     width=50,
                                     bg="#eee",
                                     bd=0,
                                     justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)  # Increase internal padding

        # Button Frame
        self.buttons_frame = tk.Frame(master, width=312, height=272.5, bg="grey")
        self.buttons_frame.pack()

        # Define Buttons (using grid layout)
        # Row 1
        self.clear = self.create_button(self.buttons_frame, text="C", row=1, column=0, command=lambda: self.clear_field())
        self.power = self.create_button(self.buttons_frame, text="^", row=1, column=1, command=lambda: self.press_key("^"))
        self.square_root = self.create_button(self.buttons_frame, text="√", row=1, column=2, command=lambda: self.square_root_op())
        self.divide = self.create_button(self.buttons_frame, text="/", row=1, column=3, command=lambda: self.press_key("/"))

        # Row 2
        self.seven = self.create_button(self.buttons_frame, text="7", row=2, column=0, command=lambda: self.press_key("7"))
        self.eight = self.create_button(self.buttons_frame, text="8", row=2, column=1, command=lambda: self.press_key("8"))
        self.nine = self.create_button(self.buttons_frame, text="9", row=2, column=2, command=lambda: self.press_key("9"))
        self.multiply = self.create_button(self.buttons_frame, text="*", row=2, column=3, command=lambda: self.press_key("*"))

        # Row 3
        self.four = self.create_button(self.buttons_frame, text="4", row=3, column=0, command=lambda: self.press_key("4"))
        self.five = self.create_button(self.buttons_frame, text="5", row=3, column=1, command=lambda: self.press_key("5"))
        self.six = self.create_button(self.buttons_frame, text="6", row=3, column=2, command=lambda: self.press_key("6"))
        self.minus = self.create_button(self.buttons_frame, text="-", row=3, column=3, command=lambda: self.press_key("-"))

        # Row 4
        self.one = self.create_button(self.buttons_frame, text="1", row=4, column=0, command=lambda: self.press_key("1"))
        self.two = self.create_button(self.buttons_frame, text="2", row=4, column=1, command=lambda: self.press_key("2"))
        self.three = self.create_button(self.buttons_frame, text="3", row=4, column=2, command=lambda: self.press_key("3"))
        self.plus = self.create_button(self.buttons_frame, text="+", row=4, column=3, command=lambda: self.press_key("+"))

        # Row 5
        self.zero = self.create_button(self.buttons_frame, text="0", row=5, column=0, columnspan=2, command=lambda: self.press_key("0")) # Span two columns
        self.decimal = self.create_button(self.buttons_frame, text=".", row=5, column=2, command=lambda: self.press_key("."))
        self.equals = self.create_button(self.buttons_frame, text="=", row=5, column=3, command=lambda: self.calculate())

    def create_button(self, frame, text, row, column, columnspan=1, command=None):
        """Helper function to create a button with consistent styling."""
        button = tk.Button(frame, text=text, padx=20, pady=20, font=('arial', 12, 'bold'),
                             bd=0, bg="white", cursor="hand2", command=command) # Set a default command to None to avoid immediate execution.
        button.grid(row=row, column=column, columnspan=columnspan, sticky=tk.NSEW)
        return button

    def press_key(self, number):
        """Updates the expression with the pressed key."""
        self.expression += str(number)
        self.input_text.set(self.expression)

    def clear_field(self):
        """Clears the input field."""
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        """Calculates the result of the expression."""
        try:
            result = str(eval(self.expression))  # Use eval with caution; see security note.
            self.input_text.set(result)
            self.expression = result #store result for next calculation
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear_field()
        except Exception as e:  # Catch all other errors.
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.clear_field()


    def square_root_op(self):
        """Calculates the square root of the current expression."""
        try:
            num = float(self.expression)
            if num < 0:
                raise ValueError("Cannot take the square root of a negative number")
            result = str(num**0.5)
            self.input_text.set(result)
            self.expression = result #store result for next calculation
        except ValueError as e:
            messagebox.showerror("Error", str(e)) #show the specific ValueError message
            self.clear_field()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.clear_field()


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()