def dedupe_experiences(records: list[dict]) -> list[dict]:
    """For prevalence, an experience counts once even when it has multiple claims/sources."""
    out={}
    for r in records:
        if r.get("product_intelligence"): continue
        out.setdefault(r["experience_id"], r)
    return list(out.values())

def confidence(records: list[dict]) -> str:
    ex=dedupe_experiences(records)
    n=len(ex)
    families=len({r.get("source_family") for r in ex if r.get("source_family")})
    strong=sum(1 for r in ex if int(r.get("tier",3)) <= 2)
    if n >= 8 and families >= 3 and strong >= 4: return "HIGH"
    if n >= 4 and families >= 2 and strong >= 2: return "MEDIUM"
    return "LOW"
