def brackets_compare(str1):
    open_bracket = '('
    close_bracket = ')'
    counter = 0

    for i in str1:
        if i == open_bracket:
            counter += 1
        if i == close_bracket:
            counter -= 1
            if counter < 0:
                break

    if counter == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = '())(()'
    print(brackets_compare(str1))
    str1 = '()()()'
    print(brackets_compare(str1))

