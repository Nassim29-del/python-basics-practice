
"""
Number to Words Converter

Converts an integer between 1 and 100
into its English word representation.
"""

# Words for numbers from 0 to 19
ONES = [
    "", "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

# Words for multiples of ten
TENS = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]


def number_to_words(n):
    """
    Convert a number into its English word representation.

    Args:
        n (int): Number between 1 and 100.

    Returns:
        str: Number written in English words.
    """

    # Handle the special case of 100
    if n == 100:
        return "one hundred"

    # Handle numbers smaller than 20
    if n < 20:
        return ONES[n]

    # Separate the tens and ones digits
    tens, ones = divmod(n, 10)

    # Combine the tens and ones words
    return TENS[tens] + ("-" + ONES[ones] if ones else "")


def main():
    """Get user input and display the number in words."""

    # Ask the user to enter a number
    n = int(input("Enter a number (1-100): "))

    # Check whether the number is within the valid range
    if 1 <= n <= 100:

        # Convert the number into words and display it
        print(number_to_words(n))

    else:
        # Display an error message for invalid numbers
        print("Please enter a number from 1 to 100.")


# Execute the main function when the script runs directly
if __name__ == "__main__":
    main()
