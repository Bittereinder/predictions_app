import sqlite3
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
DB_FILE = BASE_DIR / "predictions.db"
SCHEMA = BASE_DIR / "schema.sql"

def init_db():
    """Function to create the database and tables"""
    try:
        # Create the database
        with sqlite3.connect(DB_FILE) as conn:
            # Create a cursor object
            cursor = conn.cursor()
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
            # Read schema.sql file contents
            with open(SCHEMA, "r", encoding="utf-8") as f:
                schema_sql = f.read()
            # Execute the SQL command       
            cursor.executescript(schema_sql)
            # Commit the changes
            conn.commit()
            print(f"{SCHEMA} executed succesfully.")
            
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)

if __name__ == "__main__":
    init_db()
# End-Of-File (EOF)