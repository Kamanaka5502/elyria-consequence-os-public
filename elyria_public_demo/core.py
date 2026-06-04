from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any


class Decision(str, Enum):
    EXECUTE = "EXECUTE"
    REFUSE = "REFUSE"
    HALT = "HALT"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(value: Any) -> str:
    raw = value if isinstance(value, (bytes, bytearray)) else canonical_json(value).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class Receipt:
    decision: str
    reason: str
    proposal_hash: str
    authority_hash: str
    evidence_hash: str
    effect_bound: bool
    receipt_hash: str


class PublicConsequenceGate:
    """Bounded public proof of pre-effect consequence admission.

    This public gate intentionally exposes only a minimal category proof. It does
    not include private law bundles, production corridors, proof internals, or
    confidential deployment adapters.
    """

    def evaluate(self, proposal: dict[str, Any]) -> Receipt:
        authority = proposal.get("authority", {})
        custody = proposal.get("custody", {})
        replay = proposal.get("replay", {})
        payload = proposal.get("payload", {})
        evidence = proposal.get("evidence", {})

        decision, reason = self._decide(authority, custody, replay, payload, evidence)
        effect_bound = decision is Decision.EXECUTE

        body = {
            "decision": decision.value,
            "reason": reason,
            "proposal_hash": sha256_hex(proposal),
            "authority_hash": sha256_hex(authority),
            "evidence_hash": sha256_hex(evidence),
            "effect_bound": effect_bound,
        }
        return Receipt(**body, receipt_hash=sha256_hex(body))

    def _decide(self, authority: dict, custody: dict, replay: dict, payload: dict, evidence: dict) -> tuple[Decision, str]:
        if authority.get("revoked"):
            return Decision.REFUSE, "AUTHORITY_REVOKED"
        if not authority.get("holder") or "execute" not in authority.get("scope", []):
            return Decision.REFUSE, "AUTHORITY_INSUFFICIENT"
        if custody.get("state") != "VERIFIED" or not custody.get("evidence_refs"):
            return Decision.REFUSE, "CUSTODY_NOT_VERIFIED"
        if not replay.get("lineage_verified") or not replay.get("legitimacy_verified"):
            return Decision.HALT, "REPLAY_LEGITIMACY_UNPROVEN"
        if not payload.get("rollback_plan"):
            return Decision.REFUSE, "ROLLBACK_PLAN_MISSING"
        if not evidence:
            return Decision.REFUSE, "EVIDENCE_MISSING"
        return Decision.EXECUTE, "ADMISSIBLE"


def receipt_to_dict(receipt: Receipt) -> dict[str, Any]:
    return asdict(receipt)
