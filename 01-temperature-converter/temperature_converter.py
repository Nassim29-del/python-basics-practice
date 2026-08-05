# Converts a temperature between Celsius, Fahrenheit and Kelvin.

def convert(value, from_unit, to_unit):
    from_unit, to_unit = from_unit.upper(), to_unit.upper()
    # First get everything into Celsius.
    if from_unit == "C":
        c = value
    elif from_unit == "F":
        c = (value - 32) * 5 / 9
    elif from_unit == "K":
        c = value - 273.15
    else:
        raise ValueError("Unit must be C, F or K")
    # Then out to the target unit.
    if to_unit == "C":
        return c
    elif to_unit == "F":
        return c * 9 / 5 + 32
    elif to_unit == "K":
        return c + 273.15
    else:
        raise ValueError("Unit must be C, F or K")


def main():
    value = float(input("Enter temperature value: "))
    from_unit = input("From unit (C/F/K): ")
    to_unit = input("To unit (C/F/K): ")
    result = convert(value, from_unit, to_unit)
    print(f"{value} {from_unit.upper()} = {result:.2f} {to_unit.upper()}")


if __name__ == "__main__":
    main()
