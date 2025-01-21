def main():

    my_dict = {'Vasia':1968, 'Kolia':1970, 'Sasha':1980}
    print(my_dict)
    print(my_dict['Vasia'])
    print(my_dict.get('Kostia', 'Такого ключа нет'))
    my_dict.update({'Sergey':1990, 'Yuriy':1995})
    a = my_dict.pop('Sasha')
    print(a)
    print(my_dict)

    my_set = {1, 2, 3, 1, 2, 3, True, "string"}
    print(my_set)
    my_set.update([4,5])
    my_set.discard(1)
    print(my_set)
if __name__ == '__main__':
    main()

