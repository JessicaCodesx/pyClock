import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk, ImageSequence
import time
import os

# main window
root = tk.Tk()
root.title("Custom Clock")
root.geometry("500x270")  # Adjust height to fit everything snugly
root.overrideredirect(True)  # Borderless window

# window display settings
transparent_color = '#FFFFFF'
root.configure(bg=transparent_color)
root.attributes('-transparentcolor', transparent_color)
root.attributes('-alpha', 0.9) 

# centering window
screen_width = root.winfo_screenwidth()
window_width = 500
x_position = (screen_width - window_width) // 2
root.geometry(f"{window_width}x270+{x_position}+10")  # Adjusted height

# loading custom font
font_path = os.path.join("fonts", "Pacifico-Regular.ttf")  # Ensure the path is correct
custom_font_large = tkFont.Font(family="Pacifico", size=72)  # Larger font for time
custom_font_small = tkFont.Font(family="Pacifico", size=36)  # Smaller font for date

# loading and resizing gif
gif_path = os.path.join("images", "teddy.gif")  # Adjust path to your GIF
gif_image = Image.open(gif_path)

# resize gif frames
small_frames = [ImageTk.PhotoImage(frame.resize((70, 70))) for frame in ImageSequence.Iterator(gif_image)]
frame_count = len(small_frames)

# gif display label
gif_label = tk.Label(root, bg=transparent_color)  # Match transparent color for gif label
gif_label.pack(pady=(5, 0))  # Add padding to position above the time

# function to animate gif
def animate_gif(index=0):
    gif_label.config(image=small_frames[index])
    root.after(100, animate_gif, (index + 1) % frame_count)  # Change frame every 100ms

# start gif animation
animate_gif()

# function to update time display
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Schedule to update every second

# label for displaying time
time_label = tk.Label(root, bg=transparent_color, fg="#FFB6C1", font=custom_font_large)  # Set bg to transparent color
time_label.pack(pady=(5, 0))  # Small padding above date

# label for displaying date
date_label = tk.Label(root, bg=transparent_color, fg="#FFB6C1", font=custom_font_small)  # Set bg to transparent color
date_label.pack(pady=(0, 10))  # Small padding below date

# function to update date in "Mon. dd, yyyy" format
def update_date():
    current_date = time.strftime("%b. %d, %Y")
    date_label.config(text=current_date)
    root.after(86400000, update_date)  # Update daily
update_date()

# start updating time
update_time()

# draggable window pls
start_x = start_y = None
def start_drag(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
def do_drag(event):
    x = root.winfo_x() + (event.x - start_x)
    y = root.winfo_y() + (event.y - start_y)
    root.geometry(f"+{x}+{y}")
root.bind("<Button-1>", start_drag)
root.bind("<B1-Motion>", do_drag)

root.mainloop()
