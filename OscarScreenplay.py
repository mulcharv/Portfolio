# To run please ensure pip and flask modules are installed on a version of python 3.0 or later.
# As well, run on local server http://127.0.0.1:5000/ in your web browser. 
# By: Rahul Mulchandani

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# List of Oscar winning screenplays from the last 30 years. 
screenplays = [
    {'id': 1,
     'title': 'Thelma & Louise',
     'screenwriter': 'Callie Khouri',
     'year': '1991'},
    {'id': 2,
     'title': 'The Crying Game',
     'screenwriter': 'Neil Jordan',
     'year': '1992'},
    {'id': 3,
     'title': 'The Piano',
     'screenwriter': 'Jane Campion',
     'year': '1993'},
    {'id': 4,
     'title': 'Pulp Fiction',
     'screenwriter': 'Quentin Tarantino',
     'year': '1994'},
    {'id': 5,
     'title': 'The Usual Suspects',
     'screenwriter': 'Christopher McQuarrie',
     'year': '1995'},
    {'id': 6,
     'title': 'Fargo',
     'screenwriter': 'Joel Coen',
     'year': '1996'},
    {'id': 7,
     'title': 'Good Will Hunting',
     'screenwriter': 'Ben Affleck & Matt Damon',
     'year': '1997'},
    {'id': 8,
     'title': 'Shakespeare In Love',
     'screenwriter': 'Marc Norman',
     'year': '1998'},
    {'id': 9,
     'title': 'American Beauty',
     'screenwriter': 'Alan Ball',
     'year': '1999'},
    {'id': 10,
     'title': 'Almost Famous',
     'screenwriter': 'Cameron Crowe',
     'year': '2000'},
    {'id': 11,
     'title': 'Gosford Park',
     'screenwriter': 'Julian Fellowes',
     'year': '2001'},
    {'id': 12,
     'title': 'Talk To Her',
     'screenwriter': 'Pedro Almodovar',
     'year': '2002'},
    {'id': 13,
     'title': 'Lost In Translation',
     'screenwriter': 'Sofia Coppola',
     'year': '2003'},
    {'id': 14,
     'title': 'Eternal Sunshine Of The Spotless Miind',
     'screenwriter': 'Charlie Kaufman',
     'year': '2004'},
    {'id': 15,
     'title': 'Crash',
     'screenwriter': 'Paul Haggis & Bobby Moresco',
     'year': '2005'},
    {'id': 16,
     'title': 'Little Miss Sunshine',
     'screenwriter': 'Michael Arndt',
     'year': '2006'},
    {'id': 17,
     'title': 'Juno',
     'screenwriter': 'Diablo Cody',
     'year': '2007'},
    {'id': 18,
     'title': 'Milk',
     'screenwriter': 'Dustin Lance Black',
     'year': '2008'},
    {'id': 19,
     'title': 'The Hurt Locker',
     'screenwriter': 'Mark Boal',
     'year': '2009'},
    {'id': 20,
     'title': 'The Kings Speach',
     'screenwriter': 'David Seidler',
     'year': '2010'},
    {'id': 21,
     'title': 'Midnight In Paris',
     'screenwriter': 'Woody Allen',
     'year': '2011'},
    {'id': 22,
     'title': 'Django Unchained',
     'screenwriter': 'Quentin Tarantino',
     'year': '2012'},
    {'id': 23,
     'title': 'Her',
     'screenwriter': 'Spike Jonze',
     'year': '2013'},
    {'id': 24,
     'title': 'Birdman',
     'screenwriter': 'Armando Bo, Alexander Dinelaris Jr., Nicolas Giacobone, Alejandro G. Inarritu',
     'year': '2014'},
    {'id': 25,
     'title': 'Spotlight',
     'screenwriter': 'Tom McCarthy & Josh Singer',
     'year': '2015'},
    {'id': 26,
     'title': 'Manchester By The Sea',
     'screenwriter': 'Kenneth Lonergan',
     'year': '2016'},
    {'id': 27,
     'title': 'Get Out',
     'screenwriter': 'Jordan Peele',
     'year': '2017'},
    {'id': 28,
     'title': 'Green Book',
     'screenwriter': 'Brian Currie, Peter Farrelly, Nick Vallelonga',
     'year': '2018'},
    {'id': 29,
     'title': 'Parasite',
     'screenwriter': 'Bong Joon-ho & Han Jin-won',
     'year': '2019'},
    {'id': 30,
     'title': 'Promising Young Woman',
     'screenwriter': 'Emerald Fennell',
     'year': '2020/2021'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Recent Oscar Screenplay Winners Archive</h1>
<p>A prototype API for Oscar winning screenplays of the last 30 years.</p>'''


# A route to return all of the available entries in the catalog.
@app.route('/api/v1/resources/screenplays/all', methods=['GET'])
def api_all():
    return jsonify(screenplays)

@app.route('/api/v1/resources/screenplays', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for screenplay in screenplays:
        if screenplay['id'] == id:
            results.append(screenplay)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()