import multiprocessing
import time
import os
from docx import Document

def find_symbols_in_part(filename, target_symbols, start, end, result_queue):
    start_time = time.time()

    try:
        doc = Document(filename)
        content = ''.join([paragraph.text for paragraph in doc.paragraphs])
        content_part = content[start:end]
        count = sum(content_part.count(symbol) for symbol in target_symbols)
        result_queue.put(count)
    except Exception as e:
        print(f"Ошибка при открытии файла {filename}: {e}")
        result_queue.put(0)

    end_time = time.time()
    elapsed_time = end_time - start_time
    result_queue.put(elapsed_time)

def main():
    file_path = "/home/anton/Загрузки/VIM.docx"
    target_symbols = ['a']  # Замените символы на те, которые вам нужны

    # Получаем размер файла
    file_size = os.path.getsize(file_path)

    # Разделяем размер файла пополам
    half_size = file_size // 2

    # Создаем очередь для передачи результатов обратно в главный процесс
    result_queue = multiprocessing.Queue()

    # Создаем два процесса, каждый обрабатывает свою половину файла
    process1 = multiprocessing.Process(target=find_symbols_in_part, args=(file_path, target_symbols, 0, half_size, result_queue))
    process2 = multiprocessing.Process(target=find_symbols_in_part, args=(file_path, target_symbols, half_size, file_size, result_queue))

    # Запускаем процессы
    process1.start()
    process2.start()

    # Ожидаем завершения процессов
    process1.join()
    process2.join()

    # Получаем результаты из очереди
    count1 = result_queue.get()
    elapsed_time1 = result_queue.get()
    count2 = result_queue.get()
    elapsed_time2 = result_queue.get()

    # Выводим результаты
    print(f"Количество найденных символов в части файла 1: {count1}")
    print(f"Время выполнения для части файла 1: {elapsed_time1:.4f} сек.")

    print(f"Количество найденных символов в части файла 2: {count2}")
    print(f"Время выполнения для части файла 2: {elapsed_time2:.4f} сек.")

if __name__ == "__main__":
    main()
