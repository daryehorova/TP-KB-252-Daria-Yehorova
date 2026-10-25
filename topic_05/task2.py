import requests

def get_nbu_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        rates = {}
        for item in data:
            if item["cc"] in ("USD", "EUR", "PLN"):
                rates[item["cc"]] = item["rate"]
        return rates
    except requests.exceptions.RequestException as e:
        print(f"Помилка підключення до API НБУ: {e}")
        return None

def currency_converter():
    print("Конвертер іноземних валют в українську гривню (НБУ)")
    rates = get_nbu_rates()
    if not rates:
        print("Не вдалося отримати курси валют. Перевірте інтернет-з'єднання.")
        return
    
    print("Доступні валюти для конвертації: USD, EUR, PLN")
    print("Для виходу введіть 'q' на будь-якому етапі.\n")
    
    while True:
        curr_type = input("Введіть тип валюти (USD, EUR, PLN) або 'q' для виходу: ").strip().upper()
        if curr_type == 'Q':
            print("Вихід з конвертера. До побачення!")
            break
            
        if curr_type not in rates:
            print("Помилка: Невідома валюта. Оберіть із USD, EUR, PLN.\n")
            continue
            
        amount_input = input(f"Введіть кількість {curr_type}: ").strip()
        
        if amount_input.lower() == 'q':
            print("Вихід з конвертера. До побачення!")
            break
            
        try:
            amount = float(amount_input)
            if amount < 0:
                print("Кількість не може бути від'ємною.\n")
                continue
            
            rate = rates[curr_type]
            result = amount * rate
            print(f"Результат: {amount} {curr_type} = {result:.2f} UAH (Курс НБУ: {rate})\n")
            
        except ValueError:
            print("Помилка: Будь ласка, введіть числове значення для кількості.\n")

if __name__ == "__main__":
    currency_converter()