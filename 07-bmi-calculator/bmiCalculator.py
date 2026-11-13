
# Function to determine the BMI category based on the calculated BMI value
def bmi_category(bmi):
    # Check if BMI is below 18.5 (Underweight)
    if bmi < 18.5:
        return "Underweight"

    # Check if BMI is between 18.5 and 24.9 (Normal weight)
    elif bmi < 25:
        return "Normal weight"

    # Check if BMI is between 25 and 29.9 (Overweight)
    elif bmi < 30:
        return "Overweight"

    # If BMI is 30 or above, the category is Obese
    return "Obese"


# Main function: collects user information and calculates BMI
def main():
    # Ask the user to enter their weight in kilograms
    weight = float(input("Weight (Kg): "))

    # Ask the user to enter their height in meters
    height = float(input("Height (m): "))

    # Calculate BMI using the formula: weight / height squared
    bmi = weight / height ** 2

    # Display the BMI rounded to one decimal place and its category
    print(f"BMI: {bmi:.1f} ({bmi_category(bmi)})")


# Check if this file is being run directly
if __name__ == "__main__":
    # Call the main function to start the program
    main()
