# Brave Codex CLI: harmonic eval
import argparse
from hnum import HNum
def main():
    p = argparse.ArgumentParser(description="Harmonic Math demo")
    p.add_argument("--add", nargs=3, metavar=("A","UNIT","B"), help="Add A UNIT + B UNIT")
    p.add_argument("--mul", nargs=4, metavar=("A","UNITA","B","UNITB"), help="Multiply A UNITA * B UNITB")
    p.add_argument("--inv", nargs=2, metavar=("A","UNIT"), help="Inverse of A UNIT")
    args = p.parse_args()
    if args.add:
        a,u,b = args.add
        x = HNum(float(a), u); y = HNum(float(b), u)
        print(x + y); return
    if args.mul:
        a,ua,b,ub = args.mul
        x = HNum(float(a), ua); y = HNum(float(b), ub)
        print(x * y); return
    if args.inv:
        a,u = args.inv
        x = HNum(float(a), u)
        print(x.inverse()); return
    p.print_help()
if __name__ == "__main__":
    main()