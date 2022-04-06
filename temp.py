import sys

def temp(tem):
    far = float(tem)*1.8+32
    print('The temperature is {:.2f} degrees Fahrenheit.'.format(far))

temp(sys.argv[1])
    
