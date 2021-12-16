length = float(input('Enter length: '))
width = float(input('Enter width: '))

def getPerimeter(length, width):
    return((2*float(length)) + (2*float(width)))

def getArea(length, width):
    area = (length * width)
    return area

print("Perimeter is " + str(getPerimeter(length, width)))
print ("Area is " + str(getArea(length, width)))
