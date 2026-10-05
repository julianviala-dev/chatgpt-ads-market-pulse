# Adapter contract

The core repo intentionally does not scrape LinkedIn, Reddit or arbitrary websites. Acquisition is environment-specific and must comply with the operator's approved tools and data policies.

## Evidence adapter
An adapter returns a list conforming to schemas/evidence.schema.json. It may be backed by an approved browser/search agent, social-listening system, warehouse, API or manually reviewed evidence ledger.

## Product adapter
Refreshes official OpenAI product intelligence from config/product_sources.yaml. Its output must never enter sentiment scoring.

## Mail adapter
Distribution is downstream of a successful build and explicit approval. Credentials belong in a secrets manager, not this repository.

## Codex/ChatGPT
When an interactive agent has web/search access, use prompts/DISCOVERY.md for acquisition, write the resulting ledger to a run directory, validate it, then invoke the deterministic engine.
