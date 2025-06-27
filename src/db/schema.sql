PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
  user_id       INTEGER PRIMARY KEY AUTOINCREMENT,
  username      TEXT    NOT NULL UNIQUE,
  password_hash TEXT    NOT NULL,
  access_id     INTEGER NOT NULL,
  first_name    TEXT    NOT NULL,
  last_name     TEXT    NOT NULL,
  last_login    DATETIME,
  email         TEXT    NOT NULL,
  FOREIGN KEY(access_id) REFERENCES access_level(access_id)
);

CREATE TABLE IF NOT EXISTS access_level (
  access_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name      TEXT    NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS countries (
  country_id INTEGER PRIMARY KEY AUTOINCREMENT,
  code       TEXT    NOT NULL UNIQUE,
  name       TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS teams (
  team_id INTEGER PRIMARY KEY AUTOINCREMENT,
  country_id     INTEGER NOT NULL UNIQUE,
  FOREIGN KEY(country_id) REFERENCES countries(country_id)
);

CREATE TABLE IF NOT EXISTS rounds (
  round_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name     TEXT    NOT NULL,
  stage    TEXT    NOT NULL CHECK(stage IN ('group','knockout'))
);

CREATE TABLE IF NOT EXISTS matches (
  match_id     INTEGER PRIMARY KEY AUTOINCREMENT,
  round_id     INTEGER NOT NULL,
  home_id      INTEGER NOT NULL,
  away_id      INTEGER NOT NULL,
  match_time   DATETIME NOT NULL,
  allow_until  DATETIME NOT NULL,
  home_score   INTEGER,
  away_score   INTEGER,
  FOREIGN KEY(round_id) REFERENCES rounds(round_id),
  FOREIGN KEY(home_id) REFERENCES teams(team_id),
  FOREIGN KEY(away_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS predictions (
  bet_id         INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id        INTEGER NOT NULL,
  match_id       INTEGER NOT NULL,
  predicted_home INTEGER NOT NULL,
  predicted_away INTEGER NOT NULL,
  placed_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(user_id) REFERENCES users(user_id),
  FOREIGN KEY(match_id) REFERENCES matches(match_id),
  UNIQUE (user_id, match_id)
);

CREATE TABLE IF NOT EXISTS scoring_rules (
  rule_id        INTEGER PRIMARY KEY AUTOINCREMENT,
  round_id       INTEGER,
  exact_points   INTEGER NOT NULL DEFAULT 3,
  winner_points  INTEGER NOT NULL DEFAULT 1,
  multiplier     REAL    NOT NULL DEFAULT 1.0,
  FOREIGN KEY(round_id) REFERENCES rounds(round_id)
);
