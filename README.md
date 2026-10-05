# ChatGPT Ads Market Pulse

**Evidence-qualified Voice of Advertiser intelligence for ChatGPT Ads.**

Created by **Julian Viala · CSM Ads** as a reusable proof of concept for Ads CSMs. It converts public advertiser and marketer evidence into a weekly executive Pulse, a directional **Market Temperature (0–10)**, root-cause diagnosis, current product intelligence, and CSM Battlecards.

> **Core principle:** the unit of analysis is an **independent advertiser experience, not a social post**.

## Pipeline

`discover → extract experiences → claims → qualify → deduplicate → cluster → prevalence → temperature → diagnose → product intelligence → battlecards → QA → V13 email`

Two data planes stay separate:
1. **Voice of Advertiser** determines sentiment.
2. **Official OpenAI Ads product intelligence** informs responses but **never rewrites sentiment**.

## Market Temperature

The PoC always emits **0–10**, with **5 = neutral**. Confidence is separate.

`temperature = clamp(5 + 2.5 × weighted_mean(sentiment), 0, 10)`

Signals use sentiment `[-2,+2]` weighted by evidence tier, independence, business impact and recency. Tier 3 exploratory evidence is capped so anecdotes cannot dominate.

**0–2 Critical · 2–4 Negative · 4–6 Mixed · 6–8 Positive · 8–10 Strong**

## Evidence tiers

| Tier | Meaning | Role |
|---|---|---|
| **1** | Market-grade quantitative or credible multi-account evidence | Can materially drive Pulse |
| **2** | Corroborating first-hand quantitative/independent evidence | Supports scoped findings/themes |
| **3** | Exploratory, incomplete methodology or isolated anecdote | Watchlist, reduced influence |

Engagement cannot rescue bad evidence. Duplicate coverage of one test is one experience, not multiple votes.

## Quick start

Python 3.11+:

```bash
bash scripts/setup
bash scripts/pulse validate
bash scripts/pulse demo
```

Run with your own evidence ledger:

```bash
cp .env.example .env
bash scripts/pulse run --input path/to/evidence.json
```

## Deploy with Codex / ChatGPT

Open this repo and ask:

> Set up ChatGPT Ads Market Pulse for me. Follow AGENTS.md. Preserve Julian Viala's methodology and locked V13 presentation. Configure my recipient, timezone, scan window and approved source adapters. Validate the environment, run a test Pulse, show me the output, and do not enable distribution until I approve it.

### One-prompt bootstrap

Give Codex/ChatGPT the repository URL and say:

> Deploy this Market Pulse for me. Read AGENTS.md first. Use my approved web/search capabilities for discovery, preserve the evidence methodology and V13 renderer, configure my timezone and recipient, run a preview, and ask before enabling distribution.

The agent should use `prompts/DISCOVERY.md`, `prompts/PRODUCT_INTELLIGENCE.md` and `prompts/BATTLECARDS.md`. Real acquisition remains adapter-driven rather than hidden scraping.

**Agent entry points:** [AGENTS.md](AGENTS.md) · [SKILL.md](SKILL.md) · [Methodology](docs/METHODOLOGY.md) · [Deployment](docs/DEPLOYMENT.md)

## Configuration

- `config/pulse.yaml`: operator, cadence, author lock, distribution gate
- `config/scoring.yaml`: score weights and Tier 3 cap
- `config/thresholds.yaml`: prevalence/confidence
- `config/product_sources.yaml`: official OpenAI product-source allowlist
- `schemas/evidence.schema.json`: machine-readable evidence contract
- `templates/v13/email.html`: locked executive renderer

## Deployment status

**Core pipeline:** reusable and deterministic.  
**Weekly GitHub readiness gate:** included.  
**Real discovery:** supplied through an approved EvidenceAdapter or an interactive Codex/ChatGPT session with approved search/browser access.  
**Email delivery:** deliberately requires operator-specific mail integration and approval.

See [acceptance criteria](docs/ACCEPTANCE.md) and [adapter contract](docs/ADAPTERS.md).

## Automation boundary

The public PoC includes deterministic scoring, schema validation, rendering, QA, CI and a manual GitHub Actions build. It **does not scrape social platforms or send email by default**. Source and mail adapters must be approved/configured in the deployment environment. Distribution requires human approval.

## Repository map

```text
.github/workflows/   CI + manual Pulse build
config/              methodology and operator configuration
docs/                architecture, methodology, deployment
examples/evidence/   schema-compatible demo
schemas/             evidence contract
scripts/             one-command interface
src/market_pulse/    deterministic engine
templates/v13/       locked email presentation
tests/               methodology/rendering invariants
```

## Authorship

Original concept, methodology and V13 executive presentation: **Julian Viala · CSM Ads**  
LinkedIn: https://www.linkedin.com/in/julian-viala/

MIT licensed. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
