
"""
Student Grade Calculator

Calculates the average of student scores
and assigns a letter grade based on the average.
"""


def letter_grade(average):
    """
    Determine the letter grade based on the average score.

    Args:
        average (float): Student's average score.

    Returns:
        str: Corresponding letter grade.
    """

    # Assign a letter grade based on the average
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'

    # Return F if the average is below 60
    return 'F'


def main():
    """Get student scores, calculate average, and display grade."""

    # Ask the user to enter scores separated by spaces
    raw = input("Enter scores separated by space: ")

    # Convert the entered scores into a list of numbers
    scores = [float(s) for s in raw.split()]

    # Calculate the average score
    average = sum(scores) / len(scores)

    # Determine the letter grade
    grade = letter_grade(average)

    # Display the average and corresponding letter grade
    print(f"Average: {average:.1f} (Grade {grade})")


# Execute the main function when the program runs directly
if __name__ == "__main__":
    main()
