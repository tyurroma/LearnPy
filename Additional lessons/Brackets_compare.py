def brackets_compare(str1):
    open_bracket = '('
    close_bracket = ')'
    k1 = 0
    k2 = 0
    
    for i in str1:
        if open_bracket == i:
            k1 += 1
        if close_bracket == i:
            k2 += 1
    print(k1)
    print(k2)        
    if k1 == k2:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = '()())'
    print(brackets_compare(str1))