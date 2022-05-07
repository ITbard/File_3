def len_book(file_name): # измерим длину текстового файла
    with open(file_name) as len_file:
        return len(len_file.readlines())

file_list = []

def list_add(file_name): # создадим список с парами имя-длина файла
    a = []
    list_sort = []
    a.append(file_name)
    a.append(len_book(file_name))
    file_list.append(a)
    # list_sort.append(a)
    # file_list = sorted(list_sort, key=lambda a: a[1])
    return file_list
list_add('1.txt')
list_add('2.txt')
list_add('3.txt')
list_sort = sorted(file_list, key=lambda a: a[1]) # сортируем список
print(file_list)

def text_write(c): # создадим переменную с текстом файла
    with open(c) as file:
        c = file.read()
        return c
text_write('1.txt')
text_write('2.txt')
text_write('3.txt')

def file_write(list_with_titles): # запишем в файл '4.txt' информацию из цикла - название, длина, текст.
    with open('4.txt', "a") as document:
        index0 = 0
        for x in range(len(list_with_titles)):
            document.write(f'{list_with_titles[index0][0]} \n')
            document.write(f'{list_with_titles[index0][1]} \n')
            document.write(f'{text_write(list_with_titles[index0][0])} \n')
            index0 += 1
    return 'file written as 4.txt'
print(file_write(list_sort)) # В какой-то момент я понял, что решать это дз надо через ООП, но я уже был в процессе и отступать было некуда)))
#В классах можно было бы отсортировать объекты(файлы 1,2,3) по атрибуту 'длина файла'. Имя файла и его содержимое также стоило сделать атрибутами класса,
# а еще добавить проверку на вхождение в класс.