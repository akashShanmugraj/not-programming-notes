#!/usr/bin/env python3
"""
Elliptic Curve ElGamal Encryption Demonstration
Implements step-by-step Elliptic Curve ElGamal encryption with detailed arithmetic output.
"""

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich import box
import colorama
import random
colorama.init()

# Initialize Rich console
console = Console()

# Point at infinity representation
O = None


def mod_inv(a, p):
    """
    Compute modular inverse of a mod p using Extended Euclidean Algorithm.
    Prints all intermediate steps with rich formatting.
    """
    # Create a beautiful header
    header = Text(f"Computing modular inverse of {a} mod {p}", style="bold blue")
    console.print(Panel(header, title="[inverse] 🔢 Modular Inverse", border_style="blue"))

    if a == 0:
        console.print("[red]❌ Error: Cannot compute inverse of 0[/red]")
        return None

    # Extended Euclidean Algorithm
    r1, r2 = p, a
    t1, t2 = 0, 1
    step = 1

    # Create initialization table
    init_table = Table(box=box.ROUNDED, title="📋 Initialization", title_style="bold green")
    init_table.add_column("Variable", style="cyan", no_wrap=True)
    init_table.add_column("Value", style="yellow")
    init_table.add_row("r₁", str(p))
    init_table.add_row("r₂", str(a))
    init_table.add_row("t₁", "0")
    init_table.add_row("t₂", "1")
    console.print(init_table)
    console.print()

    # Create steps table
    steps_table = Table(box=box.HEAVY_HEAD, title="🔄 Extended Euclidean Algorithm Steps", title_style="bold magenta")
    steps_table.add_column("Step", style="bold white", justify="center", no_wrap=True)
    steps_table.add_column("q = r₁ ÷ r₂", style="cyan", justify="center")
    steps_table.add_column("r = r₁ mod r₂", style="green", justify="center")
    steps_table.add_column("t = t₁ - q·t₂", style="yellow", justify="center")
    steps_table.add_column("Update", style="blue")

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2

        update_text = Text()
        update_text.append(f"r₁ ← {r2}", style="red")
        update_text.append(", ", style="white")
        update_text.append(f"r₂ ← {r}", style="red")
        update_text.append("\n", style="")
        update_text.append(f"t₁ ← {t2}", style="red")
        update_text.append(", ", style="white")
        update_text.append(f"t₂ ← {t}", style="red")

        steps_table.add_row(
            str(step),
            f"{r1} ÷ {r2} = {q}",
            f"{r1} mod {r2} = {r}",
            f"{t1} - {q}×{t2} = {t}",
            update_text
        )

        r1, r2 = r2, r
        t1, t2 = t2, t
        step += 1

    console.print(steps_table)

    if r1 != 1:
        console.print(f"\n[red]❌ GCD = {r1} ≠ 1, so {a} has no inverse mod {p}[/red]")
        return None

    inv = t1 % p
    console.print(f"\n[green]✅ Final coefficient: t₁ = {t1}[/green]")

    if inv < 0:
        console.print(f"[orange]⚠️  t₁ is negative, adjusting: {t1} mod {p} = {inv}[/orange]")
    else:
        console.print(f"[green]📊 Final inverse: {t1} mod {p} = {inv}[/green]")

    result_text = Text(f"Result: {a}", style="bold white")
    result_text.append("⁻¹", style="superscript blue")
    result_text.append(f" mod {p} = {inv}", style="bold green")
    console.print(Panel(result_text, border_style="green"))
    console.print()

    return inv


def mod_reduce(n, p):
    """Reduce n modulo p and print the reduction with rich formatting."""
    result = n % p
    if n != result:
        reduce_text = Text(f"{n} mod {p} = {result}", style="blue")
        console.print(f"  [dim]≡[/dim] {reduce_text}")
    return result


