symbol = input("Enter a symbol: ")
times = int(input("Enter the number of times you want to print the symbol: "))
row = 0
column = 0

while row < times:
    print(symbol, end='')
    while column < row:
        print(symbol*row, end='')
        column += 1
    print()
    row += 1
