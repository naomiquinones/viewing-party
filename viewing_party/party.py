def create_movie(movie_title, genre, rating):
   return {"title":movie_title, "genre":genre, "rating":rating} if (movie_title and genre and rating) else None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    wl = user_data["watchlist"]
    for item in wl:
        if item["title"] == title:
            add_to_watched(user_data,wl.pop(wl.index(item)))
    return user_data

def get_watched_avg_rating(user_data):
    cumulative_ratings = 0
    watched = user_data["watched"]
    for item in watched:
        cumulative_ratings += item["rating"]

    return cumulative_ratings/len(watched) if len(watched) > 0 else 0

def get_most_watched_genre(user_data):
    counts = {}
    watched = user_data["watched"]
    popular = ['',0]
    for item in watched:
        this_genre_count = item["genre"]
        if this_genre_count not in counts:
            counts[this_genre_count] = 1
        else:
            counts[this_genre_count] += 1
        if counts[this_genre_count] > popular[1]:
            popular[0] = this_genre_count
            popular[1] = counts[this_genre_count]

    return popular[0] if popular[1] > 0 else None
