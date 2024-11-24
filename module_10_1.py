import threading
import time
import datetime

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(0, word_count):
        time.sleep(0.1)
        file.write(f'Слово №{i+1}')
    file.close()
    print(f'Завершилась запись в файл {file_name}')

start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = datetime.datetime.now()
print(f"Работа потоков: {end - start}")
threads = [
    threading.Thread(target=write_words, args=(10, "example5.txt")),
    threading.Thread(target=write_words, args=(30, "example6.txt")),
    threading.Thread(target=write_words, args=(200, "example7.txt")),
    threading.Thread(target=write_words, args=(100, "example8.txt"))
]

start = datetime.datetime.now()
for thread in threads:
    thread.start()


for thread in threads:
    thread.join()
end = datetime.datetime.now()
print(f"Работа потоков: {end - start}")