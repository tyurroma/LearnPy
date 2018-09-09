def compare(str1, str2):
    if str1.isdigit() == True and str2.isdigit() == True:
        print(0)
    if str1 == str2:
        print(1)
    else:
        if len(str1) > len(str2):
            print(2)
        elif str2 == 'learn':
            print(3)


compare('str1', 'str1')
compare('ghdbtnsadsdf', 'str23sd')
compare('1', '2')
compare('learn', 'learn')