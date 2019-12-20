def bmi_calculator(weight, height) -> str:
    """Calculates BMI and return a string explaining the result.
       Weight: kilograms (int)
       Height: meters (float)"""
    calculation = weight / height ** 2
    if calculation < 18.5:
        return "under"
    if 18.5 <= calculation < 25:
        return "normal"
    if 25 <= calculation < 30:
        return "over"
    return "obese"
