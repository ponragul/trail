from  tkinter import*
from PIL import 

canvas = Canvas(width=1000, height=400, bg='blue')
canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file="D:\\project\\jarvis.jpg")
canvas.create_image(10, 10, image=image, anchor=NW)

mainloop()