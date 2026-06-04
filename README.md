# Elyria Consequence OS — Public Proof Surface

Elyria Consequence OS is a governed consequence runtime.

Its core question is not whether a system can generate, recommend, approve, or log an action.

Its core question is:

> Can an inadmissible action bind consequence?

This public repository presents a bounded, reviewable proof surface for that category.

## Public category definition

Elyria Consequence OS evaluates whether consequence may bind before a protected effect is allowed to execute.

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

Execution is not assumed. It is admitted.

## What this repository proves

The included public demo shows that:

- valid authority is required
- custody must be verified
- replay legitimacy must be present
- rollback posture must exist
- inadmissible proposals are refused before effect binding
- every decision produces a deterministic receipt hash

## What this repository does not disclose

This repository does not include:

- private law bundles
- customer corridor packs
- protected proof internals
- formal BAL/RPA/LPEM corpora
- hardware enforcement designs
- production keys, secrets, or credentials
- confidential deployment adapters

See [`PUBLIC_SCOPE.md`](PUBLIC_SCOPE.md).

## Quick start

```bash
python -m pip install -e .
pytest -q
python -m elyria_public_demo.cli --demo-valid
python -m elyria_public_demo.cli --demo-invalid
```

## Public demo outcomes

```text
valid proposal   → EXECUTE
invalid custody  → REFUSE
missing replay   → HALT
```

## Repository posture

This is a public evaluation and category-proof repository. It is not a claim that a demo alone constitutes a certified distributed production deployment.

Production deployment requires environment-specific validation, target infrastructure, key management, operational controls, and bounded corridor review.

## Authors

Samantha Revita  
Terry Snyder
