from market_pulse.quality import dedupe_experiences, confidence

def test_duplicate_claims_one_experience():
    rows=[{'experience_id':'E1','claim_id':'a','tier':2,'source_family':'x','product_intelligence':False},{'experience_id':'E1','claim_id':'b','tier':2,'source_family':'y','product_intelligence':False}]
    assert len(dedupe_experiences(rows))==1
    assert confidence(rows)=='LOW'
