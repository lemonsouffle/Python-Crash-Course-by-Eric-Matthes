# 2-3. Личное сообщение: сохраните имя пользователя в переменной и выведите сообщение, 
# предназначенное для конкретного человека. Сообщение должно быть простым, например:
# “Hello Eric, would you like to learn some Python today?” 
username = 'Elena'
message = 'Hello ' + username + ', would you like to learn some Python today?'
print(message)

# 2-4. Регистр символов в именах: сохраните имя пользователя в переменной и выведите его
# в нижнем регистре, в верхнем регистре и с капитализацией начальных букв каждого слова.
my_name = 'elena sviridova'
print(my_name.lower())
print(my_name.upper())
print(my_name.capitalize())
print(my_name.title())

# 2-5. Знаменитая цитата: найдите известное высказывание, которое вам понравилось. 
# Выведите текст цитаты с именем автора. 
# Результат должен выглядеть примерно так (включая кавычки):
# Albert Einstein once said, "A person who never made a mistake never tried anything new."
quote = 'The pain of studying is only temporary. But the pain of not knowing – ignorance — is forever.'
print('"' + quote + '", is written in ' + "Harvard University's motivation book")

# 2-6. Знаменитая цитата 2: повторите упражнение 2-5, но на этот раз сохраните имя автора
# цитаты в переменной famous_person. Затем составьте сообщение и сохраните его в новой
# переменной с именем message. Выведите свое сообщение.
famous_person = 'Harvard University'
quote = 'The pain of studying is only temporary. But the pain of not knowing – ignorance — is forever.'
print('"' + quote + '", is written in ' + famous_person + "'s motivation book")

# 2-7. Удаление пропусков: сохраните имя пользователя в переменной. 
# Добавьте в начале и в конце имени несколько пропусков. 
# Проследите за тем, чтобы каждая служебная последовательность, “\t” и “\n”, встречалась по крайней мере один раз.
# Выведите имя, чтобы были видны пропуски в начале и конце строки. Затем выведите его
# снова с использованием каждой из функций удаления пропусков: lstrip(), rstrip() и strip().
username = '\t\n\n\n   lemonsouffle   \t\n'
print(username.lstrip())
print(username.rstrip())
print(username.strip())