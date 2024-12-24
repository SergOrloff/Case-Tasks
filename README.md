# Task List Application

Это простое приложение на Python с использованием библиотеки Tkinter, которое позволяет управлять списком задач. Вы можете добавлять задачи, удалять их, отмечать как выполненные, а также импортировать и экспортировать задачи в файл.

## Основные функции

- **Добавление задачи**: Добавьте новую задачу в список.
- **Удаление задачи**: Удалите выбранную задачу из списка.
- **Отметка задачи как выполненной**: Отметьте задачу как выполненную, изменив её цвет и добавив метку "(вып.)".
- **Экспорт задач в файл**: Сохраните текущий список задач в текстовый файл.
- **Импорт задач из файла**: Загрузите задачи из текстового файла в список.

## Установка

Для запуска этой программы необходимо установить Python и библиотеку Tkinter. Tkinter обычно включена в стандартную библиотеку Python, но если у вас её нет, установите её с помощью менеджера пакетов вашего дистрибутива (например, `sudo apt-get install python3-tk` для Ubuntu).

## Использование

1. **Запуск приложения**: Запустите файл скрипта с помощью Python.

   ```bash
   python task_list.py
   ```

2. **Добавление задачи**: Введите задачу в поле ввода и нажмите "Добавить".

3. **Удаление задачи**: Выберите задачу и нажмите "Удалить".

4. **Отметка задачи как выполненной**: Выберите задачу и нажмите "Отметить как выполненную".

5. **Экспорт задач**: Нажмите "Экспортировать", чтобы сохранить задачи в файл "Tasks.txt".

6. **Импорт задач**: Нажмите "Импортировать", чтобы загрузить задачи из файла "Tasks.txt".

## Код

```python
import tkinter as tk

global task_listBox

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_text = task_listBox.get(task_index)
        if '(вып.)' in task_text:
            return
        else:
            task_listBox.insert(task_index, f'{task_text} (вып.)')
            task_listBox.itemconfig(selected_task, bg="chartreuse2")
            task_listBox.delete(task_index+1)

def export_to_file():
    try:
        if task_listBox.size():
            with open("Tasks.txt", 'w', encoding="utf-8") as file:
                for i in range(task_listBox.size()):
                    file.write(task_listBox.get(i) + '\n')
            print(f'Элементы успешно экспортированы в файл "Tasks.txt"')
        else:
            print(f'Список пустой - нечего экспортировать в файл "Tasks.txt"')
    except Exception as e:
        print(f'Произошла ошибка при экспорте элементов: {e}')

def import_from_file():
    try:
        if task_listBox.size():
            return
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
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f'Произошла ошибка при импорте элементов из файла: {e}')

root = tk.Tk()
root.title("Task List")
root.configure(background="HotPink")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink", font=("Comic Sans MS", 11, "bold"))
text1.pack(pady=5)

task_entry = tk.Entry(root, width=100, bg="LightPink1")
```

## Примечания

- Цвета и шрифты можно изменить по вашему усмотрению.
- Файл для импорта и экспорта задач называется `Tasks.txt` и должен находиться в той же директории, что и скрипт.
- Добавьте дополнительные функции для улучшения функциональности, например, сохранение состояния задач при закрытии приложения.
