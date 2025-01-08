try:
    with open ('example.txt', 'r', encoding='UTF-8') as file:
        print('Построчное - 0')
        x=input()
        if x==0:
            for line in file:
                print(line)
        else:
            content = file.read()
            print(content)
except FileNotFoundError:
    print('Файл не найден')
