# Define WHO guidelines for water quality
WHO_GUIDELINES = {
    "ph_min": 6.5,
    "ph_max": 7.0,
    "turbidity_max": 5.0,  # NTU
    "contaminants_max": 100  # ppm
}

def validate_input(prompt, min_value=None, max_value=None):
    """
    Validates user input to ensure it's a number and optionally within a range.
    """
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        finally:
            print("Thanks for your contribution")

def analyze_water(ph, turbidity, contaminants):
    """
    Analyzes water quality based on WHO guidelines.
    Returns a tuple (status, issues) where:
    - status: 'safe' or 'unsafe'
    - issues: List of detected problems
    """
    issues = []
    if not (WHO_GUIDELINES['ph_min'] <= ph <= WHO_GUIDELINES['ph_max']):
        issues.append(f"pH out of range (Expected: {WHO_GUIDELINES['ph_min']} - {WHO_GUIDELINES['ph_max']})")
    if turbidity > WHO_GUIDELINES['turbidity_max']:
        issues.append(f"Turbidity very high (Max: {WHO_GUIDELINES['turbidity_max']} NTU)")
    if contaminants > WHO_GUIDELINES['contaminants_max']:
        issues.append(f"Contaminants level too high (Max: {WHO_GUIDELINES['contaminants_max']} ppm)")

    status = "safe" if not issues else "unsafe"
    return status, issues

def recommend_purification_methods(issues):
    """
    Provides purification recommendations based on detected issues.
    """
    recommendations = []
    for issue in issues:
        if "pH" in issue:
            recommendations.append("Use pH balancers eg buffer solutions.")
        if "Turbidity" in issue:
            recommendations.append("Filter water using cloth, sand, or advanced filtration methods.")
        if "Contaminant" in issue:
            recommendations.append("Use activated carbon filters or reverse osmosis.")
    return recommendations

def main():
    print("=== Water Quality Tracker ===")
    print("Input water quality parameters for assessment:")
    
     # Collect user inputs
    ph_level = validate_input("Enter pH level  ")
    turbidity = validate_input("Enter Turbidity level (NTU)  ")
    contaminants = validate_input("Enter Contaminants level (ppm)  ")

    # Analyze water quality
    status, issues = analyze_water(ph_level, turbidity, contaminants)
    print("\n=== Water Quality Report ===")
    if status == "safe":
        print(" Water is safe for drinking.")
    else:
        print(" Water is unsafe. Impurities detected:")
        for issue in issues:
            print(f"- {issue}")

        # Provide purification recommendations
        print("\nRecommended Actions:")
        recommendations = recommend_purification_methods(issues)
        for rec in recommendations:
            print(f"- {rec}")

if __name__ == "__main__":
    main()
