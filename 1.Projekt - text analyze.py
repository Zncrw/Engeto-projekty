"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Korvas
email: korvasz@seznam.com
discord: Zdeněk.K#9428
"""
from task_template import TEXTS   # import zadaneho textu
username = input('Zadejte login: \n').lower()
registered_usernames = ['bob', 'ann', 'mike', 'liz']
registered_passwords = ['123', 'pass123', 'password123', 'pass123']
LINE = '---------------------------------------'
if username in registered_usernames:
    log_plus_pass = dict(zip(registered_usernames, registered_passwords))
    password = input('Zadejte heslo: \n').lower()
    if log_plus_pass.get(username) == password:
        print(LINE)
        print(f'Welcome to the app, {username.capitalize()}')
        print('We have 3 texts to be analyzed.')
        print(LINE)
        select = int(input('Enter a number btw. 1 and 3 to select: '))
        print(LINE)

        def analyze(text):
            '''
            function for text analyze
            :param text: text imported from task_template.py and user can choose text to analyze
            :return: statistics of chosen text
            '''
            words = text.split()
            num_words = len(words)
            title_words = len([word for word in words if word.istitle()])
            upper_words = len([word for word in words if word.isupper()])
            low_words = len([word for word in words if word.islower()])
            numeric_strings = [word for word in words if word.isnumeric()]
            num_numeric_strings = len(numeric_strings)
            numbers_sum = sum(int(word) for word in numeric_strings)
            print(f'There are {num_words} words in the selected text.')
            print(f'There are {title_words} titlecase words.')
            print(f'There are {upper_words} uppercase words.')
            print(f'There are {low_words} lowercase words.')
            print(f'There are {num_numeric_strings} numeric strings.')
            print(f'The sum of all the numbers {numbers_sum}')


        analyze(TEXTS[select - 1])


        def create_ladder_graph(data_2):
            '''
            function for text analyze of lenght and occurence of words in chosen text, result showed as ladder graph.
            :param data_2: choosen text from import and input user
            :return:ladder graph of text analyze in format: Lenght,Occurences,Number.
            '''
            max_length = max(data_2.keys())
            for length in range(1, max_length + 1):
                if length in data_2:
                    star = '*' * data_2[length]
                    print(f'{length}|{star.rjust(15)}|{data_2[length]}')
                else:
                    print(f'{length}|{' ' * 15}|0')


        words_2 = TEXTS[select - 1].split()
        data_2 = {}
        for word_2 in words_2:
            length = len(word_2)
            if length in data_2:
                data_2[length] += 1
            else:
                data_2[length] = 1
        print(LINE)
        print("LEN|  OCCURRENCES  |NR")
        print(LINE)
        create_ladder_graph(data_2)

    else:
        print('Wrong password')
else:
    print('unregistered user, terminating the program..')



