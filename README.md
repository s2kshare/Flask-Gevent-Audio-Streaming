# Flask Gevent Audio Streaming

> Heya, how's it?

## Background

During a discord call with the boys, a friend of mine (new to programming) was having trouble trying to build a radio station API. He mentioned that he's been going at it for a days and he just cant seem to crack it, so I asked if I could assist him.

After talking back and forward for a bit and reading over his source, he felt discouraged and decided to discard the project entirely. He seemed really excited about this specific project and I wanted to help him get back on track with developing this.

So I decided to make this repository for anyone else who could possibly be in the same position. Hopefully this can help whoever is new to python or new to trying flask!

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

## Installation

1. Clone this repository simply by running the following command: <i>(be sure to have git installed)</i>

```sh
git clone https://github.com/s2kshare/Flask-Gevent-Audio-Streaming.git
cd Flask-Gevent-Audio-Streaming
```

2. Navigate dependencies:

```sh
pip install -r requirements.txt
```

3. Create an `audios/` directory within the root folder and add your selected MP3 files:

```sh
mkdir audios
```

## Usage

Running the flask application is pretty easy!
Just pop open a terminal / command prompt and run this command in root:

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
