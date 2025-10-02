# hnum.py – Harmonic Number Model v0.8
# CC0 – October 02, 2025

class MeasureBundle:
    def __init__(self, units=None):
        if isinstance(units, MeasureBundle):
            self.units = units.units
        else:
            self.units = units or {}

    def __eq__(self, other):
        if not isinstance(other, MeasureBundle): return False
        return self.units == other.units

    def compose(self, other):
        composed = self.units.copy()
        for k, v in other.units.items():
            composed[k] = composed.get(k, 0) + v
        return MeasureBundle(composed)

    def inverse(self):
        return MeasureBundle({k: -v for k, v in self.units.items()})

    def __str__(self):
        if not self.units: return '[]'
        parts = [k if v == 1 else f'{k}^{v}' if v > 0 else f'{k}^-1' if v == -1 else f'{k}^{v}' 
                 for k, v in self.units.items() if v != 0]
        return '[' + ' '.join(parts) + ']'


class HNum:
    def __init__(self, mag=0, measure=None, flags=0, epsilon=0.0):
        self.mag = mag
        self.measure = MeasureBundle(measure) if not isinstance(measure, MeasureBundle) else measure
        self.flags = flags  # 1: ⊘ (pause), 2: ∥ (diverge)
        self.epsilon = epsilon

    @property
    def is_pause(self): return bool(self.flags & 1)
    @property
    def is_diverge(self): return bool(self.flags & 2)

    def __str__(self):
        if self.is_diverge: return f'∥ {self.measure}'
        if self.is_pause: return f'⊘ {self.measure}'
        sign = '-' if self.mag < 0 else ''
        mag_str = f'{abs(self.mag):g}' if self.mag != 0 else '⊘'
        return f'{sign}{mag_str} {self.measure}'

    @classmethod
    def pause(cls, measure=None): return cls(0, measure, flags=1)
    @classmethod
    def diverge(cls, measure=None): return cls(0, measure, flags=2)
    @classmethod
    def opposite(cls, other): return cls(-other.mag, other.measure, other.flags, other.epsilon)

    def hadd(self, other):
        if self.measure != other.measure: return HNum(flags=1)
        if self.is_pause and other.is_pause: return HNum.pause(self.measure)
        if self.is_pause: return other
        if other.is_pause: return self
        if self.is_diverge or other.is_diverge: return HNum.diverge(self.measure)
        return HNum(self.mag + other.mag, self.measure)

    def hmult(self, other):
        if self.is_pause or other.is_pause: return HNum.pause()
        if self.is_diverge or other.is_diverge: return HNum.diverge()
        return HNum(self.mag * other.mag, self.measure.compose(other.measure))

    def hinvert(self):
        if self.is_pause or abs(self.mag) < 1e-10: return HNum.diverge()
        return HNum(1 / self.mag, self.measure.inverse())
