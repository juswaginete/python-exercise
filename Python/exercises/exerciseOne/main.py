# Add your logic here
length = input('Enter length: ')
width = input('Enter width: ')

def getPerimeter(length, width):
    return((2*int(length)) + (2*int(width)))

print("Perimeter is " + str(getPerimeter(length, width)))