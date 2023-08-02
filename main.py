import datetime as dt
import csv
import json

#Чтение заметок
def read_notes_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as f:
            notes = json.load(f)
            return notes
    except FileNotFoundError:
        return []


# Сохранение списка заметок в json
def save_notes(notes, file_name):
    with open(file_name, 'w', encoding='UTF-8') as f:
        json.dump(notes, f, indent=4)


# Сохранение списка заметок в csv
def save_notes_csv(notes, file_name):
    with open(file_name, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        for note in notes:
            writer.writerow([note['id'], note['title'], note['body'], note['timestamp']])


#Вывод на экран выбранной записи или списка
def print_notes(notes):
    if not notes:
        print('Заметка не найдена')
    else:
        for note in notes:
            print(f'ID:{note["id"]}')
            print(f'Заголовок:{note["title"]}')
            print(f'Тело заметки:{note["body"]}')
            print(f'Дата/время:{note["timestamp"]}')
            print('------------------')


#Добавление новой заметки
def add_note(notes):
    id = len(notes) + 1
    title = input('Введите заголовок - ')
    body = input('Введите тело заметки - ')
    timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_note = {
        'id':id,
        'title':title,
        'body':body,
        'timestamp':timestamp
    }

    notes.append(new_note)
    return notes

#Функция редактирования заметки
def edit_note(notes, id):
    for note in notes:
        if note['id'] == id:
            new_title = input('Введите новый заголовок (было: {note["title"]}):')
            new_body = input('Введите новое тело заметки (было: {note["body"]}):')
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            #break
            return notes

#Удаление заметки
def delete_note(notes, id):
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            #break
            return notes
        
def main():
    file_name = 'notes.json'
    notes = read_notes_file(file_name)

    while True:
        print('Выберите действие: ')
        print('1 - Вывести все заметки ')
        print('2 - Вывести конкретную заметку ')
        print('3 - Добавить заметку ')
        print('4 - Редактировать заметку ')
        print('5 - Удалить заметку ')
        print('6 - Выход ')
        choice = input('Ваш выбор:')
        print('______________________')
        if choice == '1':
            print_notes(notes)
        elif choice == '2':
            id = int(input('Введите ID заметки: '))
            note = [note for note in notes if note['id'] == id]
            print_notes(note)
        elif choice == '3':
            notes = add_note(notes)
            save_notes(notes, file_name)
        elif choice == '4':
            id = int(input('Введите ID заметки для редактирования: '))
            notes = edit_note(notes, id)
            save_notes(notes, file_name)
        elif choice == '5':
            id = int(input('Введите ID заметки для удаления: '))
            notes = delete_note(notes, id)
            save_notes(notes, file_name)
        elif choice == '6':
            break
        else:
            print('Нет такого пункта')


if __name__ == '__main__':

   main()