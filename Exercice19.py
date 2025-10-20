def LengthOfWord(word):
    print(f"Le mot '{word}' contient {len(word)} caractères.")


def fibonacciSerie(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciSerie(n-1) + fibonacciSerie(n-2)