import media
import fresh_tomatoes

# Create movie objects

grand_budapest = media.Movie(
    "The Grand Budapest Hotel",
    "Adventures of a concierge in a decaying European luxury hotel",
    "https://upload.wikimedia.org/wikipedia/en/a/a6/" +
    "The_Grand_Budapest_Hotel_Poster.jpg",
    "https://www.youtube.com/watch?v=1Fg5iWmQjwk",
    "2278388")

life_acquatic = media.Movie(
    "The Life Acquatic with Steve Zissou",
    "Adventures of an ageing ocean explorer and his team",
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",
    "https://www.youtube.com/watch?v=yh401Rmkq0o",
    "0362270")

shining = media.Movie(
    "The Shining",
    "Summary of everything that can go wrong when taking care of hotel",
    "https://upload.wikimedia.org/wikipedia/en/2/25/The_Shining_poster.jpg",
    "https://www.youtube.com/watch?v=5Cb3ik6zP2I",
    "0081505")

# Create array of movie objects
movies = [grand_budapest, life_acquatic, shining]
# Create movies page
fresh_tomatoes.open_movies_page(movies)
