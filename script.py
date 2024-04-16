import pandas as pd
from PyDictionary import PyDictionary
import numpy as np

class MyDict:
    def __init__(self):
        self.dictionary = PyDictionary()
        self.load_words()

    def load_words(self):
        try:
            self.database_df = pd.read_csv('myDict/dictionary.csv')
            self.database_set = set(self.database_df['kata'])
        except FileNotFoundError:
            self.database_df = pd.DataFrame(columns=['kata'])
            self.database_set = set()

    def save_word(self, word):
        self.database_set.add(word)
        self.database_df = pd.DataFrame(list(self.database_set), columns=['kata'])
        self.database_df.to_csv('myDict/dictionary.csv', index=False)
        print("------------------------")
        print('Database has been saved!')

    def reset_database(self):
        self.database_set.clear()
        self.database_df = pd.DataFrame(columns=['kata'])
        self.database_df.to_csv('myDict/dictionary.csv', index=False)
        print('Database has been reset!')

    def fetch_definition(self):
        word = input('Enter word: ').lower()
        try:
            meanings = self.dictionary.meaning(word)
            if meanings:
                for theword, definitions in meanings.items():
                    print("=====================")
                    print(f"Type: {theword}")
                    print("---------------------")
                    print('Definitions:')
                    for definition in definitions:
                        print(definition)
                    print("=====================")
                if input('Save word? (y/n): ').lower() == 'y':
                    self.save_word(word)
            else:
                print(f"No definition found for the word '{word}'")
        except Exception as e:
            print(f"An error occurred while fetching definitions: {e}")

    def translate_word(self):
        word = input('Enter word: ').lower()
        try:
            translation = self.dictionary.translate(word, 'id')
            if translation:
                print("---------------------")
                print(translation)
                print("=====================")
                if input('Save word? (y/n): ').lower() == 'y':
                    self.save_word(word)
            else:
                print(f"No translation found for the word '{word}'")
        except Exception as e:
            print(f"An error occurred while translating: {e}")

    def random_memorization(self):
        if not self.database_set:
            print("No words available in database.")
            return
        random_word = np.random.choice(list(self.database_set))
        print(f"Random word selected: {random_word}")

    def main_menu(self):
        while True:
            print()            
            print('º----My Dictionary----º')            
            print('=======================')
            print('MAIN MENU:')
            print('1. Search Definitions')
            print('2. Translate')
            print('3. Save Word')
            print('4. Check Word Database')
            print('5. Random Memorization')
            print('6. Reset Database')
            print('7. Exit')
            print('=======================')
            try:
                choice = int(input('Select a menu option: '))
                if choice == 1:
                    self.fetch_definition()
                elif choice == 2:
                    self.translate_word()
                elif choice == 3:
                    word = input('Enter word to save: ').lower()
                    self.save_word(word)
                elif choice == 4:
                    print("-----------------------")
                    print("Berikut adalah Database Kata:")
                    temp_df = pd.DataFrame(self.database_set, columns=['kata'])
                    temp_df.index += 1  # Mengatur indeks dimulai dari 1
                    print(pd.concat([temp_df.head(), temp_df.tail()]))
                    print()
                    print(f"Jumlah kata: {len(temp_df)}")
                    print('=======================')
                elif choice == 5:
                    print("-----------------------")
                    self.random_memorization()
                    print("=======================")
                elif choice == 6:
                    self.reset_database()
                elif choice == 7:
                    break
                else:
                    print('Please select a valid option (1-7).')
            except ValueError:
                print('Invalid input, please enter a number.')
            except Exception as e:
                print(f"An error occurred: {e}")