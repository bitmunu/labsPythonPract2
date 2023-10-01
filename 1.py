from math import factorial
print("Введите количество строк")
rows = int(input())

def pascal(rows):

    for i in range(rows):
        s = ''

        for j in range(0, i + 1):
            if i > 5:
                if i % 2 == 0:
                    if j == (i/2):
                        s = s + ' '

            s = s + repr(factorial(i) // (factorial(j) * factorial(i - j)))
            s = s + ' '
            if i > 5:
                if i % 2 == 0:
                    if j == (i/2):
                        s = s + ' '
                else:
                    if j == int(i / 2):
                        s = s + ' '

        print(f"{s}".center(rows*rows))
        print()

pascal(rows)