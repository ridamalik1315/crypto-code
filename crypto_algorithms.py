import hashlib
from typing import Optional


def xor_encrypt(plain: str, key: str) -> str:
    if not key:
        raise ValueError("Key must not be empty.")

    cipher_parts: list[str] = []
    key_len = len(key)

    for i, ch in enumerate(plain):
        ascii_plain = bin(ord(ch))[2:].zfill(7)
        ascii_key = bin(ord(key[i % key_len]))[2:].zfill(7)

        bits = []
        for a, b in zip(ascii_plain, ascii_key):
            bits.append("0" if a == b else "1")

        cipher_parts.append(str(int("".join(bits), 2)))

    return " ".join(cipher_parts)


def xor_decrypt(ciphertext: str, key: str) -> str:
    if not key:
        raise ValueError("Key must not be empty.")

    key_len = len(key)
    parts = [p for p in ciphertext.split() if p]
    plain_chars: list[str] = []

    for i, token in enumerate(parts):
        value = int(token)
        ascii_cipher = bin(value)[2:].zfill(7)
        ascii_key = bin(ord(key[i % key_len]))[2:].zfill(7)

        bits = []
        for a, b in zip(ascii_cipher, ascii_key):
            bits.append("0" if a == b else "1")

        plain_char = chr(int("".join(bits), 2))
        plain_chars.append(plain_char)

    return "".join(plain_chars)


def is_valid_permutation_key(key: str) -> bool:
    if len(key) == 0 or len(key) > 10:
        return False
    length = len(key)
    for i in range(length):
        if str(i) not in key:
            return False
    return True


def permutation_encrypt(plain: str, key: str) -> str:
    if not is_valid_permutation_key(key):
        raise ValueError("Key must contain each index (0..n-1) exactly once and be at most length 10.")

    key_len = len(key)
    while len(plain) % key_len != 0:
        plain += " "

    cipher_chars: list[str] = []

    for block_start in range(0, len(plain), key_len):
        block = plain[block_start:block_start + key_len]
        for i in range(key_len):
            cipher_chars.append(block[int(key[i])])

    return "".join(cipher_chars)


def permutation_decrypt(cipher: str, key: str) -> str:
    if not is_valid_permutation_key(key):
        raise ValueError("Key must contain each index (0..n-1) exactly once and be at most length 10.")

    key_len = len(key)
    if key_len == 0 or len(cipher) % key_len != 0:
        raise ValueError("Ciphertext length must be a multiple of the key length.")

    plain_chars: list[str] = []

    for block_start in range(0, len(cipher), key_len):
        block = cipher[block_start:block_start + key_len]
        plain_block = [" "] * key_len

        for i, ch in enumerate(block):
            original_index = int(key[i])
            plain_block[original_index] = ch

        plain_chars.extend(plain_block)

    return "".join(plain_chars).rstrip()


def rsa_encrypt(plain: str, exponent: int, modulus: int) -> str:
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")

    parts: list[str] = []
    for letter in plain:
        asc = ord(letter)
        new_asc = pow(asc, exponent, modulus)
        parts.append(str(new_asc))

    return " ".join(parts)


def rsa_decrypt(ciphertext: str, exponent: int, modulus: int) -> str:
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")

    nums = [int(i) for i in ciphertext.split() if i]
    plain_chars: list[str] = []

    for num in nums:
        new_asc = pow(num, exponent, modulus)
        plain_chars.append(chr(new_asc))

    return "".join(plain_chars)


_MD5_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def md5_bruteforce_3char(target_hash: str) -> Optional[str]:
    """
    Brute-force a 3-character string (letters + digits) whose MD5 matches target_hash.
    Returns the string if found, otherwise None.
    """
    normalized_target = target_hash.strip().lower()

    for a in _MD5_CHARS:
        for b in _MD5_CHARS:
            for c in _MD5_CHARS:
                candidate = a + b + c
                h = hashlib.md5(candidate.encode("utf8")).hexdigest()
                if h == normalized_target:
                    return candidate

    return None