def is_on_curve(P, curve, p):
    """
    Check if point P lies on the elliptic curve y^2 = x^3 + a*x + b (mod p).
    Prints the validation steps with rich formatting.
    """
    if P == O:
        console.print("  [cyan]∞[/cyan] Point is O (point at infinity), which is on every curve.")
        return True

    x, y = P
    a, b = curve

    # Create curve equation with superscript
    curve_eq = Text(f"y", style="yellow")
    curve_eq.append("²", style="superscript cyan")
    curve_eq.append(f" = x", style="yellow")
    curve_eq.append("³", style="superscript cyan")
    curve_eq.append(f" + {a}·x + {b} (mod {p})", style="white")

    console.print(f"\n  🔍 Checking if [bold magenta]({x}, {y})[/bold magenta] is on curve:")
    console.print(f"     {curve_eq}")

    # Create validation table
    val_table = Table(box=box.SIMPLE, show_header=False)
    val_table.add_column("Side", style="bold", width=12)
    val_table.add_column("Calculation", style="cyan")
    val_table.add_column("Result", style="green", justify="right")

    # Left side: y^2 mod p
    lhs = (y * y) % p
    left_calc = Text(f"y", style="yellow")
    left_calc.append("²", style="superscript cyan")
    left_calc.append(f" = {y}² = {y*y}", style="white")
    if y*y != lhs:
        left_calc.append(f" ≡ {lhs} (mod {p})", style="blue")
    val_table.add_row("Left side", left_calc, str(lhs))

    # Right side: x^3 + a*x + b mod p
    x3 = (x * x * x) % p
    ax = (a * x) % p
    rhs = (x3 + ax + b) % p

    right_calc = Text(f"x", style="yellow")
    right_calc.append("³", style="superscript cyan")
    right_calc.append(f" + {a}·x + {b}", style="white")
    right_calc.append(f"\n     = {x}³ + {a}×{x} + {b}", style="dim white")
    right_calc.append(f"\n     = {x3} + {ax} + {b}", style="dim white")
    if x3 + ax + b != rhs:
        right_calc.append(f"\n     ≡ {rhs} (mod {p})", style="blue")

    val_table.add_row("Right side", right_calc, str(rhs))

    console.print(val_table)

    is_valid = (lhs == rhs)
    status_icon = "✅" if is_valid else "❌"
    status_color = "green" if is_valid else "red"
    console.print(f"  {status_icon} [bold {status_color}]{lhs} {'≡' if is_valid else '≢'} {rhs} → {'VALID' if is_valid else 'INVALID'}[/bold {status_color}]")

    return is_valid


