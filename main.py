import functions
import const

from functions import center_window

import tkinter as tk

root = tk.Tk()


def display_last_authentication_data():
    try:
        with open("user_data.txt", "r") as file:
            lines = file.readlines()
        if lines:
            last_data = lines[-1].strip()  # Получаем последнюю строку из файла
        else:
            last_data = None
    except FileNotFoundError:
        last_data = None

    if last_data:
        center_window(root, 450, 125)
        root.title("NumMaker")
        root.iconbitmap('images/logo_1.ico')
        root.configure(bg=const.BACKGROUND)
        message = tk.Label(root,
                           text=f"Хотите продолжить?\n{last_data}",
                           font=("Comic Sans MS", 13, "bold"),
                           fg="blue",
                           bg=const.BACKGROUND)
        message.pack(pady=10)
        yes_button = tk.Button(root,
                               text="Да",
                               command=lambda: open_authentication_window(last_data),
                               font=("Comic Sans MS", 10, "bold"),
                               fg="white",
                               bg='blue',
                               relief="groove",
                               bd=4,
                               width=4)
        yes_button.bind("<Enter>", lambda event: functions.on_hover_enter(event, yes_button))
        yes_button.bind("<Leave>", lambda event: functions.on_hover_leave(event, yes_button))
        no_button = tk.Button(root,
                              text="Нет",
                              command=lambda: open_authentication_window(None),
                              font=("Comic Sans MS", 10, "bold"),
                              fg="white",
                              bg='blue',
                              relief="groove",
                              bd=4,
                              width=4)
        no_button.bind("<Enter>", lambda event: functions.on_hover_enter(event, no_button))
        no_button.bind("<Leave>", lambda event: functions.on_hover_leave(event, no_button))
        yes_button.pack(side=tk.LEFT, padx=27)
        no_button.pack(side=tk.RIGHT, padx=27)
    else:
        open_authentication_window(None)


