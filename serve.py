import os
from flask import Flask
from flask_caching import Cache
from watchlist2rss import get_feed

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache_timeout = os.environ.get('CACHE_TIMEOUT', 900)

app = Flask(__name__)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=cache_timeout)
def letterboxd_watchlist():
    feed = get_feed()
    if not feed:
        return "No movies found"
    else:
        return Response(feed.rss_str(), mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
