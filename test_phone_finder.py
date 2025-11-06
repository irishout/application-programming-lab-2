import unittest
from phone_finder import PhoneNumberFinder

class PhoneTester(unittest.TestCase):

    def test_valid_phones(self):
        """Тест корректных номеров телефонов"""
        valid_phones = [
            "+7 (912) 345-67-89",
            "8 (912) 345-67-89", 
            "+79123456789",
            "89123456789",
            "+7-912-345-67-89",
            "8-912-345-67-89",
            "+7(912)345-67-89",
            "8(912)345-67-89",
            "+7 912 345 67 89",
            "8 912 345 67 89"
        ]
        
        for phone in valid_phones:
            with self.subTest(phone=phone):
                self.assertTrue(
                    PhoneNumberFinder.validate_phone(phone),
                    f"Номер {phone} должен быть валидным"
                )
    
    def test_invalid_phones(self):
        """Тест некорректных номеров телефонов"""
        invalid_phones = [
            "1234567890",           
            "+1 (912) 345-67-89",
            "7 (912) 345-67-89",    
            "+7 (812) 345-67-8",    
            "+7 (812) 345-67-890",  
            "+7 (012) 345-67-89",   
            "телефон",              
            ""                      
        ]
        
        for phone in invalid_phones:
            with self.subTest(phone=phone):
                self.assertFalse(
                    PhoneNumberFinder.validate_phone(phone),
                    f"Номер {phone} должен быть невалидным"
                )

    def test_phones_in_text(self):
        text = """
        Контакты: 
        основной +7 (912) 345-67-89, 
        резервный 8(495)123-45-67,
        и еще один 89123456789.
        Некорректный: 1234567890.
        """

        found_phones = PhoneNumberFinder.find_in_text(text)
        expected_phones = ["+79123456789", "+74951234567"]

        self.assertEqual(len(found_phones), len(expected_phones))
        for expected in expected_phones:
            self.assertIn(expected, found_phones)
        
    def test_normalize_phone(self):
        """Тест нормализации номеров телефонов"""
        test_cases = [
            ("+7 (912) 345-67-89", "+79123456789"),
            ("8 (912) 345-67-89", "+79123456789"),
            ("89123456789", "+79123456789"),
            ("+7-912-345-67-89", "+79123456789")
        ]
        
        for original, expected in test_cases:
            with self.subTest(original=original):
                result = PhoneNumberFinder.normalize_phone(original)
                self.assertEqual(result, expected)
    
    def test_empty_text(self):
        """Тест поиска в пустом тексте"""
        result = PhoneNumberFinder.find_in_text("")
        self.assertEqual(result, [])
    
    def test_text_without_phones(self):
        """Тест поиска в тексте без номеров"""
        text = "Это текст без телефонных номеров, только слова и цифры 12345."
        result = PhoneNumberFinder.find_in_text(text)
        self.assertEqual(result, [])

    def test_url(self):
        """Тест поиска номеров через url"""

        expected_numper = ['+74959664120', '+78282675144']
        result = PhoneNumberFinder.find_in_url("https://parkfreestyle.ru/contacts/")
        self.assertEqual(result, expected_numper, "Неверно найден номер через url")
