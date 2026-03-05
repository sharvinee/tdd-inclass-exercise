import argparse
import json
from clinical_risk.risk_scores import qsofa_score, cha2ds2_vasc_score


def _to_bool(value: str) -> bool:
    return value.lower() in {"true", "1", "yes", "y"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="clinical_risk")
    subparsers = parser.add_subparsers(dest="command", required=True)

    risk = subparsers.add_parser("risk")
    risk_sub = risk.add_subparsers(dest="score", required=True)

    q = risk_sub.add_parser("qsofa")
    q.add_argument("--rr", type=int, required=True)
    q.add_argument("--sbp", type=int, required=True)
    q.add_argument("--ams", required=True)

    c = risk_sub.add_parser("chadsvasc")
    c.add_argument("--age", type=int, required=True)
    c.add_argument("--female", required=True)
    c.add_argument("--chf", required=True)
    c.add_argument("--htn", required=True)
    c.add_argument("--dm", required=True)
    c.add_argument("--stroke", required=True)
    c.add_argument("--vascular", required=True)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.score == "qsofa":
        score = qsofa_score(
            args.rr,
            args.sbp,
            _to_bool(args.ams),
        )
        print(json.dumps({"name": "qSOFA", "score": score}))
        return 0

    if args.score == "chadsvasc":
        score = cha2ds2_vasc_score(
            age=args.age,
            female=_to_bool(args.female),
            chf=_to_bool(args.chf),
            htn=_to_bool(args.htn),
            dm=_to_bool(args.dm),
            stroke=_to_bool(args.stroke),
            vascular=_to_bool(args.vascular),
        )
        print(json.dumps({"name": "CHA2DS2-VASc", "score": score}))
        return 0

    return 1