def task_6():
    s = input("Введите строку: ")
    length = len(s)
    if length <= 2:
        print(ord(s[0]))
    elif length < 10:
        mid_index = (length - 1) // 2
        total_ascii = ord(s[0]) + ord(s[mid_index]) + ord(s[-1])
        print(total_ascii)
    else:
        print(ord(s[-1]))
task_6()
