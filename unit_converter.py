def mm_to_inches(mm):
    """
    Convert a length from millimetres to inches.
    Args:
    mm (float): Length in millimetres (mm).
    Returns:
    float: The equivalent length in inches.
    """
    inches = mm / 25.4
    return inches


def inches_to_mm(inches):
    """
    Convert a length from inches to millimetres.
    Args:
    inches (float): Length in inches.
    Returns:
    float: The equivalent length in millimetres (mm).
    """
    mm = inches * 25.4
    return mm