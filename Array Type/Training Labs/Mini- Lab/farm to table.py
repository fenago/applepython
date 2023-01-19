# Create lists of fruits and vegetables
fruits = ["apple", "orange", "banana"]
vegetables = ["tomatoes", "carrots", "kale"]

# Print the lists
print("Fruits: ", fruits)
print("Vegetables: ", vegetables)

# Function to add new ingredients to the lists
def add_ingredient(ingredient, ingredient_type):
    if ingredient_type.lower() == "fruit":
        fruits.append(ingredient)
    elif ingredient_type.lower() == "vegetable":
        vegetables.append(ingredient)
    else:
        print("Invalid ingredient type. Please enter 'fruit' or 'vegetable'.")

# Function to create a new dish using the available ingredients
def create_dish(dish_name):
    ingredients = input("Enter ingredients for the dish separated by commas: ").split(",")
    dish = [dish_name]
    for ingredient in ingredients:
        ingredient = ingredient.strip()
        if ingredient in fruits:
            dish.append(ingredient)
        elif ingredient in vegetables:
            dish.append(ingredient)
        else:
            print(f"{ingredient} is not available.")
    return dish

# Add new ingredients to the lists
add_ingredient("strawberries", "fruit")
add_ingredient("spinach", "vegetable")

# Print the updated lists
print("Fruits: ", fruits)
print("Vegetables: ", vegetables)

# Create a new dish
new_dish = create_dish("Fruit and Veggie Salad")
print("New Dish: ", new_dish)
