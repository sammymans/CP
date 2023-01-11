n = input()
a = input()

transform = {
             "0":"",
             "1":"",
             "2":"2",
             "3":"3",
             "4":"322",
             "5":"5",
             "6":"53",
             "7":"7",
             "8":"7222",
             "9":"7332",
            }

result = ""
for c in a:
    result += transform[c]

result = sorted(result, reverse=True)
print(int("".join(result)))
