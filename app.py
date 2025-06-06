from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load mood to playlist mapping
playlist_df = pd.read_csv('mood_playlist.csv')

# Dummy mood prediction (replace with ML model later)
def predict_mood(text):
    text = text.lower()
    if any(word in text for word in ['happy', 'joy', 'excited']):
        return 'happy'
    elif any(word in text for word in ['sad', 'down', 'blue']):
        return 'sad'
    elif any(word in text for word in ['angry', 'mad', 'furious']):
        return 'angry'
    else:
        return 'relaxed'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_text = data.get('text', '')
    mood = predict_mood(user_text)
    playlist_row = playlist_df[playlist_df['mood'] == mood]
    if not playlist_row.empty:
        playlist_link = playlist_row.iloc[0]['playlist']
    else:
        playlist_link = ''
    return jsonify({'mood': mood, 'playlist': playlist_link})

if __name__ == '__main__':
    app.run(debug=True)