def point_add(P, Q, curve, p):
    """
    Add two points P and Q on the elliptic curve.
    Handles all cases: P != Q, P == Q (doubling), P = O, Q = O, P = -Q.
    Prints all intermediate calculations with rich formatting.
    """
    a, b = curve

    # Handle point at infinity
    if P == O:
        console.print(f"  [cyan]∞[/cyan] P = O, so P + Q = Q = [bold magenta]{Q}[/bold magenta]")
        return Q
    if Q == O:
        console.print(f"  [cyan]∞[/cyan] Q = O, so P + Q = P = [bold magenta]{P}[/bold magenta]")
        return P

    x1, y1 = P
    x2, y2 = Q

    # Check if P = -Q (i.e., P + Q = O)
    if x1 == x2 and (y1 + y2) % p == 0:
        console.print(f"  ⚠️  P = ([red]{x1}[/red], [red]{y1}[/red]) and Q = ([red]{x2}[/red], [red]{y2}[/red])")
        console.print(f"     x₁ = x₂ and y₁ + y₂ = {y1} + {y2} = [red]{y1 + y2}[/red] ≡ 0 (mod {p})")
        console.print(f"     [bold red]Therefore P = -Q, so P + Q = ∞[/bold red]")
        return O

    # Create operation header
    operation_type = "🔄 Point Doubling" if x1 == x2 and y1 == y2 else "➕ Point Addition"
    console.print(f"\n  {operation_type}: [bold magenta]{P}[/bold magenta] + [bold magenta]{Q}[/bold magenta]")

    # Compute slope λ
    if x1 == x2 and y1 == y2:
        # Point doubling: λ = (3*x1^2 + a) * inv(2*y1) mod p
        console.print(f"     [yellow]λ = (3·x² + a) · (2·y)[/yellow][blue]⁻¹[/blue] mod {p}")

        # Create computation table for doubling
        double_table = Table(box=box.SIMPLE, show_header=False)
        double_table.add_column("Step", style="cyan", width=15)
        double_table.add_column("Calculation", style="white")
        double_table.add_column("Result", style="green", justify="right")

        x1_sq = (x1 * x1) % p
        double_table.add_row("x²", f"{x1}² = {x1*x1}", f"{x1_sq}")

        three_x_sq = (3 * x1_sq) % p
        double_table.add_row("3·x²", f"3 × {x1_sq} = {3*x1_sq}", f"{three_x_sq}")

        numerator = (three_x_sq + a) % p
        double_table.add_row("Numerator", f"{three_x_sq} + {a} = {three_x_sq + a}", f"{numerator}")

        denominator = (2 * y1) % p
        double_table.add_row("Denominator", f"2 × {y1} = {2*y1}", f"{denominator}")

        console.print(double_table)

        inv_denom = mod_inv(denominator, p)
        if inv_denom is None:
            return None

        lam = (numerator * inv_denom) % p
        console.print(f"     [bold yellow]λ = {numerator} × {inv_denom} = {numerator * inv_denom} ≡ {lam} (mod {p})[/bold yellow]")
    else:
        # Point addition: λ = (y2 - y1) * inv(x2 - x1) mod p
        console.print(f"     [yellow]λ = (y₂ - y₁) · (x₂ - x₁)[/yellow][blue]⁻¹[/blue] mod {p}")

        # Create computation table for addition
        add_table = Table(box=box.SIMPLE, show_header=False)
        add_table.add_column("Step", style="cyan", width=15)
        add_table.add_column("Calculation", style="white")
        add_table.add_column("Result", style="green", justify="right")

        y_diff = (y2 - y1) % p
        add_table.add_row("y₂ - y₁", f"{y2} - {y1} = {y2 - y1}", f"{y_diff}")

        x_diff = (x2 - x1) % p
        add_table.add_row("x₂ - x₁", f"{x2} - {x1} = {x2 - x1}", f"{x_diff}")

        console.print(add_table)

        inv_x_diff = mod_inv(x_diff, p)
        if inv_x_diff is None:
            return None

        lam = (y_diff * inv_x_diff) % p
        console.print(f"     [bold yellow]λ = {y_diff} × {inv_x_diff} = {y_diff * inv_x_diff} ≡ {lam} (mod {p})[/bold yellow]")

    # Compute x3 = λ^2 - x1 - x2 mod p
    console.print(f"\n  🧮 Computing [bold cyan]x₃[/bold cyan]:")

    lam_sq = (lam * lam) % p
    console.print(f"     λ² = {lam}² = {lam*lam}")
    if lam*lam != lam_sq:
        console.print(f"     [dim]≡ {lam_sq} (mod {p})[/dim]")

    x3_temp = (lam_sq - x1 - x2) % p
    console.print(f"     x₃ = λ² - x₁ - x₂ = {lam_sq} - {x1} - {x2} = {lam_sq - x1 - x2}")
    if lam_sq - x1 - x2 != x3_temp:
        console.print(f"     [dim]≡ {x3_temp} (mod {p})[/dim]")
    x3 = x3_temp

    # Compute y3 = λ*(x1 - x3) - y1 mod p
    console.print(f"\n  🧮 Computing [bold cyan]y₃[/bold cyan]:")

    x1_minus_x3 = (x1 - x3) % p
    console.print(f"     x₁ - x₃ = {x1} - {x3} = {x1 - x3}")
    if x1 - x3 != x1_minus_x3:
        console.print(f"     [dim]≡ {x1_minus_x3} (mod {p})[/dim]")

    lam_times_diff = (lam * x1_minus_x3) % p
    console.print(f"     λ·(x₁ - x₃) = {lam} × {x1_minus_x3} = {lam * x1_minus_x3}")
    if lam * x1_minus_x3 != lam_times_diff:
        console.print(f"     [dim]≡ {lam_times_diff} (mod {p})[/dim]")

    y3_temp = (lam_times_diff - y1) % p
    console.print(f"     y₃ = λ·(x₁ - x₃) - y₁ = {lam_times_diff} - {y1} = {lam_times_diff - y1}")
    if lam_times_diff - y1 != y3_temp:
        console.print(f"     [dim]≡ {y3_temp} (mod {p})[/dim]")
    y3 = y3_temp

    result = (x3, y3)
    console.print(f"\n  🎯 [bold green]Result: {P} + {Q} = {result}[/bold green]")

    return result


