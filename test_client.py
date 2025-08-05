import requests

def get_recipe(cuisine):
    try:
        response = requests.get("http://127.0.0.1:5000/", params={"cuisine": cuisine})
        
        
        data = response.json()

        if response.status_code == 200:
            print("✅ Recipe received:")
            print("Name:", data["recipe"]["name"])
            print("Ingredients:", ", ".join(data["recipe"]["ingredients"]))
            print("Instructions:", data["recipe"]["instructions"])
        else:
            print("❌ Error:", data["error"])
    except Exception as e:
        print("Request failed:", e)

#  test
get_recipe("i")
