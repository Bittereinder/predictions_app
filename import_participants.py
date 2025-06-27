import sqlite3
import csv

DATABASE = "betting_pool.db"
CSV_FILE = "fifa_world_cup_2022_participants.csv"

def import_participants():
    conn = sqlite3.connect(DATABASE)
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Insert using only country_id, participant_id is autoincremented in DB
                conn.execute(
                    "INSERT OR IGNORE INTO participant (participant_id, country_id) VALUES (?, ?)",
                    (int(row["participant_id"]), int(row["country_id"]))
                )
        conn.commit()
        print("Participants imported successfully.")
    finally:
        conn.close()

if __name__ == "__main__":
    import_participants()