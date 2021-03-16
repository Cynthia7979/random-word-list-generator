# Reads complete list from `source` and generates word list files. Refer to `README.md` for usage details.
import csv
import random
import datetime, time
import sys, os


def main():
    source = './sources/托福红宝词汇45天突破版.csv'
    output_directory = './output/'
    number_of_words = 30
    number_of_lists = 1
    csv_mode = True
    if len(sys.argv) > 1:
        source = sys.argv[1]
        output_directory = sys.argv[2]
    if len(sys.argv) >= 4:
        number_of_words = int(sys.argv[3])
    if len(sys.argv) >= 5:
        number_of_lists = int(sys.argv[4])
    _unique_choices = True

    word_list = load_list(source)

    # Check if number of words per list is greater than list length
    if number_of_words > len(word_list):
        print("WARNING: Number of words is larger than the length of the source list. Words will not be unique.")
        _unique_choices = False
    # Check if output directory exists
    if not os.path.exists(output_directory):
        print("WARNING: Output directory doesn't exist. Trying to create the directory...")
        os.makedirs(output_directory)
    # Generate the lists TODO change to generate csv
    time_str = datetime.date.fromtimestamp(time.time()).strftime('%Y%m%d')
    for list_num in range(number_of_lists):
        new_list = generate_list(word_list, number_of_words, _unique_choices)

        if csv_mode:
            # Output parameters. Not supported to change yet.
            per_row = 3

            words = list(new_list.keys())
            with open(os.path.join(output_directory, 'Q List %d-%s.csv' % (list_num+1, time_str)), 'w', encoding='utf-8') \
                    as csvfile:
                writer = csv.writer(csvfile)
                rows = []
                for r in range(0, len(words), 3): rows.append([])
                for i, word in enumerate(words):
                    rows[i//per_row] += ['%d. %s' % (i+1, word), ' ']
                for row in rows:
                    writer.writerow(row)
                # for i in range(0, len(words), 3):
                #     writer.writerow(['%d. %s' % (a+1, word) for a in (i, i+1, i+2) for words in words[i:i+3]])
                # f.write('\n'.join(['%d. %s' % (i+1, word) for i, word in enumerate(new_list.keys())]))
            with open(os.path.join(output_directory, 'A List %d-%s.csv' % (list_num+1, time_str)), 'w', encoding='utf-8') \
                    as csvfile:
                writer = csv.writer(csvfile)
                rows = []
                for r in range(0, len(words)+1, 3): rows.append([])
                for i, (word, meaning) in enumerate(new_list.items()):
                    rows[i//per_row] += ['%d. %s' % (i+1, word), meaning]
                for row in rows:
                    writer.writerow(row)
                # for i in range(0, len(new_list), 3):
                #     f.write(['%d. %s' % (a, word, meaning) for a in (i, i+1, i+2) for word in words[i:i+3] for ])
        else:
            with open(os.path.join(output_directory, 'Q List %d-%s.txt' % (list_num + 1, time_str)), 'w',
                      encoding='gbk') as f:
                f.write('\n'.join(list(new_list.keys())))
            with open(os.path.join(output_directory, 'A List %d-%s.txt' % (list_num + 1, time_str)), 'w',
                      encoding='gbk') as f:
                for word, meaning in new_list.items():
                    f.write('%s \t %s \n' % (word, meaning))


def load_list(word_list_path):
    loaded = {}
    with open(word_list_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            loaded[row['word']] = row['meaning']
    return loaded


def generate_list(word_dict:dict, number_of_words:int, unique=True):
    selected_list = {}
    keys = list(word_dict.keys())
    for i in range(number_of_words):
        new_selected_word = random.choice(keys)
        selected_list[new_selected_word] = word_dict[new_selected_word]
        if unique:
            keys.remove(new_selected_word)
    return selected_list


if __name__ == '__main__':
    main()
