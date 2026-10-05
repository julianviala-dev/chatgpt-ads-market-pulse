from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
h=(ROOT/'templates/v13/email.html').read_text()
def test_author_locked():
    assert 'Julian Viala' in h and 'https://www.linkedin.com/in/julian-viala/' in h
def test_sections():
    for s in ['01 · MARKET READ','02 · MARKET SIGNALS','03 · CSM BATTLECARDS','04 · PRODUCT &amp; GTM PRIORITIES','05 · METHODOLOGY']: assert s in h
def test_methodology_clear():
    assert 'independent advertiser experiences rather than counted as posts' in h
    assert 'never influence market sentiment' in h
def test_no_em_dash(): assert '—' not in h
def test_source_links_present(): assert h.count('href=') >= 8
