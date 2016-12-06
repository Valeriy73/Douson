# -*- encoding: utf-8 -*-

class TVset(object):
	"""Программ пульт телевизора: каналы и громкость"""
	def __init__(self, name, chenal=12, volume=12):
		self.__name = name
		self.__chenal = chenal
		self.__volume = volume

	@property
	def name(self):
		return self.__name
	
	@property
	def chenal(self):
		return self.__chenal

	@property
	def volume(self):
		return self.__volume

	@chanel.setter
	def chenal(self, new_chanel):
		if new_chanel < 0:
			print 'Каналы на чинаются с "0"'
		elif new_chanel > 24:
			print 'Мы поддерживаем только 24 канала'
		else:
			self.__chenal = new_chenal

	@volume.setter
	def volume(self, new_volume):
		if new_volume < 0:
			print 'Громкость не может быть меньше нуля'
		elif new_volume > 24:
			print 'Максимальная громкость 24 единицы'
		else:
			self_volume = new_volume

	def change_chenal():
		new_chenal = int(raw_input"Введите номер канала от 0 до 24:")
		self.chenal

def hello():
	print "Ваш телевизор %s имеет следующие настройки:\n" % my_tv.name
	print "Выбран канал: %s\n" % my_tv.chenal
	print "Установлена громкость: %s\n" % my_tv.volume	


def main():
	name_tv = raw_input("Введите название вашего телевизора: ")
	my_tv = TVset(name_tv)

	hello()

	choise = None
	while choise != "0":
		"""
		Какие настройки желаете изменить:
			1- Номер канала
			2 - Уровень громкости
			3 - Оставить без изменений
			0 - Выход
		"""
		choise = raw_input("Ваш выбор: ")
		if choise == "1":
			self.chenal = int(raw_input"Введите номер канала от 0 до 24:")
			hello()
		elif choise == "2":
			self.volume = int(raw_input"Введите уровень громкости от 0 до 24:")
			hello()


main()
raw_input("\n\nНажмите Enter, чтобы выйти.")




