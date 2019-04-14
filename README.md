# Letterboxd Watchlist to RSS converter in Docker

convert your [Letterboxd Watchlist](https://letterboxd.com/) into an RSS feed to process in other applications using this simple Docker container.

Example:  
`$ docker build git@github.com:romanpeters/letterboxd-watchlist-rss.git -t letterboxd-rss`  
`$ docker run --rm -it -e LETTERBOXD_USER=<username> -p 5000:5000 letterboxd-rss`

Environment variables:
- LETTERBOXD_USER: your Letterboxd username (required)
- CACHE_TIMEOUT: time in seconds to hold in cache (default=900)
- FEED_LENGTH: max RSS feed length (default=100)
