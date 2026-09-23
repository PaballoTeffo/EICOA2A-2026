# A dictionary (components) stores each component's ID and voltage together
# A tuple (voltage_tolerance) stores the fixed minimum/maximum lomits - they must not change.
# A list (inspection_rows) builds the table rows in order for display.
# A set (failed_ids) collects failed component IDs ith no duplicates.
# The virtual environment keeps tabulate isolated to this project.

print(comp_ids = ["ECU-101", "ECU-102", "ECU-103", "ECU-104", "ECU-105", "ECU-106", "EC-107", "ECU-108"])
print(voltages = [4.96, 5.08, 4.88, 5.15, 4.99, 4.91, 5.05])


voltage_tolerane = (4.90, 5.10)
minimum_voltage, maximum_voltage = voltage_tolerance

random.seed(42)
sample_ids = random.sample(list(components.keys()), 4)

inspection_rows = []
pass_count = 0
fail_count = 0
failed_ids = set()

for component_id in sample_ids:
   voltage = components[component_id]
   if minimum_voltage <= voltage <= maximum_voltage:
      result = "PASS"
      pass_count += 1
   else:
      result = "FAIL"
      fail_count +=1
      failed_ids.add(components_id)
   