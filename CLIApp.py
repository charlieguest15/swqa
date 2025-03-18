
def calculate_bmi(height_inches, weight_pounds):
    """Calculate BMI given height in inches and weight in pounds."""
    return round((weight_pounds * 720) / (height_inches ** 2), 1)

def categorize_bmi(bmi):
    """Return BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    feet = int(input("Enter height (feet): "))
    inches = int(input("Enter additional inches: "))
    weight = float(input("Enter weight (lbs): "))

    total_inches = (feet * 12) + inches
    bmi = calculate_bmi(total_inches, weight)
    category = categorize_bmi(bmi)

    print(f"\nYour BMI: {bmi}")
    print(f"Category: {category}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
