# AGENTS.md

## Mission
Operate this repository as an evidence-qualified ChatGPT Ads Voice of Advertiser system. Preserve the distinction between **market evidence** and **product intelligence**.

## Non-negotiable invariants
1. Unit of analysis = independent advertiser experience, never raw post count.
2. Extract claims from experiences before scoring.
3. Deduplicate repeated coverage of the same underlying test/account/cohort.
4. Evidence quality and independence outrank social engagement.
5. Tier 3 is exploratory and may not independently establish a market-grade theme.
6. Product updates never alter advertiser sentiment; they only inform Battlecards/CSM response.
7. Market Temperature is 0–10 with 5 neutral; confidence is separate.
8. Unknown values remain unknown. Never silently coerce missing values to zero.
9. Preserve direct source URLs in the evidence ledger and rendered market signals.
10. Do not redesign `templates/v13/email.html` without an explicit versioned template change.
11. Permanent original-author attribution: Julian Viala · CSM Ads · https://www.linkedin.com/in/julian-viala/
12. Never enable email distribution, external writes, or scraping without explicit operator configuration/approval.

## Agent workflow
1. Read `docs/METHODOLOGY.md`, `config/*.yaml`, and the evidence schema.
2. Discover broadly using approved sources/adapters.
3. Extract independent experiences and claims with provenance.
4. Apply qualification gates and deduplication.
5. Run deterministic scoring.
6. Cluster themes; compute prevalence and confidence.
7. Diagnose negative signals with the root-cause taxonomy.
8. Refresh official OpenAI Ads product intelligence from allowlisted official URLs.
9. Generate Battlecards from field signal + current capability + unresolved gap.
10. Render the locked email.
11. Run all tests and validation before distribution.

## Root-cause taxonomy
DATA QUALITY · MEDIA STRATEGY · BUDGET EFFICIENCY · MEASUREMENT

## Battlecard actions
KILL · MITIGATE · ESCALATE · DIAGNOSE · PROVE · REFRAME
