a=[2, 3, 4, 5, 6, 7]
for i in range(len(a)):
    if a[i]!=a[-1] and a[i]<a[i+1]:
        print("возрастание")
    elif a[i]==a[-1] and a[i]>a[i-1]:
        print('возрастание')
    else:
        print("не")
        break