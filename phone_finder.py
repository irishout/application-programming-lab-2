import re
import requests

class PhoneNumberFinder:
    
    # Скомпилированное регулярное выражение для поиска номеров телефонов
    PHONE_PATTERN = re.compile(
        r'(?:\+7|8)[\s\-]?\(?[489]\d{2}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}',
        re.VERBOSE
    )
 