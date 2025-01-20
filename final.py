note = ["username" ,

"title",

"content",

"status",

"created_date",

"issue_date"
        ]

username = input( 'Введите Ваше имя: ')
print( username )

title = input( 'Введите Заголовок заметки: ')
print(title)

title1 = input('введите подзаголовок 1: ')
title2 = input('введите подзаголовок 2: ')
title3 = input('введите подзаголовок 3: ')
print(title1, title2, title3)

content = input( 'Напишите описание заметки: ')
print(content)

status = input( 'Укажите статус заметки: ')
print(status)

created_date = input("дата создания заметки в формате день-месяц-год: ")
print(created_date)

issue_date = input("дата истечения заметки в формате день-месяц-год: ")
print(issue_date)

note.insert(2,["Заголовок1", "Заголовок2", "Заголовок3"])
print(note)
