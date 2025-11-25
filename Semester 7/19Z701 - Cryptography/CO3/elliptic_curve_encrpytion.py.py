#!/usr/bin/env python3
"""
Elliptic Curve ElGamal Encryption Demonstration
Implements step-by-step Elliptic Curve ElGamal encryption with detailed arithmetic output.
"""

# Point at infinity representation
O = None


def mod_inv(a, p):
    """
    Compute modular inverse of a mod p using Extended Euclidean Algorithm.
    Prints all intermediate steps.
    """
    print(f"\n{'='*60}")
    print(f"Computing modular inverse of {a} mod {p}")
    print(f"{'='*60}")
    
    if a == 0:
        print("Error: Cannot compute inverse of 0")
        return None
    
    # Extended Euclidean Algorithm
    r1, r2 = p, a
    t1, t2 = 0, 1
    step = 1
    
    print(f"\nInitialization:")
    print(f"  r1 = {p}, r2 = {a}")
    print(f"  t1 = 0, t2 = 1")
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        
        print(f"\nStep {step}:")
        print(f"  q = r1 // r2 = {r1} // {r2} = {q}")
        print(f"  r = r1 mod r2 = {r1} mod {r2} = {r}")
        print(f"  t = t1 - q*t2 = {t1} - {q}*{t2} = {t1} - {q*t2} = {t}")
        
        r1, r2 = r2, r
        t1, t2 = t2, t
        
        step += 1
    
    if r1 != 1:
        print(f"\nGCD = {r1} ≠ 1, so {a} has no inverse mod {p}")
        return None
    
    inv = t1 % p
    if inv < 0:
        print(f"\n  t1 = {t1} is negative, adjusting: {t1} mod {p} = {inv}")
    else:
        print(f"\n  Final inverse: {t1} mod {p} = {inv}")
    
    print(f"Result: {a}^(-1) mod {p} = {inv}")
    print(f"{'='*60}\n")
    
    return inv


def mod_reduce(n, p):
    """Reduce n modulo p and print the reduction."""
    result = n % p
    if n != result:
        print(f"  {n} mod {p} = {result}")
    return result


def is_on_curve(P, curve, p):
    """
    Check if point P lies on the elliptic curve y^2 = x^3 + a*x + b (mod p).
    Prints the validation steps.
    """
    if P == O:
        print("  Point is O (point at infinity), which is on every curve.")
        return True
    
    x, y = P
    a, b = curve
    
    print(f"\n  Checking if ({x}, {y}) is on curve y^2 = x^3 + {a}*x + {b} (mod {p}):")
    
    # Left side: y^2 mod p
    lhs = (y * y) % p
    print(f"  Left side:  y^2 = {y}^2 = {y*y} mod {p} = {lhs}")
    
    # Right side: x^3 + a*x + b mod p
    x3 = (x * x * x) % p
    ax = (a * x) % p
    rhs = (x3 + ax + b) % p
    print(f"  Right side: x^3 + {a}*x + {b} = {x}^3 + {a}*{x} + {b}")
    print(f"              = {x3} + {ax} + {b} = {x3 + ax + b} mod {p} = {rhs}")
    
    is_valid = (lhs == rhs)
    print(f"  Result: {lhs} {'==' if is_valid else '≠'} {rhs} → {'VALID' if is_valid else 'INVALID'}")
    
    return is_valid


