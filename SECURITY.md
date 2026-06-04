# Security Policy

## Supported surface

This public repository contains a bounded evaluation runtime. It does not contain production secrets, private law bundles, customer corridors, protected proof corpora, or confidential deployment adapters.

## Reporting a vulnerability

Do not open a public issue for a vulnerability that could expose protected runtime behavior, credentials, or deployment details.

Report security concerns privately to the repository owners with:

- affected file or component
- reproduction steps
- expected versus observed behavior
- impact assessment
- suggested mitigation, if available

## Public security posture

The public demo is designed to fail closed:

- insufficient authority → `REFUSE`
- invalid custody → `REFUSE`
- unproven replay legitimacy → `HALT`
- missing rollback posture → `REFUSE`
- inadmissible proposal → `effect_bound = false`

Production deployments require environment-specific key management, infrastructure controls, and independent validation.
