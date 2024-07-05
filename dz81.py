import tkinter as tk
def func_hello():
    name = entry.get()
    label.config(text="Привет, " + name + "!")

root = tk.Tk()
root.title("Форма приветствия")

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

button = tk.Button(root, text="Введите Ваше имя", command=func_hello)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()