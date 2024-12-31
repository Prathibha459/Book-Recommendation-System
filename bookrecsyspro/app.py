from flask import Flask,render_template;
import pickle

popular_df = pickle.load(open('popular.pkl','rb'))
app = Flask(__name__,template_folder='templates')

@app.route('/')

def index():
    return render_template('index.html',
                           bookname = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M	'].values),
                           Votes = list(popular_df['num_ratings'].values),
                            Rating= list(popular_df['avg_rating'].values),
                           )

if __name__ == '__main__':
    app.run(debug=True)
