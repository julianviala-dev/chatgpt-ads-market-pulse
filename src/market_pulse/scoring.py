from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ScoreResult:
    temperature: float
    label: str
    effective_weight: float
    tier3_share: float

def recency_weight(age_days: int, cfg: dict) -> float:
    r=cfg["recency_weight"]
    if age_days <= 7: return r["0_7_days"]
    if age_days <= 14: return r["8_14_days"]
    if age_days <= 28: return r["15_28_days"]
    return r["older"]

def label_temperature(x: float) -> str:
    if x < 2: return "CRITICAL"
    if x < 4: return "NEGATIVE"
    if x < 6: return "MIXED"
    if x < 8: return "POSITIVE"
    return "STRONG"

def compute_temperature(records: list[dict], cfg: dict) -> ScoreResult:
    records=[r for r in records if not r.get("product_intelligence", False)]
    unique={r["claim_id"]:r for r in records}.values()
    parts=[]
    for r in unique:
        w=(cfg["tier_weight"][int(r["tier"])] *
           cfg["independence_weight"][r["independence"]] *
           cfg["business_impact_weight"][r["business_impact"]] *
           recency_weight(int(r["age_days"]),cfg))
        parts.append((r,w))
    if not parts:
        return ScoreResult(5.0,"MIXED",0.0,0.0)
    non3=sum(w for r,w in parts if int(r["tier"]) != 3)
    t3=sum(w for r,w in parts if int(r["tier"]) == 3)
    cap=float(cfg["tier3_effective_weight_cap"])
    if non3 > 0:
        t3_eff=min(t3, (cap/(1-cap))*non3)
    else:
        t3_eff=min(t3, cap)
    t3_scale=(t3_eff/t3) if t3 else 1.0
    numerator=denom=0.0
    for r,w in parts:
        if int(r["tier"])==3: w*=t3_scale
        numerator += int(r["sentiment"])*w
        denom += w
    raw=numerator/denom if denom else 0.0
    temp=max(0.0,min(10.0,float(cfg["sentiment"]["neutral_temperature"])+float(cfg["sentiment"]["scale_to_temperature"])*raw))
    return ScoreResult(round(temp,1),label_temperature(temp),round(denom,4),round(t3_eff/denom if denom else 0.0,3))
