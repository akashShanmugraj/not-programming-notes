#!/usr/bin/env python3
"""
Elliptic Curve Point Addition
Performs elliptic curve point addition with step-by-step output.
Supports default values ('d') and random values ('r').
"""

import random

# Point at infinity representation
O = None


def mod_inv(a, p):
    """
    Compute modular inverse of a mod p using Extended Euclidean Algorithm.
    """
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


def point_add(P, Q, a, b, p):
    """
    Add two points P and Q on the elliptic curve y^2 = x^3 + a*x + b (mod p).
    Handles all cases: P != Q, P == Q (doubling), P = O, Q = O, P = -Q.
    Does not validate if points are on the curve.
    """
    print(f"\n{'='*70}")
    print(f"ELLIPTIC CURVE POINT ADDITION")
    print(f"{'='*70}")
    print(f"Curve: y^2 = x^3 + {a}*x + {b} (mod {p})")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"{'='*70}")

    # Handle point at infinity
    if P == O:
        print(f"P = O, so P + Q = Q = {Q}")
        return Q
    if Q == O:
        print(f"Q = O, so P + Q = P = {P}")
        return P

    x1, y1 = P
    x2, y2 = Q

    # Check if P = -Q (i.e., P + Q = O)
    if x1 == x2 and (y1 + y2) % p == 0:
        print(f"P = ({x1}, {y1}) and Q = ({x2}, {y2})")
        print(f"x1 = x2 and y1 + y2 = {y1} + {y2} = {y1 + y2} ≡ 0 (mod {p})")
        print(f"Therefore P = -Q, so P + Q = O")
        return O

    # Compute slope λ
    if x1 == x2 and y1 == y2:
        # Point doubling: λ = (3*x1^2 + a) * inv(2*y1) mod p
        print(f"Point doubling: P = Q = ({x1}, {y1})")
        print(f"λ = (3*x^2 + a) * inv(2*y) mod {p}")

        x1_sq = (x1 * x1) % p
        print(f"x^2 = {x1}^2 = {x1*x1} mod {p} = {x1_sq}")

        three_x_sq = (3 * x1_sq) % p
        print(f"3*x^2 = 3*{x1_sq} = {3*x1_sq} mod {p} = {three_x_sq}")

        numerator = (three_x_sq + a) % p
        print(f"3*x^2 + a = {three_x_sq} + {a} = {three_x_sq + a} mod {p} = {numerator}")

        denominator = (2 * y1) % p
        print(f"2*y = 2*{y1} = {2*y1} mod {p} = {denominator}")

        inv_denom = mod_inv(denominator, p)
        if inv_denom is None:
            return None

        lam = (numerator * inv_denom) % p
        print(f"λ = {numerator} * {inv_denom} = {numerator * inv_denom} mod {p} = {lam}")
    else:
        # Point addition: λ = (y2 - y1) * inv(x2 - x1) mod p
        print(f"Point addition: P = ({x1}, {y1}), Q = ({x2}, {y2})")
        print(f"λ = (y2 - y1) * inv(x2 - x1) mod {p}")

        y_diff = (y2 - y1) % p
        print(f"y2 - y1 = {y2} - {y1} = {y2 - y1} mod {p} = {y_diff}")

        x_diff = (x2 - x1) % p
        print(f"x2 - x1 = {x2} - {x1} = {x2 - x1} mod {p} = {x_diff}")

        inv_x_diff = mod_inv(x_diff, p)
        if inv_x_diff is None:
            return None

        lam = (y_diff * inv_x_diff) % p
        print(f"λ = {y_diff} * {inv_x_diff} = {y_diff * inv_x_diff} mod {p} = {lam}")

    # Compute x3 = λ^2 - x1 - x2 mod p
    lam_sq = (lam * lam) % p
    print(f"\nComputing x3:")
    print(f"λ^2 = {lam}^2 = {lam*lam} mod {p} = {lam_sq}")

    x3_temp = (lam_sq - x1 - x2) % p
    print(f"x3 = λ^2 - x1 - x2 = {lam_sq} - {x1} - {x2} = {lam_sq - x1 - x2} mod {p} = {x3_temp}")
    x3 = x3_temp

    # Compute y3 = λ*(x1 - x3) - y1 mod p
    x1_minus_x3 = (x1 - x3) % p
    print(f"\nComputing y3:")
    print(f"x1 - x3 = {x1} - {x3} = {x1 - x3} mod {p} = {x1_minus_x3}")

    lam_times_diff = (lam * x1_minus_x3) % p
    print(f"λ*(x1 - x3) = {lam} * {x1_minus_x3} = {lam * x1_minus_x3} mod {p} = {lam_times_diff}")

    y3_temp = (lam_times_diff - y1) % p
    print(f"y3 = λ*(x1 - x3) - y1 = {lam_times_diff} - {y1} = {lam_times_diff - y1} mod {p} = {y3_temp}")
    y3 = y3_temp

    result = (x3, y3)
    print(f"\nResult: ({x1}, {y1}) + ({x2}, {y2}) = ({x3}, {y3})")
    print(f"{'='*70}\n")

    return result


