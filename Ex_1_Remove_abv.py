#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = input('Введите текст: \n')
remove_txt = 'абв'
new_str = ' '.join(list(filter(lambda elem: remove_txt not in elem.lower(), my_str.split())))
print(f'Текст без {remove_txt}: {new_str}')