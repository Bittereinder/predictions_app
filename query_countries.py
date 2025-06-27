import sqlite3

DATABASE = "betting_pool.db"

def get_all_countries():
    conn = sqlite3.connect(DATABASE)
    try:
        cursor = conn.execute("SELECT country_id, code, name FROM country ORDER BY name")
        countries = cursor.fetchall()
        with open("countries.txt", "w", encoding="utf-8") as f:
            for country_id, iso2, name in countries:
                f.write(f"{country_id}\t{iso2}\t{name}\n")
        print("All countries written to countries.txt")
    finally:
        conn.close()

if __name__ == "__main__":
    get_all_countries()