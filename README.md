# Elyria Consequence OS

<p align="center">
  <strong>Public Proof Surface for Governed Consequence Admission</strong>
</p>

<p align="center">
  <img alt="Elyria Consequence OS front page visual style" src="https://raw.githubusercontent.com/Kamanaka5502/elyria-consequence-os-public/main/assets/elyria-consequence-os-hero.svg" />
</p>

<p align="center">
  <strong>Execution is not assumed. It is admitted.</strong>
</p>

<p align="center">
  <code>v6.1 review-repaired local distributed consequence-boundary prototype</code>
</p>

---

## The Category

Most AI systems focus on generation, approval, orchestration, monitoring, or logging.

Elyria Consequence OS targets a stricter boundary:

> Can an inadmissible action bind consequence?

If the answer is yes, the system is not governing consequence. It is documenting execution.

Elyria evaluates consequence before protected effect binding.

```text
proposal
→ authority check
→ custody check
→ replay-legitimacy check
→ rollback check
→ admissibility decision
→ protected effect boundary
→ deterministic receipt
```

## Public Proof Surface

This public release demonstrates:

| Boundary | Required Condition | Fail-Closed Outcome |
|---|---|---|
| Authority | Valid holder and scope | REFUSE |
| Custody | Verified evidence state | REFUSE |
| Replay legitimacy | Lineage and legitimacy proven | HALT |
| Rollback posture | Repair path exists | REFUSE |
| Receipt | Deterministic evidence hash | Replayable proof |

## v6.1 Package

The private repaired package is checksum-bound and ready to publish as a release artifact:

```text
elyria_consequence_os_v6_1_review_repaired.zip
SHA-256: cd6da12f93f977a765e09bd094fa43c8058bfc961d7225e37c5dc28982d91825
```

Validated before packaging:

```text
42 passed
CLI smoke: init, up, submit, replay, verify-chain
secret scan: no key/token patterns found
```

Correct public label:

```text
Elyria Consequence OS v6.1 — Review-Repaired Local Distributed Consequence-Boundary Prototype
```

## Quick Start

```bash
python -m pip install -e .
python -m elyria_public_demo.proof_pack
python -m elyria_public_demo.cli --demo-valid
python -m elyria_public_demo.cli --demo-invalid
```

Expected public outcomes:

```text
valid proposal   → EXECUTE
invalid custody  → REFUSE
missing replay   → HALT
```

## Public Boundary

This repository is public-facing. It does not disclose private law bundles, customer corridors, protected proof corpora, production secrets, or confidential deployment materials.

See `PUBLIC_SCOPE.md` and `SECURITY.md`.

## Authors

Samantha Revita  
Terry Snyder
