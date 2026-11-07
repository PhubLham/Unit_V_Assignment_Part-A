import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title and dimensions
root.title("Hello World - Phub Lham")
root.geometry("350x200")

# Create a label
message_label = tk.Label(
    root,
    text="Welcome! Click the button below."
)

message_label.pack(pady=20)

# Function executed when button is clicked
def show_message():
    message_label.config(
        text="Hello! You clicked the button."
    )

# Create a button and connect it to the function
hello_button = tk.Button(
    root,
    text="Click Me",
    command=show_message
)

hello_button.pack(pady=10)

# Start the event loop
root.mainloop()
