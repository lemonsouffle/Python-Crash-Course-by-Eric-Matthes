# Изменение регистра символов в строках
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#Конкатенация
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

#Удаление пропусков
favourite_lang = ' python '
print(favourite_lang.rstrip())  #Удаление пропусков справа
print(favourite_lang.lstrip())  #Удаление пропусков слева
print(favourite_lang.strip())  #Удаление пропусков
