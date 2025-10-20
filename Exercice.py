with open("Table_de_multiplication.txt", "w+", encoding="utf-8") as file:
    for a in range(1, 11):
        file.write(f"{'='*10} Table de multiplication de {a:02} {'='*10}\n")
        for b in range(1, 11):
            file.write(f"{a:02} x {b:02} = {a * b:02}\n")
        file.write("\n")
