import os
import re

def main():
    print_all_files()

def print_all_files():
    try:
        list_yes = ['y', 'Y', 'yes', 'Yes', 'YES']
        list_no = ['n', 'N', 'no', 'No', 'NO']
        files = [f for f in os.listdir(".") if re.match(r'[a-z]+.*\.lst', f)]
        if len(files) == 0:
            choose_file()
        else:
            print(files)
            choice = input('Create new file? ')
            if choice in list_yes:
                choose_file()
            elif choice in list_no:
                print('Shutdown...')
    except KeyboardInterrupt:
        print('\nShutdown...')

def choose_file():
    file = input('Choose file: ')
    if os.path.isfile(file+'.lst') == False:
        print('-- no items are in the list --')
        choice = input('[A]dd [Q]uit [a]: ')
        if choice == 'a' or choice == 'A':
            create_file(file)
        elif choice == 'q' or choice == 'Q':
            print('Shutdown...')
        else:
            print('Error! Invalid command, please try again')
            choose_file()
    else:
        print('Good')

def create_file(file):
    try:
        while True:
            choice = input('[A]dd [D]elete [Q]uit [a]: ')
            if choice in 'Aa':
                write_to_file(file)
            elif choice in 'dD':
                delete = input('Delete item: ')
                remove_from_file(file, delete)
            elif choice in 'qQ':
                print('Shutdown...')
                break
            else:
                print('ERROR: invalid choice--enter one of "AaDdQq"')
    except KeyboardInterrupt:
        print('\nShutdown...')

def write_to_file(file):
    with open(file+'.lst', 'a') as f:
        item = input('Add item: ')
        f.write(item+'\n')

def remove_from_file(file, text):
    tmp = []
    f = open(file+'.lst', 'r')
    d = f.readlines()
    for line in d:
        line = line.rsplit()
        tmp.append(line)
    f.close()

    #print(tmp)

    n = open(file+'.lst', 'r+')
    for lines in tmp:
        print(lines)
        for a in lines:
            if text in a:
                print(text)
                lines.remove(text)
                print(lines)
                n.seek(0)
                n.truncate()
                n.write(a)
    n.close()
main()