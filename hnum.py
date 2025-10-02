# hnum.py – Harmonic Number Model (Seed Stub)
# Brave Codex: Harmonic Math & Kernel v0.1

class HNum:
    def __init__(self, magnitude, measure, flags=None, epsilon=None):
        self.magnitude = magnitude      # OffsetInt/IntervalRat
        self.measure = measure          # Bundle
        self.flags = flags or set()     # ⊘ (pause), ∥ (diverge)
        self.epsilon = epsilon          # Bound

    def __add__(self, other):
        if self.measure != other.measure:
            raise ValueError("Measure mismatch ⊘ error")
        return HNum(self.magnitude + other.magnitude, self.measure, self.flags | other.flags)

    def __mul__(self, other):
        return HNum(self.magnitude * other.magnitude, f"{self.measure}*{other.measure}", self.flags | other.flags)

    def inverse(self):
        if self.magnitude == 0:
            self.flags.add('⊘') # pause, not crash
            return self
        return HNum(1/self.magnitude, f"1/({self.measure})", self.flags)

    def __repr__(self):
        flag = ",".join(self.flags) if self.flags else "-"
        return f"HNum({self.magnitude}, {self.measure}, flags={flag}, ε={self.epsilon})"

# Example usage
if __name__ == "__main__":
    a = HNum(5, "kg")
    b = HNum(3, "kg")
    print(a + b)  # HNum(8, kg, ...)
    print(a * b)  # HNum(15, kg*kg, ...)
    print(a.inverse())  # HNum(0.2, 1/(kg), ...)
