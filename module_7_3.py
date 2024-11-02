import io
from importlib.metadata import files


class WordsFinder:
    def __init__(self, *files):
        self.file_names = [*files]


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                string = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    string = string.replace(char, '')
                string = string.split()
                all_words.update({file_name: string})
        return all_words


    def find(self, f_word):
        word_pos = {}
        word_count = 0
        for file, word_list in self.get_all_words().items():
            for word in word_list:
                word_count += 1
                if word == f_word.lower():
                    word_pos.update({file: word_count})
                    return word_pos



    def count(self, c_word):
        word_count = 0
        for file, word_list in self.get_all_words().items():
            for word in word_list:
                if word == c_word.lower():
                    word_count += 1
        return {file: word_count}


test1 = WordsFinder('test_file.txt')
print(test1.get_all_words())
print(test1.find('TEXT'))
print(test1.count('text'))
