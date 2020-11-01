def print_first_line(textfile: str):
    my_file = open(textfile, mode='r')
    print(my_file.readline())
    my_file.close()


def print_fifs_line(textfile: str):
    my_file = open(textfile, mode='r')
    for _ in range(4):
        my_file.readline()
    print(my_file.readline())
    my_file.close()


def print_five_lines(textfile: str):
    my_file = open(textfile, mode='r')
    for _ in range(5):
        print(my_file.readline())
    my_file.close()


def print_from_to_lines(textfile: str, from_line, to_line):
    my_file = open(textfile, mode='r')
    for _ in range(from_line - 1):
        my_file.readline()
    for _ in range(to_line):
        print(my_file.readline())
    my_file.close()


def print_all_lines(textfile: str):
    my_file = open(textfile, mode='r')
    if not my_file.readline():
        print(my_file.readline())


print_all_lines('text_file.txt')



def write_lines_from_keyboard():
    with open("text_file.txt", mode='r') as text_file:
        with open('text_file2.txt', 'w') as new_text_file:
            while True:
                readline
                if not:
                    break
            converter_str.
            new_text_file.write(converter_str)


write_lines_from_keyboard()