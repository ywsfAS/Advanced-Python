with open("Table_de_multiplication.txt", "w+") as file:
    for a in range(1, 11):
        file.write(f"Table de multiplication de {a:02}\n")
        for b in range(1, 11):
            file.write(f"{a:02} x {b:02} = {a * b}\n")
        file.write("\n")
