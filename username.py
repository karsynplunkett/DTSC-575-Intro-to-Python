import sys

def username(first, last):
    length1= int(len(first))
    length2 =int(len(last))
    sumtot=length1+length2
    name = first[0] + last[-7:-1] +last[-1] +str(sumtot)
    name=name.lower()
    print(f'Your username is {name}')

username(sys.argv[1],sys.argv[2])
