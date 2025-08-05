from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

recipes = {
    "mexican": {
        "name": "Tacos",
        "ingredients": ["tortilla", "beef", "cheese", "lettuce"],
        "instructions": "Cook beef, assemble in tortilla, add toppings."
    },
    "italian": {
        "name": "Spaghetti",
        "ingredients": ["pasta", "tomato sauce", "parmesan"],
        "instructions": "Boil pasta, add sauce, sprinkle cheese."
    }
}

@app.route('/', methods=['GET'])
def get_recipe():
    cuisine = request.args.get('cuisine', '').lower()
    if cuisine in recipes:
        return jsonify({
            "recipe": recipes[cuisine],
            "timestamp": datetime.utcnow().isoformat()
        })
    else:
        return jsonify({
            "error": "Cuisine not found",
            "timestamp": datetime.utcnow().isoformat()
        }), 404

if __name__ == '__main__':
    app.run(debug=True)
