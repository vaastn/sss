counter1, counter2 = 0, 0 
while (counter1 != 3 or counter2 != 3): 
    print("Первый игрок: 1-камень, 2 - ножницы, 3 - бумага")
    a = int(input())
    print("Второй игрок: 1-камень, 2 - ножницы, 3 - бумага") 
    b = int(input())
    if a==b:
        print("Ничья")
    elif a==1 and b==3:
        print("Победил второй игрок")
        counter2+=1
    elif a==1 and b==2:
       print("Победил первый игрок")
       counter1+=1
    elif a==2 and b==1:
       print("Победил второй игрок")
       counter2+=1
    elif a==2 and b==3:
       print("Победил первый игрок")
       counter1+=1
    elif a==3 and b==1:
       print("Победил первый игрок")
       counter1+=1
    elif a==3 and b==2:
       print("Победил второй игрок")
       counter2+=1
print("Победил " +("первый" if counter1>counter2 else "второй") + " игрок") 