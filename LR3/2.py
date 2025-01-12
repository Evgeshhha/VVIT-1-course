n_file = 'C:\\Users\\Evgen\Desktop\\ВВИТ\\ПР3\\user_input.txt'
content = ''
try:
    with open(n_file, 'r') as file:
        content = file.read() + '\n'
except FileNotFoundError:
    None
text = input("Введите текст для файла: ")
f = open(n_file,'w')  
f.write(content + text)