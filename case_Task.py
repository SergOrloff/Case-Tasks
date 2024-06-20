import tkinter as tk

global task_listBox
def add_task():
    task = task_entry.get() # [здесь мы получаем слова из поля для ввода]
    if task:
        task_listBox.insert(tk.END, task) #[здесь с помощью константы END ставляем полученное слово в конец списка]
        task_entry.delete(0, tk.END) #[здесь очищаем поле для ввода, от нулевого индекса и до конца]



def delete_task():
    selected_task = task_listBox.curselection() # [с помощью функции curselection элемент, на который мы нажмём,
    # будет передавать свой ID, индекс, в переменную selected_task]
    if selected_task:
        task_listBox.delete(selected_task) # [удаляем выбранный элемент из списка]

# Для экспорта всех элементов виджета списка элементов в файл служит функция на Python,
# которая принимает список элементов и имя файла для экспорта.
# def mark_task():
#     selected_task = task_listBox.curselection()
#     if selected_task:
#         task_listBox.itemconfig(selected_task, bg="chartreuse2") # [с помощью функции itemconfig выполненная
#         # задача изменит цвет заливки]
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_text = task_listBox.get(task_index)
        if '(вып.)' in task_text:
            return 0
        else:
            task_listBox.insert(task_index, f'{task_text} (вып.)')  # добавляем слово "вып."
            task_listBox.itemconfig(selected_task, bg="chartreuse2")  # изменяем фон на светло-зеленый
            task_listBox.delete(task_index+1)  # удаляем старый элемент

def save_task():
    save_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue") #


# Для импорта элементов из файла "Tasks.txt" в виджет списка элементов, созданный с помощью модуля tkinter,
# нужно прочитать файл, извлечь элементы и добавить их в виджет списка
def export_to_file():
    try:
        if task_listBox.size():
            with open("Tasks.txt", 'w', encoding="utf-8") as file:
                for i in range(task_listBox.size()):
                    file.write(task_listBox.get(i) + '\n')

        # with open("Tasks.txt", 'w', encoding="utf-8") as file:
        #     for element in task_listBox:
        #         file.write(str(element) + '\n')
            print(f'Элементы успешно экспортированы в файл "Tasks.txt"')
        else:
            print(f'Список пустой - нечего экспортировать в файл "Tasks.txt"')
    except Exception as e:
        print(f'Произошла ошибка при экспорте элементов: {e}')

def import_from_file():
    try:
        if task_listBox.size():
            return 0
        else:
            with open('Tasks.txt', 'r', encoding="utf-8") as file:
                tasks = file.readlines()
                for task in tasks:
                    task = task.strip()
                    if '(вып.)' in task:
                        task_listBox.insert(tk.END, task)
                        task_listBox.itemconfig(tk.END, bg="chartreuse2")
                    else:
                        task_listBox.insert(tk.END, task)
            print(f'Элементы успешно импортированы из файла "Tasks.txt"')
    except Exception as e:
        print(f'Произошла ошибка при импорте элементов из файла: {e}')

    except FileNotFoundError:
        print("Файл не найден")


root = tk.Tk()
root.title("Task list")
# 5. Меняем цвет заднего фона:
root.configure(background="HotPink")
# background — это атрибут, аргумент функции, который мы можем менять.
# Название цвета, которое можно использовать, мы находим на сайте https://letpy.com/handbook/tkinter-colors/
# 6. Создаём и позиционируем надпись, чтобы у поля для ввода задачи был заголовок:
text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink", font = ("Comic Sans MS", 11, "bold"))
text1.pack(pady=5)

# 7. Чтобы дать возможность вводить задачи, создаём переменную:
task_entry = tk.Entry(root, width=100, bg="LightPink1")

# 🧠Чтобы изменить цвет вводимого текста, используем:
# fg = “название_цвета”;
# font = “название_шрифта” (несильно различаются, можно не использовать без установки сторонних).

# 8. Чтобы выводить данную переменную на экране, прописываем:

task_entry.pack(pady=10)

# 🧠pady — перемещение элементов вверх-вниз, паддинг сверху и снизу;
# padx — перемещение элементов влево-вправо, паддинг слева и справа.

# 9. Создаём и позиционируем кнопку, которая будет добавлять задачу в список:

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task, font = (("Times New Roman"), 11, "bold"), width=35)
add_task_button.pack(pady=5)

# 10. Создаём и позиционируем кнопку, которая будет удалять задачу из списка:

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task, font = (("Times New Roman"), 11, "bold"), width=35)
delete_button.pack(pady=5)

# 11. Создаём и позиционируем кнопку, которая будет отмечать задачу выполненной:

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task, font = (("Times New Roman"), 11, "bold"), width=35)
mark_button.pack(pady=5)


save_button = tk.Button(root, text="Сохранить список задач в файле 'Tasks.txt'", command=export_to_file, font = (("Times New Roman"), 11, "bold"), width=35)
save_button.pack(pady=5)

rest_button = tk.Button(root, text="Загрузить список задач из файла 'Tasks.txt'", command=import_from_file, font = (("Times New Roman"), 11, "bold"), width=35)
rest_button.pack(pady=5)


# 12. Добавляем и позиционируем надпись, чтобы у списка задач был заголовок:

text2 = tk.Label(root, text="Список задач:", bg="HotPink", font = ("Comic Sans MS", 11, "bold"))
text2.pack(pady=5)

# 🧠Функция bg позволяет сделать заднюю заливку текста.

# 13. Используем новую команду, чтобы создать список, в который будут добавляться задачи:
task_listBox = tk.Listbox(root, height=20, width=80, bg="LightPink1", font = ("Comic Sans MS", 11))

# 14. Позиционируем список на экране:
task_listBox.pack(pady=10, padx=10)

# 15. Чтобы окно не закрывалось, прописываем:
root.mainloop()