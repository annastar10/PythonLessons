import random as rnd
import string


def create_rnd_string(min_limit, max_limit):
    chars = string.ascii_letters
    str_range = rnd.randint(min_limit, max_limit)
    return ''.join(rnd.choice(chars) for i in range(str_range))


def create_email(name, domain, rnd_num, rnd_string):
    return name + "." + str(rnd_num) + "@" + rnd_string + "." + domain


def get_rnd_num_and_commas_list(num_min, num_max, length):
    nums = [" " + str(rnd.randint(num_min, num_max)) for i in range(length)]
    punctuation = [rnd.choice("," + "\n") for v in range(length)]
    rnd_punct_and_nums = [rnd.choice(nums + punctuation) for i in range(length)]
    return [rnd.choice(punctuation + rnd_punct_and_nums) for i in range(length)]


def split_string_to_words(rnd_string, min_word_lim, max_word_lim):
    split_list = []
    str_length = len(rnd_string)
    i = 0
    while i < str_length:
        r = rnd.randint(min_word_lim, max_word_lim)
        split_list.append(rnd_string[i:i + r])
        i = i + r
    return split_list


def convert_string_to_text(rnd_string_list, rnd_punct, coefficient=0.3):
    str_len = len(rnd_string_list)
    if str_len < 3:
        return rnd_string_list
    end_word = rnd_string_list.pop(str_len - 1)+"."
    start_word = rnd_string_list.pop(0).capitalize()
    new_list = []
    for i in rnd_string_list:
        if rnd.random() < coefficient:
            p = str(rnd.choice(rnd_punct)) + " "
        else:
            p = " "
        new_list.append(i + p)
    return start_word + ''.join(new_list) + end_word


'''
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
'''
surname = ["Uranus", "Jupitor", "Mars", "Sun", "Pluto", "Saturn", "Mercury", "Earth"]
domains = ['cloud', 'city', 'ir', 'cn', 'br', 'web', 'ua', 'net', 'co.uk', 'edu',
           'eg', 'club', 'dm', 'lv', 'co', 'ru', 'tv', 'in', 'int', 'org', 'com']

# zadanie  1

min_length = 5
max_length = 7
name = rnd.choice(surname)
domain = rnd.choice(domains)
rnd_num = rnd.randint(100, 999)
rnd_string = create_rnd_string(min_length, max_length).lower()
email = create_email(name=name, rnd_num=rnd_num, domain=domain, rnd_string=rnd_string)
print("\n\n", "Задание №1: \n", email, "\n\n")


# zadanie 2

rnd_string = create_rnd_string(100, 500)
print("Задание №2: \n", rnd_string, "\n\n")

# zadanie 3
num_min = 0
num_max = 100
word_min_len = 1
word_max_len = 10
string_to_words = split_string_to_words(rnd_string.lower(), word_min_len, word_max_len)
# следующее не обязательно, можно и пропустить и инжектировать в список отдельныой функцией
punctuations_and_nums = get_rnd_num_and_commas_list(num_min, num_max, len(string_to_words))
random_text = convert_string_to_text(string_to_words, punctuations_and_nums)

print("Задание №3: \n", random_text, "\n\n")

