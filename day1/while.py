symbol = input("Enter a symbol: ")
times = int(input("Enter the number of times you want to print the symbol: "))
i = 0
j = 0

while i <= times:
    while j <= i:
        print(symbol, end='')
        j += 1
    
    print()
    i += 1