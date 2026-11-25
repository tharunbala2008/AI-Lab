def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be numeric")
    return round((celsius * 9 / 5) + 32, 2)
