def brackets_compare(str1):
    open_bracket = '('
    close_bracket = ')'
    k1 = 0
    k2 = 0
    
    for i in str1:
        if i == open_bracket:
            k1 += 1
        if i == close_bracket:
            k2 += 1
            if str1[0] == close_bracket:
                return False
                continue
    if k1 == k2:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = '()()'
    print(brackets_compare(str1))
    str1 = ')()('
    print(brackets_compare(str1))
    str1 = ')(()())'
    print(brackets_compare(str1))
    str1 = '((())()('
    print(brackets_compare(str1))

