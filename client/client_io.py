from dateutil import parser
import client_constants
import tempfile
import datetime
import json
import os

# lokale constante voor rapport lokatie
_REPORTER_JSON_PATH = os.path.join(tempfile.gettempdir(), "pypackage_reporter.json")

# functie voor het controleren of er een nieuw rapport gemaakt dient te worden
def new_report_needed() -> bool:

    # check if a local report exists
    if os.path.isfile(_REPORTER_JSON_PATH):
        # local report found, check timestamp
        with open(_REPORTER_JSON_PATH, "r") as f:
            
            #parse the json data
            report = json.load(f)
            report_timestamp = parser.parse(report["timestamp"])

            # compare timestamp with current time
            time_difference = datetime.datetime.now() - report_timestamp
            if time_difference.total_seconds() < 86400: # 86400 seconden is 24 uur
                return False    # lokaal rapport is aanwezig en niet ouder dan 24 uur, geen nieuw rapport nodig

    return True

# functie voor het opslaan van objecten als json-bestand 
def store_as_json(report):

    #TODO exceptie afhandeling
    with open(_REPORTER_JSON_PATH, "w") as f:
        json.dump(report, f, indent=4, default=serialize)   # schrijf data weg als JSON, met indent voor leesbaarheid en default serializator voor objecten die niet rechtstreeks serializeerbaar zijn

# ondersteunende functie for JSON serializatie, neemt een object en returned dit als JSON-serializeerbaar object
def serialize(obj):
    
    # zet date/time om naar string
    if (isinstance(obj, datetime.date)) or isinstance(obj, datetime.time):
        serial = obj.isoformat()
        return serial

    # zet complexe objecten om naar dictionary
    return obj.__dict__





