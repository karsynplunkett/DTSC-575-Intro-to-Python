import sys

def change(dol, q, dime, n, p):
    money = round(int(dol)+int(q)*0.25+int(dime)*0.1+int(n)*0.05+int(p)*0.01,2)
    print(f'The total value of your change is ${money}')

change(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
