# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы которой читаются из текстового файла.
import sys
import shelve

def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf=8')
    except IOError as e:
        print("Невозможно открыть файл.", file_name, ". Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    ball = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, ball, explanation

def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t%s\n" % title)

def player():
    """Ввод имени игрока"""
    name_player = input("\n\tВведите ваш логин: ")
    return name_player

def read_record(name_player):
    try:
        s = open("record.txt", "r", encoding='utf-8')
    except:
        scope_record = None
        return
    
    for line in s:
        if line.strip() == name_player:
            scope_record = s.readline()
            s.close()
            return scope_record
    scope_record = None
    s.close()
    return scope_record

def save_record(name_player, scope):
    s = open("record.txt", "r", encoding='utf-8')
    text = []
    for line in s:
        text.append(line)
    if len(text) == 0:
        text = [name_player+"\n", str(scope)+"\n"]
    else:
        pos = 0
        for line in text:    
            if line.strip() == name_player:
                text[pos+1] = str(scope)+"\n"
                break
            pos += 1
        else:
            text.append(name_player+"\n")
            text.append(str(scope)+"\n")
    s = open("record.txt", "w", encoding='utf-8')
    s.writelines(text)
    s.close()
    return

def record(name_player, scope):
    scope_record = read_record(name_player)
    if not scope_record:
        print("У вас еще нет достижений!")
    elif scope > int(scope_record):
        print("У вас новое достижение: %s баллов" % scope)
            
    else:
        print("Ваш рекорд составляет: %s баллов" % scope_record)
        return 
    save_record(name_player, scope)
    return



def main():
    trivia_file = open_file("trivia_1.txt", "r")
    name_player = player()
    title = next_line(trivia_file)
    welcome(title)
    scope = 0



    # извлечение первого блока
    category, question, answers, correct, ball, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t%s - %s" % (i +1, answers[i]))

        # получение ответа
       
        answer = input("Ваш ответ: ")

        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            scope += int(ball)
        else:
            print("\nНет.", end=" ")
        print(explanation)
        print("Счет: %s\n\n" % scope)

        # переход к следующему вопросу
        category, question, answers, correct, ball, explanation = next_block(trivia_file)

    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету", scope)
    print("\nВаши рекорды:\n")
    record(name_player, scope)

main()
input("\n\nНажмите Enter, чтобы выйти.")
