def euler_phi(n: int) -> int:
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        else:
            i += 1
    if n > 1:
        result -= result // n
    print("euler: ", result)
    return result


def egcd(a, b) -> (int, int, int):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def find_secret_key(e: int, Fn: int) -> int:
    gcd, x, y = egcd(e, Fn)
    if gcd != 1:
        return None
    else:
        return x % Fn


def parse_cipher_text(cipher_text: str, n: int) -> list:
    result: list = list()
    str_n: str = str(n)

    i = 0
    while i < len(cipher_text) - len(str_n):
        if int(cipher_text[i: i + len(str_n)]) < n:
            result.append(cipher_text[i: i + len(str_n)])
            i += len(str_n)
        else:
            result.append(cipher_text[i: i + len(str_n) - 1])
            i += len(str_n) - 1
    result.append(cipher_text[i: len(cipher_text)])

    print("Распарсенный С: ", result)
    return result


def decrypt_message(lst_cipher: list, d: int, n: int) -> str:
    decrypted: str = ''
    for c in lst_cipher:
        m = pow(int(c), d, n)
        print(m)
        decrypted += str(m)

    print("Исходное М (int): ", decrypted)

    result: str = ''
    for i in range(0, len(decrypted), 2):
        result += chr(int(decrypted[i: i + 2]))
    return result


def test_key(d: int, e: int, Fn: int) -> bool:
    return d == pow(e, euler_phi(Fn) - 1, Fn)


def RSA_decrypt(cipher_text: str, e: int, n: int) -> bool:
    Fn: int = euler_phi(n)

    d: int = find_secret_key(e, Fn)
    if d is None:
        print("Были переданы неверные значения!")
        return False
    print("Ключ верный? ", test_key(d, e, Fn))
    print("d: ", d)

    parsed_cipher: list = parse_cipher_text(cipher_text, n)

    message: str = decrypt_message(parsed_cipher, d, n)
    print(message)

    return True


def main():
    cipher_text: str = "6073334549854737481838817505469218919893372481934272786799829052850710603231301937207488228"
    e: int = 11119
    n: int = 1814354438978629

    RSA_decrypt(cipher_text, e, n)


if __name__ == '__main__':
    main()
