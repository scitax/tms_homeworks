import argparse
import os


if __name__ == '__main__':
    current_file_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_file_path)

    # parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--folder-name', required=True)
    parser.add_argument('-fi', '--file-name', required=True)
    args = parser.parse_args()

    # getting new dir and file pass and new file name
    new_dir_path = f'{current_dir_path}/{args.folder_name}'
    new_file_name = args.file_name
    new_file_path = f'{new_dir_path}/{new_file_name}'

    os.mkdir(new_dir_path)

    with open(new_file_path, 'w') as new_file:
        if new_file_name[-3:] == '.py':
            message_to_write = "def main():\n\tpass\n\n\nif __name__ == '__main__':\n\tmain()"
            new_file.write(message_to_write)

