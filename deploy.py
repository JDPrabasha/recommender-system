import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)


def get_similar_movies(movie, rating):
    similar_score = rank_df[movie]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score[similar_score.index != movie][:5].index.tolist()


rank_df = pd.read_pickle("model.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    movie = request.form['movie']

    return render_template('index.html', foobar=get_similar_movies(movie, 5))


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")
