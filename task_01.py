import queue
import random 
import time

queue = queue.Queue()

def generate_request():
    # Створення нової заявки з унікальним номером
    request_id = random.randint(1, 1000)
    print(f"Створено заявку: {request_id}")
    # Додавання заявки до черги
    queue.put(request_id)

def process_request():
    # Якщо черга не порожня
    if not queue.empty():
        # Видалення заявки з черги
        request_id = queue.get()
        # Обробка заявки
        print(f"Обробка заявки: {request_id}")
    else:
        # Виведення повідомлення про порожню чергу
        print("Черга порожня")

#Головний цикл програми:
try:
    while True:
        # Виклик функції для створення нових заявок
        generate_request()
        # Виклик функції для обробки заявок
        process_request()
        # Імітація затримки між операціями
        time.sleep(1)
except KeyboardInterrupt:
    print("Вихід з програми.")  # Для виходу натисніть Ctrl + C


