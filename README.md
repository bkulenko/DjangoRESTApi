# Django REST API

## Description
### /movies/ endpoint
A Django REST API that fetches all data related to a movie from OMDBAPI with a POST request with payload conforming to following pattern:

     {"name": "Movie Name"}

It fetches a JSON object from OMDBAPI which then gets deserialised and saved into default Django SQLite database, each JSON key into its own field.

With a GET request it fetches data about all the movies present in the database and serialises it back into a JSON object.
Data fetched from the database can be sorted by any key present in the model, if additional `sortarg` parameter is provided in following URL pattern:

    /movies/sort=sortarg

### /comments/ endpoint

The API can also save a comment about the movie to, if POST request contains a payload conforming to the following pattern:

    {"Movie": "IMDB movie id", "Comment": "Comment contents"}
    
The comment gets saved only if the database already stores the movie entity with IMDB id provided in request payload. Comment and movie models are not linked by foreign key.

Comments can also be filtered if additional movieid parameter is provided in the URL, conforming to following pattern:

    /comments/movieid

## Requirements
Main requirement of this API is Django REST Framework in version 3.8.2 and Django in version 2.1. Aside from Django REST Framework, the app does not use any other modules not already required by Django and DRF that are not already present in Python standard library.

Additional requirements are specified in `requirements.txt` file.

## Settings

The API uses default Django settings, apart from additional `OMDBKEY` parameter.

## Setup

The API contains all the source files necessary for running the application, aside from the database itself. Before running the app, make sure to make migrations!

## Tests

The API includes basic tests of its funcionality, meant to run on an empty database. The test script seeds the database with a test movie and comment objects. It then saves another movie entity to the database, tries to do it again to check if the API allows for storing multiple copies of the same entity (which it doesn't),
fetches all the movie objects, fetches all comments, fetches movies related to a speciffic movie (one seeded with `test_base_seed` method) and posts another comment.

The test script logs all test results to `testlog.txt` file in the `rest` folder.
