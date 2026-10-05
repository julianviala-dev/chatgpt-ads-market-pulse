import yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_author_config_locked():
    c=yaml.safe_load((ROOT/'config/pulse.yaml').read_text()); assert c['author']['locked'] is True and c['author']['name']=='Julian Viala'
def test_distribution_off_by_default():
    c=yaml.safe_load((ROOT/'config/pulse.yaml').read_text()); assert c['distribution']['enabled'] is False
def test_tier3_cap():
    c=yaml.safe_load((ROOT/'config/scoring.yaml').read_text()); assert c['tier3_effective_weight_cap']<=0.20
