import tkinter as tk
import matplotlib.pyplot as plt

lables = 'אל ללכב', 'הבר הדימב', 'דואמ'
sizes = [492, 50, 2]
colors = ['gold','yellowgreen','lightcoral']
plt.pie(sizes, labels=lables, colors=colors, autopct='%1.1f%%')
plt.show()


def show_image():
    img = tk.PhotoImage(file='img_6.1_3_2.png')
    varun_label = tk.Label(image=img)
    varun_label.pack()


window = tk.Tk()
label = tk.Label(
    text="whats my favorite video",
    fg="pink",
    bg="white",
)
button = tk.Button(text="click to find out!", command=show_image())
label.pack()
button.pack()
window.mainloop()


