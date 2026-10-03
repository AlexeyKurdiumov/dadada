spisok = str(input())
spf = spisok.split("student_")
lst_res = {}
for i in spf:
    if i != "":
        lst_res[i[:3]] = int(i[3:])
max = max(list(lst_res.values()))
fl = 0
for number in lst_res.items():
    if number[1] == max:
        if fl:
            print(f"-{number[0]}", end="")
        else:
            print(number[0], end="")
            fl = 1