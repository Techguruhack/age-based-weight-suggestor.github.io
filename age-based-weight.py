def my_get_weight_suggestion(my_age):
    if my_age < 2:
        my_weight_range = "Infants: 9-11 kg"
    elif 2 <= my_age < 4:
        my_weight_range = "Toddlers: 11-15 kg"
    elif 4 <= my_age < 6:
        my_weight_range = "Preschoolers: 15-20 kg"
    elif 6 <= my_age < 9:
        my_weight_range = "Young Children: 20-25 kg"
    elif 9 <= my_age < 12:
        my_weight_range = "Preteens: 25-35 kg"
    elif 12 <= my_age < 15:
        my_weight_range = "Teenagers: 35-45 kg"
    elif 15 <= my_age < 20:
        my_weight_range = "Young Adults: 45-60 kg"
    elif 20 <= my_age < 40:
        my_weight_range = "Adults: 60-80 kg"
    elif 40 <= my_age < 60:
        my_weight_range = "Middle-aged Adults: 70-90 kg"
    elif my_age >= 60:
        my_weight_range = "Seniors: 65-85 kg"
    else:
        my_weight_range = "Age not in range"

    return my_weight_range


my_age = int(input("Please enter your age: "))
my_suggested_weight = my_get_weight_suggestion(my_age)
print(f"Based on your age, the suggested weight range is: {my_suggested_weight}")
