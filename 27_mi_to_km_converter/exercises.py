import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Courier", 20, "italic"))
# placed and centered
my_label.pack(expand=True)

window.mainloop()
