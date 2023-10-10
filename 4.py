a=float(input("введите число"))
def dislike_6(a):
    if isinstance(a,(int, float)) and a==6:
        print("Только не 6!")
    else:
        print("True")
dislike_6(a)