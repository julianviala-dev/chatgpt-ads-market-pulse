# Methodology

## 1. Objective
Measure the direction of public advertiser/marketer experience with ChatGPT Ads while minimizing amplification of duplicated anecdotes, social reach, or vendor claims.

## 2. Unit of analysis
The core unit is an **independent advertiser experience**. A source is merely evidence. One source may contain several experiences; several sources may describe the same experience. Claims are extracted from each experience and qualified independently.

## 3. Qualification dimensions
- **Evidence quality:** first-hand status, KPIs, methodology, denominator, spend/sample.
- **Experience scale:** spend, impressions, clicks, conversions, accounts, markets, duration.
- **Independence:** whether this is genuinely another advertiser/test.
- **Market resonance:** practitioner discussion and independent references. Resonance is secondary.
- **Business impact:** importance to adoption, performance, trust or scaling.

## 4. Evidence tiers
**Tier 1:** market-grade evidence. Multi-account datasets, meaningful quantitative tests, substantial spend/sample, or credible first-hand agency aggregation with usable methodology.

**Tier 2:** corroborating evidence. Smaller first-hand quantitative tests with sufficient methodology/KPIs or multiple independently consistent experiences.

**Tier 3:** anecdotal/exploratory evidence. Isolated tests, missing methodology/denominators, generic commentary or unresolved vendor claims.

Tier 3 can inform discovery/watchlists and has reduced score influence. It cannot establish a market-grade theme alone.

## 5. Deduplication
Create a canonical experience key from advertiser/account, campaign/test, time window and source relationships. Reposts, press rewrites and commentary on the same underlying test share one experience identity. Agency cohorts are not expanded into independent votes unless underlying advertiser independence is verifiable.

## 6. Prevalence
- **ISOLATED:** 1 qualified independent advertiser/account
- **EMERGING:** 2–3
- **RECURRING:** 4–7, ideally across 2+ source families/verticals
- **BROAD:** 8+ with source/vertical diversity

These labels describe observed public evidence, not the entire advertiser population.

## 7. Market Temperature
Each assessed signal receives `sentiment ∈ {-2,-1,0,+1,+2}`.

`raw = Σ(sentiment × weight) / Σ(weight)`

`temperature = clamp(5 + 2.5 × raw, 0, 10)`

`weight = tier_weight × independence_weight × business_impact_weight × recency_weight`

Default values live in `config/scoring.yaml`.

### Tier 3 cap
All Tier 3 contribution combined is capped at 20% of effective total weight when stronger evidence exists. This lets exploratory evidence move the PoC slightly without allowing anecdotes to dominate it.

### Interpretation
0–2 Critical · 2–4 Negative · 4–6 Mixed · 6–8 Positive · 8–10 Strong

## 8. Confidence is separate
Temperature answers: **what direction does observed advertiser evidence point?**

Confidence answers: **how much evidence supports that reading?**

A small early-market sample can therefore yield `4.1/10 · LOW confidence` rather than N/A.

## 9. Root cause
Negative performance signals map to one primary diagnostic family: DATA QUALITY, MEDIA STRATEGY, BUDGET EFFICIENCY, or MEASUREMENT. Root cause remains a hypothesis unless evidence establishes causality.

## 10. Product intelligence firewall
Official OpenAI Ads capabilities are refreshed independently from allowlisted official sources. They can contextualize a field signal, provide a mitigation/proof path, and power a Battlecard. They **cannot** improve the sentiment score or mark a field problem resolved without advertiser evidence.

## 11. Battlecard contract
`FIELD SIGNAL → ROOT CAUSE → LATEST PRODUCT CAPABILITY → CSM ACTION → PRODUCT GAP → SOURCE`

Actions: KILL · MITIGATE · ESCALATE · DIAGNOSE · PROVE · REFRAME.

## 12. Coverage transparency
Every run reports actual evidence counts, unknowns and confidence. Missing data is never represented as zero.
