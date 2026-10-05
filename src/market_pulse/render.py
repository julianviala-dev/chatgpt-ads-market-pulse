from pathlib import Path
from html import escape
import re

def render(base_html: Path, output: Path, temperature: float, confidence: str) -> None:
    html=base_html.read_text()
    html=re.sub(r'4\.1\s*<span style="font-size:28px;color:#8e8e93">/ 10</span>', f'{temperature:.1f} <span style="font-size:28px;color:#8e8e93">/ 10</span>', html, count=1)
    html=re.sub(r'EVIDENCE CONFIDENCE · LOW', f'EVIDENCE CONFIDENCE · {escape(confidence)}', html, count=1)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(html)
