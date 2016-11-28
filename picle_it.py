# Законсервируем
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки

import pickle, shelve
print("Консервация списков.")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондбэль"]
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nРасконсервация списков.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
bootle = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(bootle)
print(brand)
f.close()

print("\nПомещение списков на полку.")
s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпродукт", "Чумак", "Бондбэль"]
s.sync()
print("/nИзвлечени списков из файла полки:")
print("торговые марки - ", s["brand"])
print("формы - ", s["brand"])
print("виды овощей - ", s["variety"])
s.close()
input("\n\nНажмите Enter, чтобы выйти.")
