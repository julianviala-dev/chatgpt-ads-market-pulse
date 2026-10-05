# Deployment acceptance criteria

A release is reusable only when all of the following hold:

- public clone works without author-local files
- CI passes on a clean GitHub runner
- demo evidence validates against the schema
- deterministic scoring emits 0–10 temperature and separate confidence
- Tier 3 cannot dominate stronger evidence
- duplicate claims do not inflate advertiser prevalence
- product intelligence cannot enter sentiment scoring
- V13 renders as one master email surface
- Julian Viala original authorship remains visible
- a new operator can configure recipient/timezone without editing methodology
- discovery uses an approved adapter and preserves direct provenance
- scheduled execution never silently fabricates evidence
- distribution remains disabled until explicitly configured/approved

The public PoC can satisfy all core/reproducibility criteria without shipping organization-specific search or mail credentials.