def point_add(P, Q, curve, p):
    """
    Add two points P and Q on the elliptic curve.
    Handles all cases: P != Q, P == Q (doubling), P = O, Q = O, P = -Q.
    Prints all intermediate calculations.
    """
    a, b = curve
    
    # Handle point at infinity
    if P == O:
        print(f"  P = O, so P + Q = Q = {Q}")
        return Q
    if Q == O:
        print(f"  Q = O, so P + Q = P = {P}")
        return P
    
    x1, y1 = P
    x2, y2 = Q
    
    # Check if P = -Q (i.e., P + Q = O)
    if x1 == x2 and (y1 + y2) % p == 0:
        print(f"  P = ({x1}, {y1}) and Q = ({x2}, {y2})")
        print(f"  x1 = x2 and y1 + y2 = {y1} + {y2} = {y1 + y2} ≡ 0 (mod {p})")
        print(f"  Therefore P = -Q, so P + Q = O")
        return O
    
    # Compute slope λ
    if x1 == x2 and y1 == y2:
        # Point doubling: λ = (3*x1^2 + a) * inv(2*y1) mod p
        print(f"  Point doubling: P = Q = ({x1}, {y1})")
        print(f"  λ = (3*x^2 + a) * inv(2*y) mod {p}")
        
        x1_sq = (x1 * x1) % p
        print(f"  x^2 = {x1}^2 = {x1*x1} mod {p} = {x1_sq}")
        
        three_x_sq = (3 * x1_sq) % p
        print(f"  3*x^2 = 3*{x1_sq} = {3*x1_sq} mod {p} = {three_x_sq}")
        
        numerator = (three_x_sq + a) % p
        print(f"  3*x^2 + a = {three_x_sq} + {a} = {three_x_sq + a} mod {p} = {numerator}")
        
        denominator = (2 * y1) % p
        print(f"  2*y = 2*{y1} = {2*y1} mod {p} = {denominator}")
        
        inv_denom = mod_inv(denominator, p)
        if inv_denom is None:
            return None
        
        lam = (numerator * inv_denom) % p
        print(f"  λ = {numerator} * {inv_denom} = {numerator * inv_denom} mod {p} = {lam}")
    else:
        # Point addition: λ = (y2 - y1) * inv(x2 - x1) mod p
        print(f"  Point addition: P = ({x1}, {y1}), Q = ({x2}, {y2})")
        print(f"  λ = (y2 - y1) * inv(x2 - x1) mod {p}")
        
        y_diff = (y2 - y1) % p
        print(f"  y2 - y1 = {y2} - {y1} = {y2 - y1} mod {p} = {y_diff}")
        
        x_diff = (x2 - x1) % p
        print(f"  x2 - x1 = {x2} - {x1} = {x2 - x1} mod {p} = {x_diff}")
        
        inv_x_diff = mod_inv(x_diff, p)
        if inv_x_diff is None:
            return None
        
        lam = (y_diff * inv_x_diff) % p
        print(f"  λ = {y_diff} * {inv_x_diff} = {y_diff * inv_x_diff} mod {p} = {lam}")
    
    # Compute x3 = λ^2 - x1 - x2 mod p
    lam_sq = (lam * lam) % p
    print(f"\n  Computing x3:")
    print(f"  λ^2 = {lam}^2 = {lam*lam} mod {p} = {lam_sq}")
    
    x3_temp = (lam_sq - x1 - x2) % p
    print(f"  x3 = λ^2 - x1 - x2 = {lam_sq} - {x1} - {x2} = {lam_sq - x1 - x2} mod {p} = {x3_temp}")
    x3 = x3_temp
    
    # Compute y3 = λ*(x1 - x3) - y1 mod p
    x1_minus_x3 = (x1 - x3) % p
    print(f"\n  Computing y3:")
    print(f"  x1 - x3 = {x1} - {x3} = {x1 - x3} mod {p} = {x1_minus_x3}")
    
    lam_times_diff = (lam * x1_minus_x3) % p
    print(f"  λ*(x1 - x3) = {lam} * {x1_minus_x3} = {lam * x1_minus_x3} mod {p} = {lam_times_diff}")
    
    y3_temp = (lam_times_diff - y1) % p
    print(f"  y3 = λ*(x1 - x3) - y1 = {lam_times_diff} - {y1} = {lam_times_diff - y1} mod {p} = {y3_temp}")
    y3 = y3_temp
    
    result = (x3, y3)
    print(f"\n  Result: ({x1}, {y1}) + ({x2}, {y2}) = ({x3}, {y3})")
    
    return result


def point_double(P, curve, p):
    """Double point P (convenience wrapper for point_add)."""
    print(f"\n  Doubling point {P}:")
    return point_add(P, P, curve, p)


