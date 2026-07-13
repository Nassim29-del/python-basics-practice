# Calculates BMI from weight (kg) and height (m) and gives a category.

def bmi_category(bmi):
    if bmi < 18.5 :
        return "Underweight"
    elif bmi < 25 :
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    return "obese"


def main():
    weight = float(input("Enter your Weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight / height ** 2
    print(f"BMI: {bmi:.1f} ({bmi_category(bmi)})")


if __name__ == "__main__":
    main()
