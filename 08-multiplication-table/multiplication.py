
# Function to generate a multiplication table of size n
def multiplication_table(n):

    # Loop through each row, starting from 1 up to n
    for row in range(1, n + 1):

        # Loop through each column, starting from 1 up to n
        for col in range(1, n + 1):

            # Multiply the current row by the current column
            # :4d reserves 4 spaces for each result to align the table
            # end="" keeps the results on the same line
            print(f"{row * col:4d}", end="")

        # Move to the next line after printing all columns
        print()


# Check if the file is being executed directly
if __name__ == "__main__":

    # Ask the user to enter the desired multiplication table size
    # Convert the input into an integer
    multiplication_table(int(input("Table size: ")))
