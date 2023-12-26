a=str(input("Введите слово"))
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        print("True")
    else:
        print("")
        