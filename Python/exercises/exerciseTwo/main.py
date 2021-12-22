radius = float(input('Enter radius: '))
height = float(input('Enter height: '))

def getBaseArea(radius):
    return float((radius**2) * 3.14)
# Add your logic here

baseArea = getBaseArea(radius)

def getVolume(baseArea, height):
    vol = baseArea * height
    return vol

volume = getVolume(baseArea, height)
print("Volume is " + str(volume))
