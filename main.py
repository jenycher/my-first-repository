# Приложение для упрвления задачами
import tkinter as tk

#Функция добавления задачи
def add_task():
    task = task_entry.get() #[здесь мы получаем слова из поля для ввода]
    if task:
        task_listBox.insert(tk.END, task) #[здесь с помощью константы END вставляем полученное слово в конец списка]
        task_entry.delete(0, tk.END) #[здесь очищаем поле для ввода, от нулевого индекса и до конца]

#Функция удаления задачи
def delete_task():
    selected_task = task_listBox.curselection() #[с помощью функции curselection элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную selected_task]

    if selected_task:
         task_listBox.delete(selected_task) #[удаляем выбранный элемент из списка]

#Функция помечает задачу выполенненой
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue") #[с помощью функции itemconfig выполненная задача изменит цвет заливки]

#Функция снимает пометку, что задачу выполнена
def del_mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="coral3") #[с помощью функции itemconfig выполненная задача изменит цвет заливки]

root = tk.Tk()
root.title("Список задач")
root.configure(background="coral4")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="coral1", font="bold")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="cornsilk", font="bold")
#fg = “название_цвета”;
#font = “название_шрифта”

task_entry.pack(pady=10)
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task, font="bold")

add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task, font="bold")

delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task, font="bold")

mark_button.pack(pady=5)

del_mark_button = tk.Button(root, text="Снять отметку с выполненной задачи", command=del_mark_task, font="bold")
del_mark_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="coral1", font="bold")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="coral3", font="bold")


task_listBox.pack(pady=10)

root.mainloop()