# Assignment07

Sync And Async Programming In Python With [AIOHTTP](https://docs.aiohttp.org/en/stable/) And [AsyncIO](https://docs.python.org/3/library/asyncio.html)

## Classroom Activities

Simple Excersize To Introduce with async/await/sync Concepts

## Async API

A relatively more advanced exercise than the previous one, in which there are several methods that are supposed to be executed asynchronously, named `rhyme_finder` and `get_coordinates`, in the first one a request is sent to the HTTP server to receive the rhyme of the chosen word, and in the second one that It is a bit more complicated, first I get the list of provinces of Iran, then a random province is selected from the list, and then the cities of that province are received from the next API, and the geographic location of that city will ultimately be the value of Kharoji, and these two methods `rhyme_finder` and `get_coordinates` are executed asynchronously and without affecting each other

## Usage

```shell
git clone "https://github.com/FarzadForuozanfar/PyDeploy-Course.git"
cd PyDeploy-Course/Assignment07/Async_API
python script.py
```

## Dependencies

```shell
pip install aiohttp python-dotenv
```

* AIOHTTP
* dotenv
