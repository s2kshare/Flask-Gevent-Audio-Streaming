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

1. Clone this repository

```sh

```
