def max_int_chain(n: int) -> int:
    if n < 5:
        return -1
    return (n // 2) * ((n // 2) + 1) if n % 2 != 0 else ((n // 2) * (n // 2)) - 1
