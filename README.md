# Flask Gevent Audio Streaming

## Background

I don't have anything on my GitHub so I'm building this project and I always wondered how to a stream of some sort.
If there's anything you would recommend with my code Feel free to submit a pull request

## Features

- Streams MP3 files sequentially as a continuous radio stream
- Uses `gevent` for efficient green-threaded concurrency
- Supports multiple clients without blocking
- Runs on a `gevent.pywsgi.WSGIServer` for improved performance.

## Requirements

```
Python 3.8+
    Flask
    gevent
```

## Usage

1. Clone this repository simply by running the following command: <i>(be sure to have git installed)</i>

```sh
git clone https://github.com/s2kshare/Flask-Gevent-Audio-Streaming.git
cd Flask-Gevent-Audio-Streaming/Radio-Backend
```

2. Navigate dependencies:

```sh
pip install -r requirements.txt
```

3. Create an `audios/` directory within the root folder and add your selected MP3 files:

```sh
mkdir audios
```

4. Running the flask application is pretty easy! Just run the following:

```sh
python app.py
```

The server will start on [http://0.0.0.0:5000/radio](http://0.0.0.0:5000/radio). Clients can connect to this endpoint to listen to the stream!

# API

- `GET /radio`
  - This endpoint streams audio in real-time
  - Response MIME type: `audio/mpeg`

## TODO:

- [ ] Implement configuration files for usage simplicity
- [ ] Add functionality of shuffling upon request
- [ ] Create endpoint with ID to create unique hosting session
- [ ] Create endpoints to return metadata of current track and next track
- [ ] Create a request endpoint which takes in links from supported sites
- [ ] Create tests for checking state of endpoints

## Contributing

Feel free to submit pull requests or open issues for improvements!
