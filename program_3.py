# Claire Francis, March 7th, 2025
# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    all_entered_values = []
    values_per_state = [0,"a",0]


    again = 'y'
    while again == 'y':
        try:
            year = int(input('Enter a year: '))
            state = str(input("Enter the state: "))
            population = int(input("Enter the population of the state: "))

            values_per_state[0] = year
            values_per_state[1] = state
            values_per_state[2] = population

            all_entered_values.append((year, state, population))

            print('Do you want to add another year and state?')
            again = input('y = yes, anything else = no: ')
            print(again)

            print(all_entered_values)

        except ValueError:
            print("year and population must be integers")
            break

    # Now have the user enter a year.
    year_entered = int(input("Enter a year of interest: "))

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(all_entered_values, year_entered)


def sum_population_for_year(values, year_to_sum):
    pop_total = 0

    try:
        #print("length of all_entered_values is", len(values))

        # Loop through and sum the populations for the appropriate year.
        # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
        # or 3,421,988 if they enterd 2011 for the year to sum.

        for i in range(0,len(values)):
            var = values[i-1]
            #print("index",i)

            if year_to_sum == var[0]:
            #    print("valid year data", var)
                pop_total+=var[2]
            #else:
            #    print("year does not match")

        # print the totalled population
        print("The total population for year", year_to_sum, "is",pop_total)

    except ValueError:
        print("year must be an integer")



if __name__ == '__main__':
    main()








