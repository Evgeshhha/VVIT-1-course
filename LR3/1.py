def printfile(type = 0):
    with open('C:\\Users\\Evgen\Desktop\\ВВИТ\\ПР3\\example.txt', 'r') as file:
        if type == 0:
            #Чтение всего файла
            content = file.read()
            print(content)
        else:
            #Построчное чтение
            for line in file:
                print(line.strip())

printfile()