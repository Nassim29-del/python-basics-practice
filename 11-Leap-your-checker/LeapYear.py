
# Function to check whether a given year is a leap year
def is_leap_year(year):

    # A year is a leap year if:
    # 1. It is divisible by 4 AND not divisible by 100
    # OR
    # 2. It is divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Main function: gets the year from the user and displays the result
def main():

    # Ask the user to enter a year
    # Convert the input from a string to an integer
    year = int(input("Enter a year: "))

    # Check whether the year is a leap year
    # Display the appropriate message using a conditional expression
    print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}.")


# Check if the file is being executed directly
if __name__ == "__main__":

    # Call the main function to start the program
    main()
