import random
from flask import Flask, render_template

app = Flask(__name__)

main_dishes = ["Spaghetti Carbonara", "Grilled Chicken Caesar Salad", "Vegetable Stir-Fry", "Beef Tacos", "Mushroom Risotto", "Teriyaki Salmon"]
side_dishes = ["Garlic Bread", "Steamed Broccoli", "Roasted Potatoes", "Caprese Salad", "Quinoa Pilaf", "Grilled Asparagus"]
desserts = ["Chocolate Lava Cake", "Fruit Salad", "Cheesecake", "Apple Pie", "Tiramisu", "Ice Cream Sundae"]
    
def get_complex_dinner_suggestion():
    main_dish = random.choice(main_dishes)
    side_dish = random.choice(side_dishes)
    dessert = random.choice(desserts)
    return main_dish, side_dish, dessert
    
"""
Randomly selects a main dish, a side dishes and a dessert 
from predefined lists and prints out the dinner suggestion. 
"""
@app.route('/')
def index():
    main, side, dessert = get_complex_dinner_suggestion()
    return render_template('index.html', main=main, side=side, dessert=dessert)

if __name__ == '__main__':
    app.run(debug=True)
