positiveInt = int(input("Positive Integer : "))
for i in range(positiveInt):
    for j in range(i + 1):
        print(f"{positiveInt - j}", end="")
    print()
for i in range(positiveInt):
    for j in range(positiveInt-(i + 1)):
        print(f"{positiveInt - j}", end="")
    print()
