num = int(input('Введите число:'))
if num>=1:
    for i in range (1,num+1):
        print(i)
else:
    for i in range (-1,num-1,-1):
        print(i)
