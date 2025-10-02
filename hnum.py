# hnum.py – Harmonic Number Model (Seed Stub)
# Brave Codex: Harmonic Math & Kernel v0.1

from typing import Optional, Set

class HNum:
    def __init__(self, magnitude: float, measure: str, flags: Optional[Set[str]] = None, epsilon: Optional[float] = None):
        """
        Initialize a Harmonic Number (HNum).

        :param magnitude: The magnitude (float) of the number.
        :param measure: The unit or measure associated with the number.
        :param flags: Optional set of flags (e.g., ⊘, ∥).
        :param epsilon: Optional bound for approximation.
        """
        self.magnitude = magnitude      # OffsetInt/IntervalRat
        self.measure = measure          # Bundle
        self.flags = flags or set()     # ⊘ (pause), ∥ (diverge)
        self.epsilon = epsilon          # Bound

    def __add__(self, other: "HNum") -> "HNum":
        """Add two HNums, ensuring measure compatibility."""
        if self.measure != other.measure:
            raise ValueError(f"Measure mismatch ⊘ error: {self.measure} vs {other.measure}")
        return HNum(self.magnitude + other.magnitude, self.measure, self.flags | other.flags)

    def __mul__(self, other: "HNum") -> "HNum":
        """Multiply two HNums, combining measures."""
        return HNum(self.magnitude * other.magnitude, f"{self.measure}*{other.measure}", self.flags | other.flags)

    def inverse(self) -> "HNum":
        """Return the multiplicative inverse of the HNum."""
        if self.magnitude == 0:
            self.flags.add('⊘') # pause, not crash
            return self
        return HNum(1/self.magnitude, f"1/({self.measure})", self.flags)

    def __repr__(self) -> str:
        """Provide a string representation of the HNum."""
        flag = ",".join(self.flags) if self.flags else "-"
        return f"HNum({self.magnitude}, {self.measure}, flags={flag}, ε={self.epsilon})"

# Example usage
if __name__ == "__main__":
    a = HNum(5, "kg")
    b = HNum(3, "kg")
    print(a + b)  # HNum(8, kg, ...)
    print(a * b)  # HNum(15, kg*kg, ...)
    print(a.inverse())  # HNum(0.2, 1/(kg), ...)
