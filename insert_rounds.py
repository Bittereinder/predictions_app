import sqlite3

DATABASE = "betting_pool.db"

rounds = [
    ("Group Stage", "group"),
    ("Round of 16", "knockout"),
    ("Quarterfinals", "knockout"),
    ("Semifinals", "knockout"),
    ("Final", "knockout"),
    ("Third Place", "knockout")
]

def insert_rounds():
    conn = sqlite3.connect(DATABASE)
    try:
        for name, stage in rounds:
            conn.execute(
                "INSERT OR IGNORE INTO round (name, stage) VALUES (?, ?)",
                (name, stage)
            )
        conn.commit()
        print("Rounds inserted.")
    finally:
        conn.close()

if __name__ == "__main__":
    insert_rounds()