def main():
    data = input().strip().split('+')
    summary = 0
    for num in data:
        summary += int(num)
    print(summary)


if __name__ == '__main__':
    main()
