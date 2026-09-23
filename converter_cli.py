from unit_converter import mm_to_inches, inches_to_mm

direction = input("Enter conversion (mm_to_inches or inches_to_mm): ")
value = float(input("Enter the measurement: "))

if direction == "mm_to_inches":
    result = mm_to_inches(value)
    print("Coverted value:" , result, "inches")
elif direction == "inches_to_mm":
    result = inches_to_mm(value)
    print("Converted value:", result, "mm")
else:
    print("Invalid conversion option.")

print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)