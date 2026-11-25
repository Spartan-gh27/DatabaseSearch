from sqlite3 import connect

def inicializar_banco():
    with connect("meubanco2.db") as banco:
        cursor = banco.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS amigos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                nascimento TEXT
            )
        """)

        cad_amigos = [
            ("Gustavo", "2002-06-13"),
            ("Lucas", "1995-01-12"),
            ("Beatriz", "2001-11-23"),
            ("Rafael", "1988-07-05"),
            ("Amanda", "2001-03-30"),
            ("Cláudio", "1985-05-10"),
            ("Pedro", "2003-01-24"),
            ("João", "")
        ]

        cursor.executemany(
            "INSERT OR IGNORE INTO amigos (nome, nascimento) VALUES (?, ?)",
            cad_amigos
        )