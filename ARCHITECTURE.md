# Public Architecture

Elyria Consequence OS is a pre-effect consequence admission runtime.

The public proof surface exposes the following bounded path:

```text
proposal
→ authority validation
→ custody validation
→ replay-legitimacy validation
→ rollback validation
→ admissibility decision
→ effect boundary
→ deterministic receipt
```

The public demo intentionally excludes private law bundles, protected proof machinery, confidential adapters, and production credentials.

## Decision classes

- `EXECUTE`: the proposal is admissible and the public demo marks the effect as bound.
- `REFUSE`: the proposal is inadmissible and no effect may bind.
- `HALT`: legitimacy cannot be proven and the runtime stops the path.

## Public invariant

```text
inadmissible proposal → effect_bound = false
```

The receipt hash is deterministic for the same proposal and decision state.
