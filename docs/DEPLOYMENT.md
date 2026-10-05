# Deployment

## Local
```bash
./scripts/setup
./scripts/pulse validate
./scripts/pulse demo
```

## GitHub Actions
`ci.yml` validates every push/PR. `build-pulse.yml` is manual (`workflow_dispatch`) and builds the demo artifact. It does not scrape sources or send email.

## Production adapters
Implement an adapter that outputs the evidence schema. Store credentials only in your environment/secrets manager. Never commit tokens or raw private advertiser data.

## Distribution
Email distribution is intentionally disabled in this public PoC. Add a mail adapter only after your organization approves destination, credentials and review process. Keep a human approval gate for distribution.
