a=input("день/ночь")
b = float(input('время в 12-часовом формате'))
if a=='день':
    print(b)
if a=='ночь':
    b=b+12
    print(b)
