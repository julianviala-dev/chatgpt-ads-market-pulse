# Architecture

## Separation of responsibilities
**Semantic/agent layer:** discovery, first-hand classification, experience extraction, claim extraction, duplicate hypotheses, theme naming, root-cause hypothesis, Battlecard wording.

**Deterministic layer:** validation, tier weights, dedupe enforcement, prevalence counts, recency, Tier 3 cap, Market Temperature, confidence, sorting, rendering checks.

**Presentation layer:** locked V13 email template. It consumes structured output only.

## Data flow
```text
approved sources
  ↓
raw evidence archive
  ↓
experience + claim extraction
  ↓
qualification + dedupe
  ↓
evidence ledger
  ↓
deterministic scoring / prevalence / confidence
  ↓                         official OpenAI sources
market themes                    ↓
  ↓                       product intelligence
root-cause diagnosis             ↓
  └──────────────→ battlecards ←─┘
                    ↓
                 V13 email
                    ↓
                    QA
```

## Production boundary
Source acquisition and distribution sit behind adapters. A company can connect approved search/browser, social listening, data warehouse or mail systems without modifying methodology/scoring.
