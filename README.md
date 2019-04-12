# Letterboxd Watchlist to RSS converter in Docker

convert your [Letterboxd Watchlist](https://letterboxd.com/) into an RSS feed to process in other applications using this simple Docker container.

Example:
`$ docker build git@github.com:DevOps-Utrecht/bot -t letterboxd-rss`
`$ docker run --rm -it -e LETTERBOXD_USER=<username> -p 80:80 letterboxd-rss`
