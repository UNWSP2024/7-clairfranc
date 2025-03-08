# Claire Francis, March 6th, 2025, Week7_program_1.py
# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall,
# and the months with the highest and lowest amounts.

import statistics
def main():
    ######################
    m=0
    rainfall = []
    total_rain = 0


    for m in range(1,13):                 # m for months
        print("How many inches of rainfall per month ", m)
        rain = float(input("Inches of rainfall: "))
        rainfall.append(rain)
    #print(rainfall)
    total_rain = sum(rainfall)
    average_rain = total_rain/len(rainfall)


    print("total inches of rainfall for the year: ", total_rain, "inches")
    print("average rainfall per month for entire period:", total_rain / 12, "inches")
    print('The lowest value of rain per month is', min(rainfall), "inches")
    print('The highest value of rain per month is', max(rainfall), "inches")

if __name__ == '__main__':
    main()
