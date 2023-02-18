import model, view

import os
os.system('cls') # чистим консоль

print('ЗАМЕТКИ')
var = input('1. Посмотреть записи\n2. Добавить запись\n3. Редактировать запись\n4. Экспортировать в файл\n0. Выход\n-> ')

if var == '1':
    os.system('cls')
    data = model.readAll()
    view.showToScreenABC(data)
if var == '2':
    head = input("Введите название темы: ")
    body = input("Введите текст записи: ")
    model.add(head, body)
    print("Сохранено!")
if var == '3':
    os.system('cls')
    data = model.readAll()
    view.showToScreen(data)
    index = input(' Выберите запись для редактирования -> ')
    head = input(" Введите название темы: ")
    body = input(" Введите текст записи: ")
    model.edit(head, body, index)
    print("Сохранено!")
if var == '4':
    subvar = input(' 1. В формате TXT\n 2. В формате HTML\n 3. В формате XML\n 4. В формате CSV\n 0. Выход\n-> ')    
    if subvar == '1':
        data = model.readAll()    
        view.saveToTXT(data)
        print("Сохранено!")  
    if subvar == '2':
        data = model.readAll()
        view.saveToHTML(data)
        print("Сохранено!")
    if subvar == '3':
        data = model.readAll()
        view.saveToXML(data)
        print("Сохранено!")
    if subvar == '4':
        data = model.readAll()
        view.saveToCSV(data)
        print("Сохранено!")