def scalar_mult(n, P, curve, p):
    """
    Multiply scalar n by point P using double-and-add method.
    Prints each step of the binary method.
    """
    print(f"\n{'='*60}")
    print(f"Computing {n} * {P} using double-and-add method")
    print(f"{'='*60}")
    
    if n == 0:
        print("  n = 0, so result is O")
        return O
    
    if n < 0:
        print(f"  n = {n} is negative, computing {abs(n)} * (-P) instead")
        neg_P = (P[0], (-P[1]) % p) if P != O else O
        return scalar_mult(-n, neg_P, curve, p)
    
    # Convert n to binary
    n_bin = bin(n)[2:]
    print(f"\n  Binary representation of {n}: {n_bin}")
    print(f"  Processing bits from left to right (MSB to LSB)")
    
    result = O
    current = P
    
    print(f"\n  Initialization:")
    print(f"    result = O")
    print(f"    current = {P}")
    
    for i, bit in enumerate(n_bin):
        print(f"\n  Bit {i+1} (position {len(n_bin)-1-i}): bit = {bit}")
        
        if bit == '1':
            print(f"    Bit is 1, so we add current to result:")
            if result == O:
                print(f"      result = O, so result = current = {current}")
                result = current
            else:
                print(f"      result = result + current")
                result = point_add(result, current, curve, p)
        
        if i < len(n_bin) - 1:  # Don't double after the last bit
            print(f"    Doubling current for next iteration:")
            current = point_double(current, curve, p)
    
    print(f"\n  Final result: {n} * {P} = {result}")
    print(f"{'='*60}\n")
    
    return result


def ec_elgamal_encrypt(P_m, k, G, n_B, curve, p):
    """
    Perform Elliptic Curve ElGamal encryption.
    Returns ciphertext (C1, C2) and public key P_B.
    """
    print("\n" + "="*70)
    print("ELLIPTIC CURVE ELGAMAL ENCRYPTION")
    print("="*70)
    
    a, b = curve
    print(f"\nParameters:")
    print(f"  Prime field: p = {p}")
    print(f"  Curve: y^2 = x^3 + {a}*x + {b} (mod {p})")
    print(f"  Base point G = {G}")
    print(f"  B's secret key n_B = {n_B}")
    print(f"  Message point P_m = {P_m}")
    print(f"  Random ephemeral key k = {k}")
    
    # Step 1: Validate points
    print(f"\n{'='*70}")
    print("STEP 1: Validating points on curve")
    print(f"{'='*70}")
    
    print(f"\nValidating base point G = {G}:")
    if not is_on_curve(G, curve, p):
        print("ERROR: G is not on the curve!")
        # return None, None
    
    print(f"\nValidating message point P_m = {P_m}:")
    if not is_on_curve(P_m, curve, p):
        print("ERROR: P_m is not on the curve!")
        return None, None
    
    # Step 2: Compute public key P_B = n_B * G
    print(f"\n{'='*70}")
    print(f"STEP 2: Computing B's public key P_B = {n_B} * G")
    print(f"{'='*70}")
    P_B = scalar_mult(n_B, G, curve, p)
    print(f"\nB's public key: P_B = {P_B}")
    
    # Step 3: Compute C1 = k * G
    print(f"\n{'='*70}")
    print(f"STEP 3: Computing C1 = {k} * G")
    print(f"{'='*70}")
    C1 = scalar_mult(k, G, curve, p)
    print(f"\nC1 = {C1}")
    
    # Step 4: Compute k * P_B
    print(f"\n{'='*70}")
    print(f"STEP 4: Computing k * P_B = {k} * {P_B}")
    print(f"{'='*70}")
    k_P_B = scalar_mult(k, P_B, curve, p)
    print(f"\nk * P_B = {k_P_B}")
    
    # Step 5: Compute C2 = P_m + k*P_B
    print(f"\n{'='*70}")
    print(f"STEP 5: Computing C2 = P_m + k*P_B")
    print(f"        C2 = {P_m} + {k_P_B}")
    print(f"{'='*70}")
    C2 = point_add(P_m, k_P_B, curve, p)
    print(f"\nC2 = {C2}")
    
    # Summary
    print(f"\n{'='*70}")
    print("ENCRYPTION SUMMARY")
    print(f"{'='*70}")
    print(f"Public Key: P_B = {P_B}")
    print(f"Ciphertext: C = (C1, C2)")
    print(f"  C1 = {C1}")
    print(f"  C2 = {C2}")
    print(f"{'='*70}\n")
    
    return (C1, C2), P_B


if __name__ == "__main__":
    # Example parameters
    p = 11
    curve = (2, 9)  # y^2 = x^3 + x + 6
    G = (2, 7)
    n_B = 7
    P_m = (10, 9)
    k = 5
    
    # Run encryption
    ciphertext, public_key = ec_elgamal_encrypt(P_m, k, G, n_B, curve, p)
    
    if ciphertext:
        C1, C2 = ciphertext
        print("\nFinal Results:")
        print(f"  Public Key P_B: {public_key}")
        print(f"  Ciphertext C: ({C1}, {C2})")

