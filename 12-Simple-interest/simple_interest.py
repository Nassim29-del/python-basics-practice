
"""
Simple Interest Calculator

Calculates simple interest and the total amount
based on the principal, annual interest rate, and time.
"""


def simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Args:
        principal (float): Initial amount of money.
        rate (float): Annual interest rate in percentage.
        time (float): Time period in years.

    Returns:
        float: Calculated simple interest.
    """
    return principal * rate * time / 100


def main():
    """Get user input, calculate interest, and display results."""

    # Get the principal amount from the user
    principal = float(input("Principal amount: "))

    # Get the annual interest rate
    rate = float(input("Annual rate (%): "))

    # Get the time period in years
    time = float(input("Time (years): "))

    # Calculate the simple interest
    interest = simple_interest(principal, rate, time)

    # Display the interest and total amount
    print(f"Interest: {interest:.2f}")
    print(f"Total:    {principal + interest:.2f}")


# Run the main function when this file is executed directly
if __name__ == "__main__":
    main()
