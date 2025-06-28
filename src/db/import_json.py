import sqlite3
import pathlib
import json

BASE_DIR = pathlib.Path(__file__).parent
DB_FILE = BASE_DIR / "predictions.db"
JSON_FILES = [
    (BASE_DIR / "access_level.json", "access_level"),
    (BASE_DIR / "countries.json", "countries"),
    (BASE_DIR / "rounds.json", "rounds"),
    (BASE_DIR / "teams.json", "teams")
]

def import_json_into_db(json_file, table):
    """Function to import data from json files into the tables"""
    try:
        # Read the json data
        with open(json_file, 'r', encoding="utf-8") as file:
            data = json.load(file)
        # Create/open the database
        with sqlite3.connect(DB_FILE) as conn:
            # Create a cursor object
            cursor = conn.cursor()
            # Commit the changes
            conn.commit()
    except:
        pass

if __name__ == "__main__":
    for json_file, table in JSON_FILES:
        import_json_into_db(json_file, table)
# End-Of-File (EOF)