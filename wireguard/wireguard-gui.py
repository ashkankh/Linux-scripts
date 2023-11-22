import tkinter as tk
from tkinter import PhotoImage
import subprocess



def status_canvas(color):
    # Create a small Canvas widget (10x10 pixels) with a white background
    status_canvas = tk.Canvas(root, width=15, height=15)
    status_canvas.pack()
    # Draw a red rectangle on the canvas (for illustration)
    status_canvas.create_oval(1, 1, 9, 9, fill=color ,outline=color)
    status_canvas.place(relx=0.05, rely=.96, anchor=tk.CENTER)

# Function for connection status :
def connection_status():
    process = subprocess.run(["wg", "show"], check=True, stdout=subprocess.PIPE )
    output = process.stdout.decode('utf-8')
    if len(output.splitlines()) < 10:  
        status_canvas("red")    
        # Create a label at the corner of the window to display connection status
        connection = tk.Label(root, text="Disconected", font=("Ubuntu", 9),fg="red")
        connection.place(relx=0.15, rely=.95, anchor=tk.CENTER)

    else :
        status_canvas("green")
        connection = tk.Label(root, text="Connected", font=("Ubuntu", 10),fg="green")
        connection.place(relx=0.15, rely=.95, anchor=tk.CENTER)

# Function to execute the "sudo wg-quick up wg" command
def button1_click():
    try:
        subprocess.run(["pkexec", "wg-quick", "up", "wg"], check=True)
        status_label.config(text="WireGuard is now up.")
    except subprocess.CalledProcessError:
        status_label.config(text="Error: Failed to start WireGuard.")
    finally :
        connection_status()

# Function to execute the "sudo wg-quick down wg" command
def button2_click():
    try:
        subprocess.run(["pkexec", "wg-quick", "down", "wg"], check=True)
        status_label.config(text="WireGuard is now down.")
    except subprocess.CalledProcessError:
        status_label.config(text="Error: Failed to stop WireGuard.")
    finally :
        connection_status()
        
# Create the main window
root = tk.Tk()
root.title("WireGuard Control")

# Set the fixed window size (400x300)
root.geometry("400x300")

# Set the minimum and maximum window sizes to the same fixed size
root.minsize(400, 300)
root.maxsize(400, 300)

# Check the initial connection status
connection_status()

# Load the transparent logo image
logo_image = PhotoImage(file="/home/ashkan/scripts/wireguard/transparent_logo.png")  # Replace with your transparent logo image file

# Create a label to display the logo in the header (top) of the window
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(pady=5)

# Position the logo in the header (top) of the window
logo_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Create the first button with a red background and Ubuntu font
button1_font = ("Ubuntu", 10, "bold")  # Replace with the desired font name, size, and style
button1 = tk.Button(root, text="Start WireGuard", command=button1_click, bg="#831618", fg="white", font=button1_font)  # Set background, text color, and font
button1.pack(pady=5)

# Create the second button with a red background and Ubuntu font
button2_font = ("Ubuntu", 10, "bold")  # Replace with the desired font name, size, and style
button2 = tk.Button(root, text="Stop WireGuard", command=button2_click, bg="#831618", fg="white", font=button2_font)  # Set background, text color, and font
button2.pack(pady=5)

# Create a label at the bottom of the window to display messages
status_label = tk.Label(root, text="", font=("Ubuntu", 10),fg="gray")
status_label.place(relx=0.5, rely=.95, anchor=tk.CENTER)

# Place the buttons in the middle of the window
button1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
