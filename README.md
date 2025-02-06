# Spotify Music Recommendation System

This project builds a **music recommendation system** using **K-Means clustering** to group songs with similar features and a **distance-based recommendation algorithm** to suggest songs based on a given track. The dataset consists of Spotify album and feature data from 2023.

## Motivation
With millions of songs available on streaming platforms, finding similar tracks can be challenging. This project applies machine learning techniques to analyze song features and recommend similar tracks.

## Features

- **Data Preprocessing**:
  - Merges Spotify album data with song feature data.
  - Handles missing values and normalizes numeric features.

- **Clustering Songs**:
  - Uses **K-Means clustering** to group songs into clusters based on their audio features.

- **Song Recommendation System**:
  - Implements a **distance-based** recommendation algorithm.
  - Finds and suggests similar songs based on a given track.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- NumPy
- Pandas
- Matplotlib & Seaborn (for visualization)
- Scikit-learn (for clustering & scaling)
- tqdm (for progress bars)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/spotify-recommendation-system.git
cd spotify-recommendation-system
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the Jupyter Notebook
```bash
jupyter notebook Spotify_rec.ipynb
```

## How It Works

### 1. Data Preprocessing
- Loads Spotify album data (`spotify-albums_data_2023.csv`) and track feature data (`spotify_features_data_2023.csv`).
- Merges the datasets on the `track_id` column.
- Cleans missing values and normalizes numeric features using **MinMaxScaler**.

### 2. K-Means Clustering
- Applies **K-Means** clustering to group songs into **35 clusters** based on their feature similarity.

### 3. Recommendation System
- Uses a **custom distance function** to find and suggest songs most similar to a given track.
- Example:
  ```python
  recommendations = Spotify_rec(df)
  recommendations.recommend("Lover", 13)  # Recommends 13 similar songs
  ```

## To-Do

- [ ] Improve clustering by experimenting with more algorithms like Expectation Maximization.
- [ ] Enhance the recommendation model using additional feature engineering.
- [ ] Deploy the recommendation system using a web app (Streamlit)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
