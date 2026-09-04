from ohms_law import calc_resistance
from unit_converter import mm_to_inches, inches_to_mm


def display_menu():
    """Print a numbered menu of engineering calculations.

    The menu includes:
    1. Calculate resistance (Ohm's Law)
    2. Convert length (mm_to_in)
    3. Exit
    """
    print("\n--- Engineering Calculator Menu ---")
    print("1. Calculate resistance")
    print("2. Covert length")
    print("3. Exit")


def main():
    running = True
    while running:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))
            resistance = calc_resistance(voltage, current)
            print("Resistance =", resistance, "ohms")
            print(calc_resistance.__doc__)

        elif choice == "2":
            direction = input("Enter conversion (mm_to_in or in_to_mm): ")
            value = float(input("Enter the measurement: "))
            if direction == "mm_to_in":
                print("Converted value:", mm_to_inches(value), "inches")
            elif direction == "in_to_mm":
                print("Converted value:", inches_to_mm(value), "mm")
            else:
                print("Invalid conversion option.")
            print(mm_to_inches.__doc__)

        elif choice == "3":
            running = False
            print("Program closed.")

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()