import yaml
from pathlib import Path
from market_pulse.scoring import compute_temperature
ROOT=Path(__file__).resolve().parents[1]
cfg=yaml.safe_load((ROOT/'config/scoring.yaml').read_text())

def rec(**kw):
    x=dict(experience_id='E',claim_id='C',source_url='https://example.com',source_family='x',tier=2,sentiment=0,independence='verified',business_impact='high',age_days=0,product_intelligence=False)
    x.update(kw); return x

def test_neutral_is_five(): assert compute_temperature([rec()],cfg).temperature==5.0
def test_positive_above_five(): assert compute_temperature([rec(sentiment=2)],cfg).temperature>5
def test_negative_below_five(): assert compute_temperature([rec(sentiment=-2)],cfg).temperature<5
def test_bounds():
    assert 0<=compute_temperature([rec(sentiment=-2)],cfg).temperature<=10
    assert 0<=compute_temperature([rec(sentiment=2)],cfg).temperature<=10
def test_tier3_capped_with_strong_evidence():
    rows=[rec(claim_id='strong',tier=1,sentiment=2)] + [rec(claim_id=f'w{i}',experience_id=f'w{i}',tier=3,sentiment=-2) for i in range(30)]
    r=compute_temperature(rows,cfg); assert r.tier3_share<=0.201 and r.temperature>5
def test_product_intelligence_excluded():
    a=rec(sentiment=1)
    p=rec(claim_id='P',sentiment=-2,product_intelligence=True,tier=1)
    assert compute_temperature([a,p],cfg).temperature==compute_temperature([a],cfg).temperature
