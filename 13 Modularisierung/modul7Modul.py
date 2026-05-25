def fak(n: int) -> int:
    if n < 2:
        return 1
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod


# nur ausführen, wenn das Skript direkt aufgerufen wird
if __name__ == "__main__":
    print(fak(5))