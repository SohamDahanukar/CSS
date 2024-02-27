def power(a, b, P):
    if b == 1:
        return a
    else:
        return (pow(a, b) % P)

def main():
    P = 23  # Prime number (publicly available)
    G = 9   # Primitive root of P (publicly available)
    a = 4   # Private key for Alice
    b = 3   # Private key for Bob

    # Compute public values
    x = power(G, a, P)
    y = power(G, b, P)

    # Compute symmetric keys
    ka = power(y, a, P)
    kb = power(x, b, P)

    print(f"The value of P: {P}")
    print(f"The value of G: {G}")
    print(f"Private key for Alice: {a}")
    print(f"Private key for Bob: {b}")
    print(f"Secret key for Alice: {ka}")
    print(f"Secret key for Bob: {kb}")

if __name__ == "__main__":
    main()