# Dictionary of dictionaries: each motor ID (key) holds its own record (value)
motors = {
# fault_codes is a list because a motor can report the same fault more than
# once, and the order faults were reported in doesn't matter for counting them.
    "M-101": {
        "location": "Workshop A",
        "rated_power_kw": 5.5,
        "temperature": 72,
        "status": "RUNNING",
        "fault_codes": ["F01", "F03", "F01"]
    },
    "M-102": {
        "location": "Workshop B",
        "rated_power_kw": 7.5,
        "temperature": 88,
        "status": "RUNNING",
        "fault_codes": ["F07", "F03"]

    },
    "M-103": {
        "location": "Pump Station",
        "rated_power_kw": 11.0,
        "temperature": 79,
        "status": "SERVICE REQUIRED",
        "fault_codes": ["F12", "F07"]
    }
}

# Requirement 1: display the complete record for M-102
print("Record for M-102:", motors["M-102"])

# Requirement 2: update the status of M-102
# Two keys: the first picks the motor,the second picks the field inside it
motors["M-102"]["status"] = "OVERHEAT"
print("Updated M-102 status:", motors["M-102"]["status"])

# Requirements 3: loop through every motor
# .items() gives each motor ID (key) and its record (value) together
hot_count = 0  # Requirement 4: counter starts at zero
# unique_faults is a set because a fault code should only be counted once,
# even if several motors report the same one
unique_faults = set ()  # Requirement 5: collects fault codes, no duplicates

print("\nAll motors:")
for motor_id, details in motors.items():
    print(motor_id, "|", details["location"], "|", details["temperature"], "°C |", details["status"])
    if details["temperature"] > 85:
        hot_count = hot_count + 1
    unique_faults.update(details["fault_codes"])

print("Motors above 85 °C:", hot_count)
print("Unique fault codes:", unique_faults)
print("Number of unique faults:", len(unique_faults))