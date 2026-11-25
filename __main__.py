from sqlite3 import connect, Row, Error
from datetime import date
from database import inicializar_banco

busca = input("Quem você está procurando? ").strip()
hoje = date.today()

try:
    inicializar_banco()

    with connect("meubanco2.db") as banco:
        banco.row_factory = Row
        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM amigos WHERE nome LIKE ?",
            (f"%{busca}%",)
        )

        total = 0

        for total, amigo in enumerate(cursor, start=1):
            txtNasc = amigo['nascimento']
            info_nasc = ""

            if not txtNasc:
                info_nasc = "sem data de nascimento"
            else:
                try:
                    data = date.fromisoformat(str(txtNasc))
                    jaPassou = (hoje.month, hoje.day) >= (data.month, data.day)
                    idade = hoje.year - data.year - (0 if jaPassou else 1)
                    info_nasc = f"nasceu em {data:%d/%m/%Y} e tem {idade} anos"

                except ValueError:
                    info_nasc = "data inválida"

            print(f"{amigo['nome']} {info_nasc}")

        print("-" * 55)

        if total == 0:
            print(f"Não encontrei ninguém com {busca} no nome!")
        elif total == 1:
            print(f"Encontrei apenas um amigo com {busca}")
        else:
            print(f"Ao todo encontrei {total} amigos com \"{busca}\"")

except Error as erro:
    print(f"\033[31mFalha no banco -> {erro}\033[m")

except Exception as erro:
    print(f"\033[31mAlgo deu errado -> {erro}\033[m")

print("ACABOU!")