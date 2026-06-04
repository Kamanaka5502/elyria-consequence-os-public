from __future__ import annotations

import argparse
import json

from elyria_public_demo.core import PublicConsequenceGate, receipt_to_dict


def valid_demo() -> dict:
    return {
        "proposal_id": "public-valid",
        "authority": {"holder": "operator", "scope": ["execute"], "revoked": False},
        "custody": {"state": "VERIFIED", "evidence_refs": ["public-demo"]},
        "replay": {"lineage_verified": True, "legitimacy_verified": True},
        "evidence": {"ticket": "PUBLIC-1", "tests": "passing"},
        "payload": {"action": "demo-effect", "rollback_plan": "restore previous state"},
    }


def invalid_demo() -> dict:
    proposal = valid_demo()
    proposal["custody"] = {"state": "RECONSTRUCTED", "evidence_refs": []}
    return proposal


def main() -> None:
    parser = argparse.ArgumentParser(prog="elyria-public-demo")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--demo-valid", action="store_true")
    group.add_argument("--demo-invalid", action="store_true")
    args = parser.parse_args()

    proposal = valid_demo() if args.demo_valid else invalid_demo()
    receipt = PublicConsequenceGate().evaluate(proposal)
    print(json.dumps(receipt_to_dict(receipt), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
