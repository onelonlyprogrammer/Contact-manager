import main
import tkinter as tk

window = tk.Tk()
window.title("Contact Manager")

usrInput = tk.Entry()

findButton = tk.Button(text = "Find contact", command = lambda: output(main.findContact(usrInput.get())))
addButton = tk.Button(text = "Add contact", command = lambda: output(main.addContact(usrInput.get().split(", "))))
deleteButton = tk.Button(text = "Delete contact", command = lambda: output(main.deleteContact(usrInput.get())))

label = tk.Label(window, text = "test")

usrInput.pack(side = tk.TOP)
label.pack()
findButton.pack()
addButton.pack()
deleteButton.pack()

def output(ret):
    label.configure(text = "")
    if type(ret) is list:
        for i in ret:
            label.configure(text = label.cget("text") + i + "\n")
    else:
        label.configure(text = ret)

window.geometry("500x200")
window.mainloop()
