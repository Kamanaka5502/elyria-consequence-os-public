# Elyria Consequence OS v6.1 Release Package

Correct label:

```text
Elyria Consequence OS v6.1 — Review-Repaired Local Distributed Consequence-Boundary Prototype
```

Package prepared outside the repo:

```text
elyria_consequence_os_v6_1_review_repaired.zip
SHA-256: cd6da12f93f977a765e09bd094fa43c8058bfc961d7225e37c5dc28982d91825
```

Validation completed before packaging:

```text
42 passed
CLI smoke: init, up, submit, replay, verify-chain
secret scan: no key/token patterns found
```

Repair points included:

- version alignment to `0.7.1`
- cache artifact cleanup
- HTTP API auth boundary
- OpenAPI bearer auth declaration
- independent replay reconstruction
- independent pre-effect witness quorum
- formal proof policy
- mandatory proof refusal before effect when required
- production override labeling
- claim posture correction

The ZIP should be attached as a GitHub Release artifact rather than committed as normal source history.
