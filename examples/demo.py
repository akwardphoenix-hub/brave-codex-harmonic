# Brave Codex: Harmonic Math & Kernel — Demo Script
# Chapter 16: The Demo That Proves Itself
# 
# This script is more than code—it's the living proof of Harmonic Math. 
# A kernel isn’t real until it runs, and harmony isn’t trusted until it survives chaos. 
# Here, we drop the candle into the dark and watch the flame steady itself.

from hnum import HNum

def demo():
    print("=== Harmonic Math Demo ===\n")

    # Normal addition: Harmony in action
    # Adding two quantities of the same unit is natural—a simple, expected truth.
    a = HNum(5, "kg")
    b = HNum(3, "kg")
    print("Add same units:", a + b)  # HNum(8, kg, ...)

    # Unit mismatch triggers ⊘ flag: Proof of safety
    # This is where the demo flexes—an impossible operation, caught and flagged.
    try:
        mismatch = a + HNum(2, "m")
        print("Mismatch add:", mismatch)
    except ValueError as e:
        print("Mismatch add caught:", e)

    # Multiplication composes measures: Building reality
    # Multiplication isn’t just math—it’s the act of composing new realities.
    c = HNum(5, "m")
    d = HNum(2, "s^-1")
    print("Multiply measures:", c * d)  # HNum(10, m*s^-1, ...)

    # Safe inverse: Bravery means handling the undefined
    # Inverting a value is risky—what happens at zero? Here, zero doesn’t crash.
    print("Inverse of 5 kg:", a.inverse())

    # Division by zero: ⊘ means pause, not death
    # The hallmark of Harmonic Math: Division by zero doesn’t crash the system.
    zero = HNum(0, "kg")
    print("Divide by ⊘:", zero.inverse())

if __name__ == "__main__":
    demo()

# Expected Output (roughly):
# === Harmonic Math Demo ===
# Add same units: HNum(8, kg, flags=-, ε=None)
# Mismatch add caught: Measure mismatch ⊘ error: kg vs m
# Multiply measures: HNum(10, m*s^-1, flags=-, ε=None)
# Inverse of 5 kg: HNum(0.2, 1/(kg), flags=-, ε=None)
# Divide by ⊘: HNum(0, kg, flags=⊘, ε=None)