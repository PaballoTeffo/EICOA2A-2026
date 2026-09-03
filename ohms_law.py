def calc_resistance(voltage, current):
    """
    Calculate electrical resistance using Ohm's law.
    Args:
    voltage (float): Voltage across the component in volts (V).
    current (float): Current through the component in amperes (A). Must be non-zero.
    Returns:
    float: Resistance in ohms.
    Notes:
    The function raises a ZeroDivisionError if current is 0
    """
    return voltage / current
