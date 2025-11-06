import re
import requests

class PhoneNumberFinder:
    def __init__(self):
        pass

    # Скомпилированное регулярное выражение для поиска номеров телефонов
    PHONE_PATTERN = re.compile(
        r'(?:\+7|8)[\s\-]?\(?[489]\d{2}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}',
        re.VERBOSE
    )

    def __make_list_uniqe(self, arr):
        uniqe_arr = []
        for i in arr:
            if i not in uniqe_arr:
                uniqe_arr.append(i)
        return uniqe_arr
    
    @classmethod
    def find_in_text(cls,text: str):
        phones = cls.PHONE_PATTERN.findall(text)
        result = [cls.normalize_phone(phone) for phone in phones]
        fin = cls.__make_list_uniqe(cls, result)
        return fin

    @classmethod
    def validate_phone(cls,phone: str):
        return bool(cls.PHONE_PATTERN.fullmatch(phone))

    @classmethod
    def normalize_phone(cls, phone:str):
        cleaned = re.sub(r'[^\d+]', '', phone) #Удаляем все нецифровые символы, кроме +

        if cleaned[0] == '8':
                cleaned = '+7' + cleaned[1:]

        return cleaned

    @classmethod
    def find_in_file(cls, path:str):
        try:
            with open(path, 'r') as file:
                content = file.read()
                phones = cls.PHONE_PATTERN.findall(content)
                result = [cls.normalize_phone(phone) for phone in phones]
                fin = cls.__make_list_uniqe(cls, result)
                return fin
                

        except FileNotFoundError:
            print(f"Файл {path} не найден.")
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла {path}: {e}")
            return []

    @classmethod
    def find_in_url(cls, url:str):

        try:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            phones = cls.find_in_text(response.text)
            result = [cls.normalize_phone(phone) for phone in phones]
            fin = cls.__make_list_uniqe(cls, result)
            return fin
        
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к {url}: {e}")
            return []
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            return []
    
p = PhoneNumberFinder.find_in_url("https://parkfreestyle.ru/contacts/")

print(p)

# r = PhoneNumberFinder.find_in_file("test_txt_file.txt")
# print(r)

# text = """
#         Контакты: 
#         основной +7 (912) 345-67-89, 
#         резервный 8(495)123-45-67,
#         и еще один 89123456789.
#         Некорректный: 1234567890.
#         """
# t = PhoneNumberFinder.find_in_text(text)
# print(t)