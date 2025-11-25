# sdes_verbose.py
# Simple DES (SDES) implementation with verbose print statements for manual verification.
# Works with 8-bit plaintext and 10-bit key (strings of '0'/'1').
import random

P10 = [3, 5, 2, 4, 7, 10, 1, 9, 6, 8]
P8  = [6, 3, 4, 7, 8, 5, 10, 9]
IP  = [7, 6, 3, 1, 4, 8, 2, 5]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP  = [4, 1, 2, 3, 2, 3, 4, 1]
P4  = [2, 4, 3, 1]

S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [1, 0, 3, 2],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

def permute(bits: str, table):
    return ''.join(bits[i-1] for i in table)

def left_shift(bits: str, n: int):
    return bits[n:] + bits[:n]

def xor_bits(a: str, b: str):
    return ''.join('0' if x==y else '1' for x,y in zip(a,b))

def sbox_lookup(bits: str, sbox):
    # bits is 4-bit string
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1:3], 2)
    val = sbox[row][col]
    return format(val, '02b')

def generate_subkeys(key10: str, verbose=True):
    if verbose:
        print(f"Original 10-bit key: {key10}")
    p10_out = permute(key10, P10)
    if verbose:
        print(f"After P10: {p10_out}")
    left = p10_out[:5]
    right = p10_out[5:]
    if verbose:
        print(f"Split into L and R: L={left}, R={right}")

    # first left shift by 1
    left1 = left_shift(left,1)
    right1 = left_shift(right,1)
    if verbose:
        print(f"After LS-1: L1={left1}, R1={right1}")

    k1 = permute(left1 + right1, P8)
    if verbose:
        print(f"Subkey K1 (after P8): {k1}")

    # second left shift: total shift of 2 from original (i.e., shift one more)
    left2 = left_shift(left1,2)  # note: shifting left1 by 2 equals original left shifted by 3
    right2 = left_shift(right1,2)
    if verbose:
        print(f"After LS-2 (on L1/R1): L2={left2}, R2={right2}")

    k2 = permute(left2 + right2, P8)
    if verbose:
        print(f"Subkey K2 (after P8): {k2}")

    return k1, k2

def fk(bits8: str, subkey: str, stage_name=""):
    # bits8: 8-bit string: left(4) + right(4)
    left = bits8[:4]
    right = bits8[4:]
    print(f"\n--- fk {stage_name} ---")
    print(f"Input to fk: L={left}, R={right}, subkey={subkey}")

    # Expand and permute right half
    expanded = permute(right, EP)
    print(f"Expanded R (E/P): {expanded}")

    # XOR with subkey
    xored = xor_bits(expanded, subkey)
    print(f"After XOR with subkey: {xored}")

    # S-boxes
    left_sbox_in = xored[:4]
    right_sbox_in = xored[4:]
    print(f"S-box inputs: left={left_sbox_in}, right={right_sbox_in}")

    s0_out = sbox_lookup(left_sbox_in, S0)
    s1_out = sbox_lookup(right_sbox_in, S1)
    print(f"S-box outputs: S0={s0_out}, S1={s1_out}")

    combined_sboxes = s0_out + s1_out
    print(f"Combined S-box output (4 bits): {combined_sboxes}")

    p4_out = permute(combined_sboxes, P4)
    print(f"After P4 permutation: {p4_out}")

    # XOR with left half
    left_xored = xor_bits(left, p4_out)
    print(f"Left XOR P4 result: {left_xored}")

    # result is (left_xored, right) — note: no swap here, swap done by caller if needed
    result = left_xored + right
    print(f"fk output (L' R): {result}")
    return result

def switch_halves(bits8: str):
    left = bits8[:4]
    right = bits8[4:]
    switched = right + left
    print(f"Switch halves (SW): before={bits8} after={switched}")
    return switched

def encrypt(plaintext8: str, key10: str, verbose=True):
    print("\n==== SDES ENCRYPTION ====")
    if verbose:
        print(f"Plaintext (8-bit): {plaintext8}")
    k1, k2 = generate_subkeys(key10, verbose=verbose)
    # initial permutation
    ip_out = permute(plaintext8, IP)
    if verbose:
        print(f"\nAfter initial permutation IP: {ip_out}")

    # fk with K1
    fk1_out = fk(ip_out, k1, stage_name="(using K1)")
    # switch
    sw = switch_halves(fk1_out)
    # fk with K2
    fk2_out = fk(sw, k2, stage_name="(using K2)")
    # inverse IP
    cipher = permute(fk2_out, IP_INV)
    if verbose:
        print(f"\nAfter inverse IP (ciphertext): {cipher}")
    return cipher

def decrypt(cipher8: str, key10: str, verbose=True):
    print("\n==== SDES DECRYPTION ====")
    if verbose:
        print(f"Ciphertext (8-bit): {cipher8}")
    k1, k2 = generate_subkeys(key10, verbose=verbose)
    # note: decryption uses subkeys in reverse order
    ip_out = permute(cipher8, IP)
    if verbose:
        print(f"\nAfter initial permutation IP: {ip_out}")
    fk1_out = fk(ip_out, k2, stage_name="(using K2 for decrypt)")
    sw = switch_halves(fk1_out)
    fk2_out = fk(sw, k1, stage_name="(using K1 for decrypt)")
    plain = permute(fk2_out, IP_INV)
    if verbose:
        print(f"\nAfter inverse IP (recovered plaintext): {plain}")
    return plain

def validate_bitstring(s: str, length: int, name="value"):
    if len(s) != length or any(c not in '01' for c in s):
        raise ValueError(f"{name} must be a {length}-bit string of 0/1. Got: '{s}'")

if __name__ == "__main__":
    # Example: using the classic SDES example values
    example_key = ''.join(random.choices('01', k=10))  # 10-bit key
    example_plain = ''.join(random.choices('01', k=8))  # 8-bit plaintext

    print("Example run with key =", example_key, "and plaintext =", example_plain)
    validate_bitstring(example_key, 10, "key")
    validate_bitstring(example_plain, 8, "plaintext")

    ciphertext = encrypt(example_plain, example_key, verbose=True)
    print("\n=== Final ciphertext:", ciphertext)

    # Decrypt to verify
    recovered = decrypt(ciphertext, example_key, verbose=True)
    print("\n=== Recovered plaintext:", recovered)

    # Interactive prompt
    while True:
        ans = input("\nDo you want to encrypt/decrypt another? (e/d/q): ").strip().lower()
        if ans == 'q':
            break
        if ans not in ('e','d'):
            print("Type 'e' to encrypt, 'd' to decrypt, 'q' to quit.")
            continue
        key = input("Enter 10-bit key (e.g., 1010000010): ").strip()
        try:
            validate_bitstring(key, 10, "key")
        except ValueError as ve:
            print(ve); continue
        if ans == 'e':
            pt = input("Enter 8-bit plaintext: ").strip()
            try:
                validate_bitstring(pt, 8, "plaintext")
            except ValueError as ve:
                print(ve); continue
            print("\nEncrypting...")
            print(encrypt(pt, key, verbose=True))
        else:
            ct = input("Enter 8-bit ciphertext: ").strip()
            try:
                validate_bitstring(ct, 8, "ciphertext")
            except ValueError as ve:
                print(ve); continue
            print("\nDecrypting...")
            print(decrypt(ct, key, verbose=True))
