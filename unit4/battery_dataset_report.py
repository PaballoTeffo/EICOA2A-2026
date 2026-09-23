# List of battery voltage readings (V)
voltages = [12.8, 11.4, 12.1, 10.9, 12.7, 11.8, 13.0, 11.2]

# Counters for each category, all start at zero
good_count = 0
marginal_count = 0
low_count = 0

# Second list to store every LOW reading
low_voltages = []

# Loop through readings; enumerate gives the reading number, starting at 1
for number, voltage in enumerate(voltages, start=1):
    print("Reading", number, ":", voltage, "V")
    # Classify: check the highest range first, so each reading lands in one category
    if voltage > 12.5:
        print(" GOOD")
        good_count = good_count + 1
    elif voltage >= 11.5:  # already <= 12.5 here, so this covers 11.5 to 12.5 inclusive
        print(" MARGINAL")
        marginal_count = marginal_count + 1
    else:
        print(" LOW")
        low_count = low_count + 1
        low_voltages.append(voltage)  # store every LOW reading

# Display the counters and LOW readings list
print("GOOD:", good_count)
print("MARGINAL:", marginal_count)
print("LOW:", low_count)
print("Low-voltage readings:", low_voltages)

# Calculations: sum() adds the list, len() counts the readings
total_voltage = sum(voltages)
average_voltage = total_voltage / len(voltages)
print("Total voltage:", round(total_voltage, 2), "V")
print("Average voltage:", round(average_voltage, 2), "V")
print("Highest voltage:", max(voltages), "V")
print("Lowest voltage:",min(voltages), "V")

# Search the list with the "in" operator
search_value = 12.1
if search_value in voltages:
    print(search_value, "V was record.")
else:
    print(search_value, "V was not recorded.")