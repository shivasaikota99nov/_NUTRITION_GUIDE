def get_nutrition_suggestion(age):
    """
    Suggests nutrition/food recommendations based on age group.
    """

    if age < 0:
        return "Invalid age. Please enter a valid number."

    elif age <= 3:
        return (
            "Age Group: Infants (0-3 years)\n"
            "- Breast milk or formula\n"
            "- Soft mashed fruits (banana, apple)\n"
            "- Mashed vegetables (carrot, potato)\n"
            "- Iron-rich cereals"
        )

    elif age <= 12:
        return (
            "Age Group: Children (4-12 years)\n"
            "- Milk, eggs, fruits\n"
            "- Vegetables and whole grains\n"
            "- Light snacks (nuts, healthy sandwiches)\n"
            "- Adequate water"
        )

    elif age <= 19:
        return (
            "Age Group: Teenagers (13-19 years)\n"
            "- High-protein foods (egg, chicken, paneer)\n"
            "- Calcium-rich foods (milk, curd)\n"
            "- Fruits and salads\n"
            "- Avoid junk food"
        )

    elif age <= 60:
        return (
            "Age Group: Adults (20-60 years)\n"
            "- Balanced diet: rice/roti + dal + sabji\n"
            "- Lean proteins (dal, chicken, fish)\n"
            "- Seasonal fruits\n"
            "- Fiber-rich vegetables"
        )

    else:
        return (
            "Age Group: Senior Citizens (60+ years)\n"
            "- Soft, easy-to-digest food\n"
            "- Calcium and vitamin D rich foods\n"
            "- Low salt and low sugar diet\n"
            "- Hydration and soups"
        )

print("------ NUTRITION GUIDE ------")
try:
    age = int(input("Enter your age: "))
    recommendation = get_nutrition_suggestion(age)
    print("\nNutrition Suggestion:")
    print(recommendation)

except ValueError:
    print("Please enter a valid number for age.")
