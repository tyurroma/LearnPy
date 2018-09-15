
def length_of_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            return len(content)
    except FileNotFoundError:
        print("File doesn't exist!")

def words_in_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            content = content.split()
            return len(content)
    except FileNotFoundError:
        print("File doesn't exist!")

def replace_dots_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            content = content.replace('.', '!')  
        with open('referat2.txt', 'w', encoding='utf-8') as myfile:
            myfile.write(content)
        print('Success!')
    except FileNotFoundError:
        print("File doesn't exist!")


if __name__ == '__main__':
    test1 = length_of_file_content('referat.txt')
    print(test1)
    test2 = words_in_file_content('referat.txt')
    print(test2)
    test3 = replace_dots_file_content('referat.txt')