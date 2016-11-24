# -*- coding: utf8 -*-

# Крестики-нолики
# Компьютер играет в Крестики-нолики против пользователя
# глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
    """
    Добропожаловать на ринг созтязаний всех времен.
    Схватка за доской игры "Крестики-нолики".
    Чтоб сделать ход, введи число от 0 до 8. Числа однозначно 
    соответствуют полям доски - так, как показано ниже:
     0 | 1 | 2 
     ----------
     3 | 4 | 5 
     ----------
     6 | 7 | 8 
     Приготовся к бою, жалкий человечишка. Вот-вот начнется решающее сражение. \n """ 
    )

def ask_yes_no(question):
    """ Задает вопрос с ответом 'да'' или 'нет'"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()

    return response

def ask_number(question, low, high):
	""" Просит ввести число из диапазона"""
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

def pieces():
	""" Определяет принадлежность первого хода. """
	go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y/n): ")
	if go_first == "y":
		print("\nНу что ж, дою тебе фору: играй крестиками.")
		human = X
		computer = O
	else:
		print("\nТвоя удаль тебя погубит... Буду начинать я.")
		computer = X
		human = O
return computer, human

def new_board():
	""" Создает новую игровую доску."""
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
return board

def display_board(board):
	""" Отображает игровую доску на экране."""
	print("\n\t{}|{}|{}".format(board[0], board[1], board[2]))
	print("\t--------")
	print("\t{}|{}|{}".format(board[3], board[4], board[5]))
	print("\t--------")
	print("\t{}|{}|{}\n".format(board[6], board[7], board[8]))

def legal_moves(board):
	""" Создает список доступных ходов."""
	moves = []
	for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
        	moves.append(square)
return moves

def winner(board):
	""" Определяет победителя в игре."""
	WAYS_TO_WIN ((0, 1, 2),
				 (3, 4, 5),
				 (6, 7, 8),
				 (0, 3, 6),
				 (1, 4, 7),
				 (2, 5, 8),
				 (0, 4, 8),
				 (2, 4, 6))
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
return None


