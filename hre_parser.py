import re
from hnum import HNum

_num = r"([-+]?\\d+(?:\.\\d+)?)"
_unit = r"\[([^\\]]*)\]"           # anything inside [...]
_tok  = re.compile(fr"\s*(({_num}\s*{_unit}|[\*\+]|inv)\s*)")

def eval_expr(expr: str):
    """Very tiny parser: supports 'A [u] + B [u]', 'A [u] * B [v]', and 'inv A [u]'."""
    tokens = [t[0] for t in _tok.findall(expr)]
    if not tokens: raise ValueError("Parse error")
    if tokens[0] == "inv":
        mag, unit = re.findall(fr"{_num}\s*{_unit}", " ".join(tokens[1:]))[0]
        return HNum(float(mag), unit).inverse()
    if "+" in tokens:
        left = tokens[:tokens.index("+")]
        right = tokens[tokens.index("+")+1:]
        a,u = re.findall(fr"{_num}\s*{_unit}", " ".join(left))[0]
        b,v = re.findall(fr"{_num}\s*{_unit}", " ".join(right))[0]
        return HNum(float(a), u) + HNum(float(b), v)
    if "*" in tokens:
        left = tokens[:tokens.index("*")]
        right = tokens[tokens.index("*")+1:]
        a,u = re.findall(fr"{_num}\s*{_unit}", " ".join(left))[0]
        b,v = re.findall(fr"{_num}\s*{_unit}", " ".join(right))[0]
        return HNum(float(a), u) * HNum(float(b), v)
    raise ValueError("Unsupported expression")
