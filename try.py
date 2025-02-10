import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Rounded Button Example")

# Set the size of the window
window.geometry("300x200")

# Function to be called when the button is clicked
def on_button_click():
    print("Rounded button was clicked!")

# Create a canvas to draw the rounded button
canvas = tk.Canvas(window, width=200, height=60)
canvas.pack(pady=50)

# Draw a rounded rectangle by combining ovals and rectangles
canvas.create_oval(0, 0, 40, 40, fill="lightblue", outline="blue")  # Top-left corner
canvas.create_oval(160, 0, 200, 40, fill="lightblue", outline="blue")  # Top-right corner
canvas.create_oval(0, 20, 40, 60, fill="lightblue", outline="blue")  # Bottom-left corner
canvas.create_oval(160, 20, 200, 60, fill="lightblue", outline="blue")  # Bottom-right corner
canvas.create_rectangle(40, 0, 160, 60, fill="lightblue", outline="blue")  # Middle part

# Create a label to display text on the "button"
label = tk.Label(window, text="Click Me", font=("Arial", 12), bg="lightblue")
label.place(x=100, y=30, anchor="center")

# Bind click event to the canvas (simulating the button)
canvas.tag_bind("button", "<Button-1>", lambda e: on_button_click())

# Run the window loop
window.mainloop()
