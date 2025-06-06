# Mood-Based Playlist Recommender

A web application that recommends Spotify playlists based on your current mood. Built with Flask (Python), HTML/CSS, and JavaScript.

## Features
- Enter your mood and get a curated Spotify playlist suggestion
- Fun, interactive UI with animated background and emoji suggestions
- Responsive design for desktop and mobile

## Demo
![Screenshot](screenshot.png)

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/moood-playlist-recommender.git
   cd moood-playlist-recommender

   2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open your browser and go to: http://localhost:5000
## Project Structure
```
├── app.py                # Flask backend
├── mood_playlist.csv     # Mood to playlist mapping
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # CSS styles
├── templates/
│   └── index.html        # Main HTML template
└── venv/                 # Virtual environment (not tracked 
by git)
```
## Deployment
- You can deploy the frontend on Vercel (static files) and the backend (Flask) on platforms like Render, Railway, or Heroku.
- For Vercel, move static files and templates as needed, and set up an API endpoint for the backend.
## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT