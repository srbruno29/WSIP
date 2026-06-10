import sqlite3

# Script de migração: remove coluna de plataforma se existir, e garante o esquema sem plataforma
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

def get_columns():
    cursor.execute("PRAGMA table_info(games)")
    return [row[1] for row in cursor.fetchall()]

cols = get_columns()

desired = [
    ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
    ("name", "TEXT NOT NULL"),
    ("genre", "TEXT NOT NULL"),
    ("status", "TEXT NOT NULL"),
    ("cover_url", "TEXT"),
    ("release_date", "TEXT"),
    ("rating", "REAL")
]

if "platform" in cols or "platforma" in cols:
    print("Detectada coluna de plataforma — recriando tabela sem ela...")

    # Criar tabela temporária
    cursor.execute("DROP TABLE IF EXISTS games_new")
    cols_sql = ",\n    ".join([f"{name} {typ}" for name, typ in desired])
    cursor.execute(f"CREATE TABLE games_new ({cols_sql})")

    # Montar seleção mapeando colunas antigas para novas (aceita nomes em pt/eng)
    def pick(old_names):
        for n in old_names:
            if n in cols:
                return n
        return "NULL"

    name_col = pick(["name", "nome"])
    genre_col = pick(["genre", "genero"])
    status_col = pick(["status"])
    cover_col = pick(["cover_url"])
    release_col = pick(["release_date"])
    rating_col = pick(["rating"])

    select_cols = f"{name_col} AS name, {genre_col} AS genre, {status_col} AS status, {cover_col} AS cover_url, {release_col} AS release_date, {rating_col} AS rating"

    cursor.execute(f"INSERT INTO games_new (name, genre, status, cover_url, release_date, rating) SELECT {select_cols} FROM games")

    cursor.execute("DROP TABLE games")
    cursor.execute("ALTER TABLE games_new RENAME TO games")
    conn.commit()
    print("Migração concluída: plataforma removida")
else:
    print("Nenhuma coluna de plataforma encontrada; nada a fazer")

conn.close()