"""
Temperature Converter
Converts between Celsius, Fahrenheit, and Kelvin.
"""

def cel_to_fah(c):
    return ( c * 9/5 ) + 32

def cel_to_kel(c):
    return c + 273.15

def fah_to_cel(f):
    return ( f - 32) * 5 / 9

def kel_to_cel(k):
    return k - 273.15

def main():
    print("Temperature Converter")
    print("1: Celsuis to Fahrenheit")
    print("2: Celsuis to Kelvin")
    print("3: Fahreneit to Celsuis")
    print("4: Kelvin to Celsuis")

    choice = input("Choose a conversion (1-4): ")

    try:
        temp = float(input("Enter the Temperature: "))
    except ValueError:
        print("That's not a valid number.")
        return
    
    if choice == "1":
        print(f"{temp}C = {cel_to_fah(temp): .2f}F")
    elif choice == "2":
        print(f"{temp}C = {cel_to_kel(temp): .2f}K")
    elif choice == "3":
        print(f"{temp}F = {fah_to_cel(temp): .2f}C")
    elif choice == "4":
        print(f"{temp}K = {kel_to_cel(temp): .2f}C")
    else:
        print("Invalid Choice.")

if __name__ == "__main__":
    main()

