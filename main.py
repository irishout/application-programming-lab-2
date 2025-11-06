from phone_finder import PhoneNumberFinder

finder = PhoneNumberFinder()

print("=== Поиск российских номеров телефонов ===\n")

#Проверка номера на валидность (1)
phone = input("Введите номер для проверки валидности (Enter для пропуска)")
if phone:
    if finder.validate_phone(phone):
        print(f"Номер валиден {finder.normalize_phone(phone)}")
    else:
        print("Номер не валиден")

#Проверка номеров в тексте (2)
text = input("Введите текст для проверки номеров (Enter для пропуска)")
if text:
    text_result = finder.find_in_text(text)
    print(f"Найдено номеров {len(text_result)}")
    print(text_result)

#Поиск номеров по url (3)
url = input("Введите ссылку для поиска номеров (Enter для пропуска)")
if url:
    url_result = finder.find_in_url(url)
    print(f"Найдено номеров {len(url_result)}")
    print(url_result)

#Поиск новеров в файле (4)
path = input("Введите название файла (Enter для пропуска)")
if path:
    file_result = finder.find_in_file(path)
    print(f"Найдено номеров {len(file_result)}")
    print(file_result)


