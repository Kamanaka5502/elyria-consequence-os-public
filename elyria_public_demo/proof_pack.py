from __future__ import annotations

from elyria_public_demo.cli import invalid_demo, valid_demo
from elyria_public_demo.core import PublicConsequenceGate


def run() -> dict:
    gate = PublicConsequenceGate()

    valid = gate.evaluate(valid_demo())
    invalid = gate.evaluate(invalid_demo())

    missing_replay = valid_demo()
    missing_replay["replay"]["legitimacy_verified"] = False
    halted = gate.evaluate(missing_replay)

    repeated = gate.evaluate(valid_demo())

    checks = {
        "valid_executes": valid.decision == "EXECUTE" and valid.effect_bound is True,
        "invalid_custody_refuses": invalid.decision == "REFUSE" and invalid.effect_bound is False,
        "missing_replay_halts": halted.decision == "HALT" and halted.effect_bound is False,
        "receipt_is_deterministic": valid.receipt_hash == repeated.receipt_hash,
    }

    return {
        "ok": all(checks.values()),
        "checks": checks,
        "valid_receipt_hash": valid.receipt_hash,
        "invalid_receipt_hash": invalid.receipt_hash,
        "halt_receipt_hash": halted.receipt_hash,
    }


if __name__ == "__main__":
    import json
    import sys

    result = run()
    print(json.dumps(result, sort_keys=True, indent=2))
    raise SystemExit(0 if result["ok"] else 1)