def open_authentication_window(last_data):
    root.withdraw()
    new_root = tk.Toplevel()
    new_root.title("NumMaker")
    new_root.iconbitmap('images/logo_1.ico')

    # Рассчитать ширину и высоту экрана
    screen_width = new_root.winfo_screenwidth()
    screen_height = new_root.winfo_screenheight()

    # Создание синей рамки для верхней линии
    top_line_frame = tk.Frame(new_root,
                              height=20,
                              width=screen_width,
                              bg='#32CAFB')
    top_line_frame.pack_propagate(False)  # Запретить изменение размера рамки
    top_line_frame.pack(side=tk.TOP)

    # Создание синей рамки для нижней линии
    bottom_line_frame = tk.Frame(new_root,
                                 height=20,
                                 width=screen_width,
                                 bg='#32CAFB')
    bottom_line_frame.pack_propagate(False)
    bottom_line_frame.pack(side=tk.BOTTOM)

    # Создание синей рамки для левой линии
    left_line_frame = tk.Frame(new_root,
                               height=screen_height - 2 * 40,
                               width=20, bg='#32CAFB')
    left_line_frame.pack_propagate(False)
    left_line_frame.pack(side=tk.LEFT)

    # Создание синей рамки для правой линии
    right_line_frame = tk.Frame(new_root,
                                height=screen_height - 2 * 40,
                                width=20,
                                bg='#32CAFB')
    right_line_frame.pack_propagate(False)
    right_line_frame.pack(side=tk.RIGHT)

    # Создание основной области контента
    content_frame = tk.Frame(new_root, bg=const.BACKGROUND)
    content_frame.pack()
    new_root.geometry('700x600+390+110')
    new_root.configure(bg=const.BACKGROUND)

    # Загрузка логотипа
    logo = tk.PhotoImage(file="images/origin.png")
    image_label = tk.Label(master=new_root,
                           image=logo,
                           bg=const.BACKGROUND)
    image_label.pack(pady=10)

    # Описание приложения
    description_label = tk.Label(new_root,
                                 text="Данное приложение создано для автоматического ввода\nданных о пользователе",
                                 font=const.font_for_title,
                                 fg="blue",
                                 bg=const.BACKGROUND)
    description_label.pack()

    # Пометка, что далее нужно будет вводить ссылку
    link_label = tk.Label(new_root,
                          text="Введите ссылку:",
                          font=const.custom_font_for_forms,
                          fg="blue",
                          bg="#BAF7F2")
    link_label.pack(pady=5)

    # Ввод ссылки
    link_entry = tk.Entry(new_root,
                          width=40)
    link_entry.pack()

    # Пометка, что далее нужно будет вводить имя пользователя
    name_label = tk.Label(new_root,
                          text="Введите Ваше имя:",
                          font=const.custom_font_for_forms,
                          fg="blue",
                          bg="#BAF7F2")
    name_label.pack(pady=5)

    # Ввод имени пользователя
    name_entry = tk.Entry(new_root,
                          width=40)
    name_entry.pack()
    if last_data:
        first_name = last_data.split(", ")[0][5:]
        name_entry.insert(0, first_name)
    name_entry.pack()

    last_name_label = tk.Label(new_root,
                           text="Введите Вашу фамилию:",
                           font=const.custom_font_for_forms,
                           fg="blue",
                           bg="#BAF7F2")
    last_name_label.pack(pady=5)

    # Ввод фамилии
    last_name_entry = tk.Entry(new_root,
                           width=40)
    last_name_entry.pack()

    # Пометка, что далее нужно будет вводить email-адрес
    email_label = tk.Label(new_root,
                           text="Введите Ваш email:",
                           font=const.custom_font_for_forms,
                           fg="blue",
                           bg="#BAF7F2")
    email_label.pack(pady=5)

    # Ввод email-адреса
    email_entry = tk.Entry(new_root,
                           width=40)
    email_entry.pack()
    if last_data:
        last_email = last_data.split(", ")[1].replace("Email: ", "")
        email_entry.insert(0, last_email)
    email_entry.pack()

    password_label = tk.Label(new_root,
                           text="Введите Ваш пароль:",
                           font=const.custom_font_for_forms,
                           fg="blue",
                           bg="#BAF7F2")
    password_label.pack(pady=5)

    # Ввод пароля
    password_entry = tk.Entry(new_root,
                           width=40)
    password_entry.pack()

    # Описание того, что делает кнопка "Старт"
    link_label = tk.Label(new_root,
                          text="Когда Вы нажмете кнопку 'Старт', программа автоматически сгенерирует новый"
                               "\nномер телефона, а так же заполнит данные за Вас",
                          font=("Comic Sans MS", 11),
                          fg="blue",
                          bg=const.BACKGROUND)
    link_label.pack(pady=10)

    # Вывод сгенерированного телефона
    phone_label = tk.Label(new_root,
                           text="",
                           font=const.custom_font_for_forms,
                           fg="red",
                           bg=const.BACKGROUND)
    phone_label.pack()

    # Создание отдельного блока, в который будут помещаться кнопки "Старт" и "Закончить работу программы"
    button_frame = tk.Frame(new_root, bg=const.BACKGROUND)
    button_frame.pack(pady=10)

    # Кнопка, для старта работы программы
    open_button = tk.Button(button_frame,
                            text="Старт",
                            command=lambda: functions.open_link(phone_label, link_entry, name_entry, last_name_entry, email_entry, password_entry),
                            font=("Comic Sans MS", 11, "bold"),
                            fg="white",
                            bg='blue',
                            relief="groove",
                            bd=3)
    open_button.pack(side=tk.LEFT,
                     padx=10)

    # Бинд - при наведении на кнопку, она меняет цвет
    open_button.bind("<Enter>", lambda event: functions.on_hover_enter(event, open_button))
    open_button.bind("<Leave>", lambda event: functions.on_hover_leave(event, open_button))

    # Кнопка, для окончания работы программы
    exit_button = tk.Button(button_frame,
                            text="Закончить работу программы",
                            command=lambda: functions.exit_application(root, new_root),
                            font=("Comic Sans MS", 11, "bold"),
                            fg="white",
                            bg='blue',
                            relief="groove",
                            bd=3)
    exit_button.pack(side=tk.LEFT,
                     padx=10)

    # Бинд - при наведении на кнопку, она меняет цвет
    exit_button.bind("<Enter>", lambda event: functions.on_hover_enter(event, exit_button))
    exit_button.bind("<Leave>", lambda event: functions.on_hover_leave(event, exit_button))

    # mainloop обеспечивает постоянную работу главного окна и его объектов до момента, когда оно будет закрыто
    new_root.mainloop()


if __name__ == "__main__":
    display_last_authentication_data()
    root.mainloop()