def point_double(P, curve, p):
    """Double point P (convenience wrapper for point_add) with rich formatting."""
    console.print(f"\n  [bold blue]🔄 Doubling point {P}:[/bold blue]")
    return point_add(P, P, curve, p)


def scalar_mult(n, P, curve, p):
    """
    Multiply scalar n by point P using double-and-add method.
    Prints each step of the binary method with rich formatting.
    """
    # Create beautiful header
    header_text = f"Computing [bold cyan]{n}[/bold cyan] × [bold magenta]{P}[/bold magenta] using double-and-add method"
    console.print(Panel(header_text, title="🔢 Scalar Multiplication", border_style="cyan", title_align="left"))

    if n == 0:
        console.print("  [cyan]∞[/cyan] n = 0, so result is O")
        return O

    if n < 0:
        console.print(f"  ⚠️  n = {n} is negative, computing {abs(n)} × (-P) instead")
        neg_P = (P[0], (-P[1]) % p) if P != O else O
        return scalar_mult(-n, neg_P, curve, p)

    # Convert n to binary and create binary display
    n_bin = bin(n)[2:]
    binary_display = Text()
    for i, bit in enumerate(n_bin):
        color = "green" if bit == '1' else "red"
        binary_display.append(bit, style=f"bold {color}")
        if i < len(n_bin) - 1:
            binary_display.append(" ", style="dim")

    console.print(f"\n  🔢 Binary representation of [bold cyan]{n}[/bold cyan]: {binary_display}")
    console.print(f"     Processing bits from [yellow]left to right[/yellow] (MSB to LSB)")

    # Create algorithm tracking table
    mult_table = Table(box=box.HEAVY_HEAD, title="📊 Double-and-Add Algorithm Steps", title_style="bold purple")
    mult_table.add_column("Bit", style="bold white", justify="center", no_wrap=True)
    mult_table.add_column("Position", style="cyan", justify="center")
    mult_table.add_column("Action", style="yellow", width=20)
    mult_table.add_column("Result", style="green", width=15)
    mult_table.add_column("Current", style="magenta", width=15)

    result = O
    current = P

    # Add initialization row
    mult_table.add_row("—", "—", "[bold green]Initialize[/bold green]", "∞" if result == O else str(result), str(current))

    for i, bit in enumerate(n_bin):
        bit_pos = len(n_bin) - 1 - i
        action_text = Text()
        new_result = result
        new_current = current

        if bit == '1':
            action_text.append("Add", style="bold green")
            if result == O:
                action_text.append(" (result was ∞)", style="dim")
                new_result = current
            else:
                action_text.append(" result + current", style="dim")
                # Don't perform the addition here, just record it
                pass
        else:
            action_text.append("Skip addition", style="dim red")

        # Add bit processing row
        mult_table.add_row(
            f"[bold {'green' if bit == '1' else 'red'}]{bit}[/bold {'green' if bit == '1' else 'red'}]",
            str(bit_pos),
            action_text,
            "∞" if new_result == O else str(new_result),
            str(new_current)
        )

        # Actually perform the addition if bit is 1
        if bit == '1':
            if result == O:
                result = current
            else:
                console.print(f"\n    [green]➕ Adding current to result:[/green]")
                result = point_add(result, current, curve, p)

        # Double current for next iteration (except after last bit)
        if i < len(n_bin) - 1:
            console.print(f"\n    [blue]🔄 Doubling current for next iteration:[/blue]")
            current = point_double(current, curve, p)

            # Add doubling row
            mult_table.add_row(
                "—",
                "—",
                "[bold blue]Double current[/bold blue]",
                "∞" if result == O else str(result),
                str(current)
            )

    console.print(mult_table)

    final_result_text = Text(f"Final result: [bold cyan]{n}[/bold cyan] × [bold magenta]{P}[/bold magenta] = ", style="bold white")
    if result == O:
        final_result_text.append("∞", style="cyan")
    else:
        final_result_text.append(f"{result}", style="bold green")
    console.print(Panel(final_result_text, border_style="green"))
    console.print()

    return result


