n = 8
def Serp(n):
    b = n - 1

    while b >= 0:
        i = 0

        while i < b:
            print(" ", end="")
            i = i + 1

        a = 0

        while a + b < n:

            if (a & b) != 0:
                print(" ", end=" ")
            else:
                print("* ", end="")

            a = a + 1

        print()
        b = b - 1

Serp(n)