def get_random_prime():
    """Get a small random prime for testing."""
    primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    return random.choice(primes)


def generate_random_point(p, a, b):
    """Generate a random point on the curve y^2 = x^3 + a*x + b (mod p)."""
    max_attempts = 100
    for _ in range(max_attempts):
        x = random.randint(0, p-1)
        # Compute y^2 = x^3 + a*x + b mod p
        y_squared = (x**3 + a*x + b) % p

        # Check if y_squared is a quadratic residue
        for y in range(p):
            if (y * y) % p == y_squared:
                return (x, y)

    # If no point found, return a simple point that might work
    return (random.randint(1, p-1), random.randint(1, p-1))


def main():
    """Main function to demonstrate elliptic curve point addition."""
    print("Elliptic Curve Point Addition")
    print("=" * 50)
    print("Options:")
    print("  'd' - Use default values")
    print("  'r' - Use random values")
    print("  'm' - Manual input")
    print("=" * 50)

    try:
        mode = input("Choose mode (d/r/m): ").strip().lower()

        if mode == 'd':
            # Default values
            p = 11
            a = 1
            b = 6
            P = (2, 7)
            Q = (5, 2)
            print("\nUsing default values:")
            print(f"  p = {p}")
            print(f"  a = {a}, b = {b}")
            print(f"  P = {P}")
            print(f"  Q = {Q}")

        elif mode == 'r':
            # Random values
            p = get_random_prime()
            a = random.randint(0, p-1)
            b = random.randint(1, p-1)  # b != 0 for non-singular curve

            # Generate random points
            P = generate_random_point(p, a, b)
            Q = generate_random_point(p, a, b)

            # Sometimes make one point the point at infinity
            if random.random() < 0.1:
                if random.random() < 0.5:
                    P = O
                else:
                    Q = O

            print("\nUsing random values:")
            print(f"  p = {p}")
            print(f"  a = {a}, b = {b}")
            print(f"  P = {P}")
            print(f"  Q = {Q}")

        elif mode == 'm':
            # Manual input
            print("\nManual input mode:")
            p = int(input("Enter prime modulus p: "))
            a = int(input("Enter curve parameter a: "))
            b = int(input("Enter curve parameter b: "))

            # Get point P
            print("\nEnter point P (x,y) or 'O' for point at infinity:")
            p_input = input("P: ").strip()
            if p_input.upper() == 'O':
                P = O
            else:
                x1, y1 = map(int, p_input.replace('(', '').replace(')', '').split(','))
                P = (x1, y1)

            # Get point Q
            print("\nEnter point Q (x,y) or 'O' for point at infinity:")
            q_input = input("Q: ").strip()
            if q_input.upper() == 'O':
                Q = O
            else:
                x2, y2 = map(int, q_input.replace('(', '').replace(')', '').split(','))
                Q = (x2, y2)

        else:
            print("Invalid mode selected. Using defaults.")
            p, a, b = 11, 1, 6
            P, Q = (2, 7), (5, 2)

        print(f"\nCurve: y^2 = x^3 + {a}*x + {b} (mod {p})")

        # Perform addition
        result = point_add(P, Q, a, b, p)

        if result is not None:
            print(f"\nFinal result: P + Q = {result}")
        else:
            print("\nAddition failed (possibly due to invalid inverse).")

    except ValueError as e:
        print(f"Error: Invalid input. {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
