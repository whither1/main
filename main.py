def main():
    data = input('Введите фамилию, имя, отчество: ').strip().split()
    print(f'{data[0]} {data[1][0]}.{data[2][0]}.')


if __name__ == '__main__':
    main()
