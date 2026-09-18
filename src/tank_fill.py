INCHES_PER_FOOT = 12.0
CUBIC_FEET_TO_GALLONS = 7.48052


def calculate_tank_volume(length_ft, width_ft, depth_in):
    if length_ft <= 0:
        raise ValueError("Tank length must be greater than zero.")

    if width_ft <= 0:
        raise ValueError("Tank width must be greater than zero.")

    if depth_in <= 0:
        raise ValueError("Fill depth must be greater than zero.")

    depth_ft = depth_in / INCHES_PER_FOOT
    volume_cubic_ft = length_ft * width_ft * depth_ft
    volume_gallons = volume_cubic_ft * CUBIC_FEET_TO_GALLONS

    return volume_gallons
