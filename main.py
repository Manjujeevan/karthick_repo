row = int(input("Enter a Row :"))
column = int(input("Enter a Coulmn :"))
symbol = input("Enter a Symbol :")


for x in range(row):
    for y in range(column):
        print(symbol,end='')

    print()
