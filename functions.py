import random
import threading
import const
import sys

import tkinter as tk

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = const.driver
exit_browser_event = threading.Event()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x-35}+{y-70}")


def on_hover_enter(event, button):
    button.config(bg="cyan")


def on_hover_leave(event, button):
    button.config(bg="blue")


# Генерация телефона
def generate_phone(phone_label, entered_name, entered_last_name, entered_email, entered_password):
    phone = const.phone_number
    phone += random.choice(const.code)
    while len(phone) < 9:
        phone += random.choice(const.list_of_numbers)

    phone_label.config(text=f"Ваш сгенерированный номер: +375{phone}")
    name = entered_name
    email = entered_email

    with open("user_data.txt", "r+") as file:
        data = file.read()
        write_string = f"Имя: {name}, Email: {email}\n"
        if write_string not in data:
            file.write(write_string)
    update_page(phone, entered_name, entered_last_name, entered_email, entered_password)


# Открытие браузера с заполненными данными
def open_link(phone_label, link_entry, name_entry, last_name_entry, email_entry, password_entry):
    global driver
    link = link_entry.get()
    entered_name = name_entry.get()
    entered_email = email_entry.get()
    entered_last_name = last_name_entry.get()
    entered_password = password_entry.get()

    if driver is None:
        driver = webdriver.Chrome()
    driver.get(link)
    generate_phone(phone_label, entered_name, entered_last_name, entered_email, entered_password)


# Добавление на страницу значений, которые ввел пользователь

def update_page(phone, entered_name, entered_last_name, entered_email, entered_password):
    try:
        if entered_last_name and entered_password:
            name = entered_name
            email = entered_email
            last_name = entered_last_name
            password = entered_password

            first_name_input = driver.find_element(By.NAME, "first_name")
            last_name_input = driver.find_element(By.NAME, "last_name")
            email_input = driver.find_element(By.NAME, "email")
            phone_input = driver.find_element(By.NAME, "phone")
            password_input = driver.find_element(By.NAME, "password")

            first_name_input.clear()
            first_name_input.send_keys(name)

            last_name_input.clear()
            last_name_input.send_keys(last_name)

            email_input.clear()
            email_input.send_keys(email)

            phone_input.clear()
            phone_input.send_keys("+375" + phone)

            password_input.clear()
            password_input.send_keys(password)
        else:
            phone_input = driver.find_element(By.NAME, "tildaspec-phone-part[]")
            name_input = driver.find_element(By.NAME, "Name")
            email_input = driver.find_element(By.NAME, "Email")

            phone_input.clear()
            phone_input.send_keys(phone)

            name_input.clear()
            name_input.send_keys(entered_name)

            email_input.clear()
            email_input.send_keys(entered_email)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "confirmation_message")))

    except Exception as e:
        print(f"Error: {e}")


# Закрытие браузера
def close_browser():
    global driver
    if driver:
        driver.quit()


# Закрытие приложения
def exit_application(root, new_root):
    global driver

    if driver:
        driver.quit()

    # Close all open Toplevel windows
    for win in root.winfo_children():
        if isinstance(win, tk.Toplevel):
            win.destroy()

    # Close the main root window
    root.quit()
    sys.exit()



