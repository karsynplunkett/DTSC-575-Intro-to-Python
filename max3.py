import sys

def max3(x,y,z):
    list1=[int(x),int(y),int(z)]
    maximum= max(list1)
    print(maximum)

max3(sys.argv[1],sys.argv[2],sys.argv[3])

