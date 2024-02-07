import tkinter as tk
from tkinter import ttk, messagebox, font
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (selected_task,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List using Python")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#E6E6FA")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#4169E1")
    functions_frame = tk.Frame(guiWindow, bg="#4169E1")
    listbox_frame = tk.Frame(guiWindow, bg="#4169E1")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both", padx=10)
    listbox_frame.pack(side="right", expand=True, fill="both", padx=10)

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Brush Script MT", 30),
        background="#87CEEB",
        foreground="#191970"
    )
    header_label.pack(pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Times New Roman", 12, "bold"),
        background="#F0F8FF",
        foreground="#000000"
    )
    task_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    task_field = ttk.Entry(
        functions_frame,
        font=("Times New Roman", 12),
        width=25,
        background="#FFFFFF",
        foreground="#000000"
    )
    task_field.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    buttons_font = font.nametofont("TkDefaultFont")
    buttons_font.configure(size=10)  # Adjusting the font size for buttons

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=20,
        command=add_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=20,
        command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=20,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=20,
        command=close
    )

    add_button.grid(row=1, column=0, pady=10, sticky="w")
    del_button.grid(row=2, column=0, pady=10, sticky="w")
    del_all_button.grid(row=3, column=0, pady=10, sticky="w")
    exit_button.grid(row=4, column=0, pady=10, sticky="w")

    task_listbox = tk.Listbox(
        listbox_frame,
        width=30,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.pack(padx=10, pady=10)

    retrieve_database()
    list_update()

    guiWindow.mainloop()

    the_connection.commit()
    the_connection.close()
import tkinter as tk
from tkinter import ttk, messagebox, font
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (selected_task,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List using Python")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#E6E6FA")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#4169E1")
    functions_frame = tk.Frame(guiWindow, bg="#4169E1")
    listbox_frame = tk.Frame(guiWindow, bg="#4169E1")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both", padx=10)
    listbox_frame.pack(side="right", expand=True, fill="both", padx=10)

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Times New Roman", 30),
        background="#87CEEB",
        foreground="#191970"
    )
    header_label.pack(pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Times New Roman", 12, "bold"),
        background="#F0F8FF",
        foreground="#000000"
    )
    task_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    task_field = ttk.Entry(
        functions_frame,
        font=("Times New Roman", 12),
        width=25,
        background="#FFFFFF",
        foreground="#000000"
    )
    task_field.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    buttons_font = font.nametofont("TkDefaultFont")
    buttons_font.configure(size=10)  # Adjusting the font size for buttons

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=20,
        command=add_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=20,
        command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=20,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=20,
        command=close
    )

    add_button.grid(row=1, column=0, pady=10, sticky="w")
    del_button.grid(row=2, column=0, pady=10, sticky="w")
    del_all_button.grid(row=3, column=0, pady=10, sticky="w")
    exit_button.grid(row=4, column=0, pady=10, sticky="w")

    task_listbox = tk.Listbox(
        listbox_frame,
        width=30,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.pack(padx=10, pady=10)

    retrieve_database()
    list_update()

    guiWindow.mainloop()

    the_connection.commit()
    the_connection.close()
