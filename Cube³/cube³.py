import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


def help_click():
    messagebox.showinfo(
        "How To Use",
        "Enter the length, width, and height of a cube to calculate the surface area and volume. \
        This application also works with distorted cubes."
    )


def about_click():
    messagebox.showinfo(
        "About",
        "Created by Brandon Jones\n2024©"
    )


class Cube:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()

        # Set the window title
        self.root.title("Cube³")

        # Set the window size
        self.root.geometry('285x415')

        # Create a help bar
        menu_bar = tk.Menu(
            self.root,
            background="#b3bece",
            foreground="#001635"
        )

        help_menu = tk.Menu(
            menu_bar,
            background="#b3bece",
            foreground="#001635",
            tearoff=0
        )

        help_menu.add_command(
            label='How To Use...',
            background="#b3bece",
            foreground="#001635",
            command=help_click
        )

        help_menu.add_command(
            label='About',
            background="#b3bece",
            foreground="#001635",
            command=about_click
        )

        menu_bar.add_cascade(
            label='Help',
            menu=help_menu
        )

        # Configure help menu bar
        self.root.config(menu=menu_bar)

        # Create frame for C-Cubed logo
        self.logo_frame = tk.Frame(
            self.root,
            background="#42486C"
        )
        self.logo_frame.pack(fill=tk.X)

        # Add to logo_frame
        photo = tk.PhotoImage(file="cube³.png")
        self.image_label = tk.Label(
            self.logo_frame,
            image=photo,
            relief=tk.GROOVE,
            borderwidth=5,
            background="#42486C",
            width=98,
            height=98
        )
        self.image_label.pack()

        # Create labels, entry fields, and buttons for length, width, and height
        self.length_frame = tk.Frame(
            self.root,
            background="#42486C"
        )
        self.length_frame.pack(fill=tk.X)

        self.length_label = tk.Label(
            self.length_frame,
            text="Length:",
            font=("gothic", 14),
            background="#42486C",
            foreground="#B4D9E0",
            height=3
        )
        self.length_label.pack(side="left", fill=tk.X)

        self.length_entry = tk.Entry(
            self.length_frame,
            font=("gothic", 12),
            background="#b3bece",
            foreground="#001635"
        )
        self.length_entry.pack(side="right", fill=tk.X)

        self.width_frame = tk.Frame(
            self.root,
            background="#42486C"
        )
        self.width_frame.pack(fill=tk.X)

        self.width_label = tk.Label(
            self.width_frame,
            text="Width:",
            font=("gothic", 14),
            background="#42486C",
            foreground="#B4D9E0",
            height=3
        )
        self.width_label.pack(side="left")

        self.width_entry = tk.Entry(
            self.width_frame,
            font=("gothic", 12),
            background="#b3bece",
            foreground="#001635"
        )
        self.width_entry.pack(side="right")

        self.height_frame = tk.Frame(
            self.root,
            background="#42486C"
        )
        self.height_frame.pack(fill=tk.X)

        self.height_label = tk.Label(
            self.height_frame,
            text="Height:",
            font=("gothic", 14),
            background="#42486C",
            foreground="#B4D9E0",
            height=3
        )
        self.height_label.pack(side="left")

        self.height_entry = tk.Entry(
            self.height_frame,
            font=("gothic", 12),
            background="#b3bece",
            foreground="#001635"
        )
        self.height_entry.pack(side="right")

        # Create button for calculating surface area and volume
        self.calculate_frame = tk.Frame(
            self.root,
            background="#42486C"
        )
        self.calculate_frame.pack(fill=tk.X)

        self.calculate_button = tk.Button(
            self.calculate_frame,
            text="Calculate",
            command=self.calculate,
            font=("gothic", 14),
            background="#b3bece",
            relief=tk.RAISED,
            borderwidth=3,
            foreground="#001635"
        )
        self.calculate_button.pack()

        # Prints system fonts to the console for testing purposes
        available_fonts = [f for f in tkfont.families()]
        print(available_fonts)

        # This is not an erroneous extra call, it is essential for image to display
        self.root.mainloop()

    def calculate(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())

            # Calculate surface area and volume
            surface_area = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
            volume = length * width * height

            # Display results in a message box
            messagebox.showinfo(
                "Results",
                f"Surface Area: {surface_area:.2f}\nVolume: {volume:.2f}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid input. Please enter valid numbers."
            )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    cube = Cube()
    cube.run()
