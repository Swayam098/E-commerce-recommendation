import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Sample data for illustration
# Replace this with actual data source like a CSV or database
ratings_dict = {
    "userID": [1, 1, 1, 2, 2, 3, 3, 4],
    "itemID": [1, 2, 3, 1, 2, 2, 3, 3],
    "rating": [5, 3, 4, 4, 2, 5, 4, 5]
}
df = pd.DataFrame(ratings_dict)

# Home route to render the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['userID'])
    item_id = int(request.form['itemID'])

    # Dummy logic: Replace this with actual recommendation logic
    # Filter the DataFrame by the user ID to simulate recommendations
    user_data = df[df['userID'] == user_id]

    if user_data.empty:
        recommendation = f"No data found for User ID: {user_id}"
    else:
        # Example: Get all the items the user has rated and suggest one with the highest rating
        recommended_item = user_data.loc[user_data['rating'].idxmax()]['itemID']
        recommendation = f"Based on your preferences, we recommend Item ID: {recommended_item}"

    return f"<h1>{recommendation}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