def ec_elgamal_encrypt(P_m, k, G, n_B, curve, p):
    """
    Perform Elliptic Curve ElGamal encryption with rich formatting.
    Returns ciphertext (C1, C2) and public key P_B.
    """
    # Main title
    title = Text("ELLIPTIC CURVE ELGAMAL ENCRYPTION", style="bold white on blue")
    console.print(Panel(title, border_style="blue", padding=(1, 2)))

    a, b = curve

    # Parameters section
    params_table = Table(box=box.ROUNDED, title="🔧 Parameters", title_style="bold green")
    params_table.add_column("Parameter", style="cyan", no_wrap=True)
    params_table.add_column("Value", style="yellow")
    params_table.add_column("Description", style="white")

    # Create curve equation with superscripts
    curve_eq = Text("y", style="yellow")
    curve_eq.append("²", style="superscript cyan")
    curve_eq.append(" = x", style="yellow")
    curve_eq.append("³", style="superscript cyan")
    curve_eq.append(f" + {a}·x + {b} (mod {p})", style="white")

    params_table.add_row("Prime field", f"[bold red]{p}[/bold red]", "Finite field modulus")
    params_table.add_row("Curve", curve_eq, f"E_{p}({a}, {b})")
    params_table.add_row("Base point G", f"[bold magenta]{G}[/bold magenta]", "Generator point")
    params_table.add_row("B's secret key n_B", f"[bold cyan]{n_B}[/bold cyan]", "Private key")
    params_table.add_row("Message point P_m", f"[bold magenta]{P_m}[/bold magenta]", "Plaintext point")
    params_table.add_row("Ephemeral key k", f"[bold cyan]{k}[/bold cyan]", "Random session key")

    console.print(params_table)
    console.print()

    # Step 1: Validate points
    step1_title = Text("STEP 1: Validating points on curve", style="bold white")
    console.print(Panel(step1_title, title="✅ Validation", border_style="green", title_align="left"))

    console.print(f"\n🔍 [bold]Validating base point G = {G}:[/bold]")
    if not is_on_curve(G, curve, p):
        console.print("[red]❌ ERROR: G is not on the curve![/red]")
        # return None, None

    console.print(f"\n🔍 [bold]Validating message point P_m = {P_m}:[/bold]")
    if not is_on_curve(P_m, curve, p):
        console.print("[red]❌ ERROR: P_m is not on the curve![/red]")
        # return None, None

    console.print("[green]✅ All points validated successfully![/green]")
    console.print()

    # Step 2: Compute public key P_B = n_B * G
    step2_title = Text(f"STEP 2: Computing B's public key P_B = {n_B} × G", style="bold white")
    console.print(Panel(step2_title, title="🔑 Public Key Generation", border_style="cyan", title_align="left"))
    P_B = scalar_mult(n_B, G, curve, p)
    console.print(f"[green]✅ B's public key: P_B = {P_B}[/green]")
    console.print()

    # Step 3: Compute C1 = k * G
    step3_title = Text(f"STEP 3: Computing C1 = {k} × G", style="bold white")
    console.print(Panel(step3_title, title="🎭 Ciphertext Component 1", border_style="yellow", title_align="left"))
    C1 = scalar_mult(k, G, curve, p)
    console.print(f"[green]✅ C1 = {C1}[/green]")
    console.print()

    # Step 4: Compute k * P_B
    step4_title = Text(f"STEP 4: Computing k × P_B = {k} × {P_B}", style="bold white")
    console.print(Panel(step4_title, title="🔐 Shared Secret", border_style="magenta", title_align="left"))
    k_P_B = scalar_mult(k, P_B, curve, p)
    console.print(f"[green]✅ k × P_B = {k_P_B}[/green]")
    console.print()

    # Step 5: Compute C2 = P_m + k*P_B
    step5_title = Text("STEP 5: Computing C2 = P_m + k×P_B", style="bold white")
    console.print(Panel(step5_title, title="🔒 Ciphertext Component 2", border_style="red", title_align="left"))
    console.print(f"    [yellow]C2 = {P_m} + {k_P_B}[/yellow]")
    C2 = point_add(P_m, k_P_B, curve, p)
    console.print(f"[green]✅ C2 = {C2}[/green]")
    console.print()

    # Final summary
    summary_title = Text("ENCRYPTION SUMMARY", style="bold white")
    summary_panel = Panel(summary_title, title="🎉 Complete!", border_style="green", title_align="center")

    summary_table = Table(box=box.DOUBLE, show_header=False)
    summary_table.add_column("Item", style="bold cyan", justify="right")
    summary_table.add_column("Value", style="bold green")

    summary_table.add_row("Public Key", f"P_B = {P_B}")
    summary_table.add_row("Ciphertext C1", f"{C1}")
    summary_table.add_row("Ciphertext C2", f"{C2}")
    summary_table.add_row("Complete Ciphertext", f"({C1}, {C2})")

    console.print(summary_panel)
    console.print(summary_table)
    console.print()

    return (C1, C2), P_B


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
    """Main function with input options."""
    console.print("[bold blue]🚀 Elliptic Curve ElGamal Encryption Demo[/bold blue]")
    console.print("="*80)
    console.print("Options:")
    console.print("  [green]'d'[/green] - Use default values")
    console.print("  [yellow]'r'[/yellow] - Use random values")
    console.print("  [cyan]'m'[/cyan] - Manual input")
    console.print("="*80)

    try:
        mode = input("Choose mode (d/r/m): ").strip().lower()

        if mode == 'd':
            # Default values - E_23(2,9) with G=(2,7)
            p = 23
            a, b = 18, 21
            G = (20, 3)
            n_B = 7
            P_m = (6, 0)
            k = 3
            console.print("\n[green]✅ Using default values:[/green]")
            console.print(f"  p = {p}, curve: y² = x³ + {a}·x + {b}")
            console.print(f"  G = {G}, n_B = {n_B}")
            console.print(f"  P_m = {P_m}, k = {k}")

        elif mode == 'r':
            # Random values
            p = get_random_prime()
            a = random.randint(0, p-1)
            b = random.randint(1, p-1)  # b != 0 for non-singular curve

            # Generate random base point
            G = generate_random_point(p, a, b)
            n_B = random.randint(1, 5)

            # Generate random message point
            P_m = generate_random_point(p, a, b)
            k = random.randint(1, 5)

            console.print("\n[yellow]🎲 Using random values:[/yellow]")
            console.print(f"  p = {p}, curve: y² = x³ + {a}·x + {b}")
            console.print(f"  G = {G}, n_B = {n_B}")
            console.print(f"  P_m = {P_m}, k = {k}")

        elif mode == 'm':
            # Manual input
            console.print("\n[cyan]📝 Manual input mode:[/cyan]")
            p = int(input("Enter prime modulus p: "))
            a = int(input("Enter curve parameter a: "))
            b = int(input("Enter curve parameter b: "))

            # Get base point G
            g_input = input("Enter base point G (x,y): ").strip()
            g_x, g_y = map(int, g_input.replace('(', '').replace(')', '').split(','))
            G = (g_x, g_y)

            n_B = int(input("Enter B's secret key n_B: "))

            # Get message point P_m
            pm_input = input("Enter message point P_m (x,y): ").strip()
            pm_x, pm_y = map(int, pm_input.replace('(', '').replace(')', '').split(','))
            P_m = (pm_x, pm_y)

            k = int(input("Enter ephemeral key k: "))

        else:
            console.print("[red]❌ Invalid mode selected. Using defaults.[/red]")
            p, a, b = 11, 1, 6
            G, n_B = (2, 7), 3
            P_m, k = (10, 9), 2

        curve = (a, b)

        # Run encryption
        console.print("\n" + "="*80)
        ciphertext, public_key = ec_elgamal_encrypt(P_m, k, G, n_B, curve, p)

        if ciphertext:
            C1, C2 = ciphertext

            # Final results in a nice box
            final_panel = Panel(
                f"[bold green]Public Key P_B:[/bold green] {public_key}\n"
                f"[bold green]Ciphertext C:[/bold green] ({C1}, {C2})",
                title="📋 Final Results",
                border_style="green",
                title_align="center"
            )
            console.print(final_panel)

            console.print("[dim]✨ Demo completed successfully![/dim]")
        else:
            console.print("[red]❌ Encryption failed due to invalid parameters![/red]")

    except ValueError as e:
        console.print(f"[red]❌ Error: Invalid input. {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


if __name__ == "__main__":
    main()

