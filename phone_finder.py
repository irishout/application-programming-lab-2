import re
import requests

class PhoneNumberFinder:

    # Скомпилированное регулярное выражение для поиска номеров телефонов
    PHONE_PATTERN = re.compile(
        r'(?:\+7|8)[\s\-]?\(?[489]\d{2}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}',
        re.VERBOSE
    )

    @classmethod
    def find_in_text(cls,text: str):
        return cls.PHONE_PATTERN.findall(text)

    @classmethod
    def validate_phome(cls,phone: str):
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



        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
            return []

    @classmethod
    def find_in_url(cls, url:str):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        phones = cls.find_in_text(response.text)
        result = [cls.normalize_phone(phone) for phone in phones]

        return result

# p = PhoneNumberFinder.find_in_url("https://www.topnomer.ru/blog/mobilnye-nomera-rossii-kody-po-regionam.html")
# print(p)
# r = PhoneNumberFinder.find_in_file("test_txt_file.txt")
# print(r)