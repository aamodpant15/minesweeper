import tkinter as tk

# # Grid
# def create_grid(event=None):
#     w = c.winfo_width() # Get current width of canvas
#     h = c.winfo_height() # Get current height of canvas
#     c.delete('grid_line') # Will only remove the grid_line
#
#     # Creates all vertical lines at intevals of 100
#     # for i in range(0, w, 100):
#     for i in range(0, 1600, 100):
#         c.create_line([(i, 0), (i, h)], tag='grid_line')
#
#     # Creates all horizontal lines at intevals of 100
#     for i in range(0, 900, 100):
#     # for i in range(0, h, 100):
#         c.create_line([(0, i), (w, i)], tag='grid_line')
#
# root = tk.Tk()
#
# c = tk.Canvas(root, height=1000, width=1000, bg='white')
# c.pack(fill=tk.BOTH, expand=True)
#
# c.bind('<Configure>', create_grid)

##########

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

mainloop()

root.mainloop()
