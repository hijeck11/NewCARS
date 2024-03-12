import threading
import time
import os
from docx import Document

def find_symbols_in_part(filename, target_symbols, start, end):
    start_time = time.time()

    try:
        doc = Document(filename)
        content = ''.join([paragraph.text for paragraph in doc.paragraphs])
        content_part = content[start:end]
        count = sum(content_part.count(symbol) for symbol in target_symbols)
        print(f"Количество найденных символов в части файла: {count}")
    except Exception as e:
        print(f"Ошибка при открытии файла {filename}: {e}")
        return

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.4f} сек.")

def main():
    file_path = "/home/anton/Загрузки/VIM.docx"
    target_symbols = ['a']  # Замените символы на те, которые вам нужны

    # Получаем размер файла
    file_size = os.path.getsize(file_path)

    # Разделяем размер файла пополам
    half_size = file_size // 2

    # Создаем два потока, каждый обрабатывает свою половину файла
    thread1 = threading.Thread(target=find_symbols_in_part, args=(file_path, target_symbols, 0, half_size))
    thread2 = threading.Thread(target=find_symbols_in_part, args=(file_path, target_symbols, half_size, file_size))

    # Запускаем потоки
    thread1.start()
    thread2.start()

    # Ожидаем завершения потоков
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
