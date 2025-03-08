# Claire Francis, March 7th, 2025
# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math

def get_distance(coord1, coord2):
    distance = math.sqrt(pow(coord1[0] - coord2[0],2)+pow(coord1[1] - coord2[1],2)+pow(coord1[2] - coord2[2],2))
    return distance



#get_distance()



def main():

    coordinate1 = ()
    coordinate2 = ()

    try:
        num1 = float(input("Enter number for coordinate 1, x: "))
        num2 = float(input("Enter number for coordinate 1, y: "))
        num3 = float(input("Enter number for coordinate 1, z: "))

        num4 = float(input("Enter number for coordinate 2, x: "))
        num5 = float(input("Enter number for coordinate 2, y: "))
        num6 = float(input("Enter number for coordinate 2, z: "))

        coordinate1 = (num1, num2, num3)
        coordinate2 = (num4, num5, num6)
        dist = get_distance(coordinate1, coordinate2)
        #print (coordinate1)
        #print (coordinate2)
        print("distance between", coordinate1, "and", coordinate2, "is", dist)
    except ValueError:
        print("must enter float as input")




if __name__ == '__main__':
    main()
