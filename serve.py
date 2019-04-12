from flask import Flask
from flask_caching import Cache
from watchlist2rss import get_feed

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=900)
def letterboxd_watchlist():
    feed = get_feed()
    if not feed:
        return "No movies found"
    else:
        return feed.rss_str()

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')