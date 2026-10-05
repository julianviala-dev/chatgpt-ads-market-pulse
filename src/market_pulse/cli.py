from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml
from jsonschema import validate
from .scoring import compute_temperature
from .quality import confidence
from .render import render

ROOT=Path(__file__).resolve().parents[2]

def load_yaml(name): return yaml.safe_load((ROOT/name).read_text())
def load_records(path): return json.loads(Path(path).read_text())

def validate_records(records):
    validate(records, json.loads((ROOT/'schemas/evidence.schema.json').read_text()))
    assert all(not r.get('product_intelligence') for r in records), 'product intelligence cannot enter evidence input'

def run(inp, out):
    records=load_records(inp); validate_records(records)
    result=compute_temperature(records,load_yaml('config/scoring.yaml'))
    conf=confidence(records)
    render(ROOT/'templates/v13/email.html',Path(out),result.temperature,conf)
    print(json.dumps({'temperature':result.temperature,'label':result.label,'confidence':conf,'tier3_share':result.tier3_share,'output':str(out)},indent=2))

def main():
    p=argparse.ArgumentParser(); sp=p.add_subparsers(dest='cmd',required=True)
    d=sp.add_parser('demo'); d.add_argument('--output',default='runs/latest/market-pulse.html')
    r=sp.add_parser('run'); r.add_argument('--input',required=True); r.add_argument('--output',default='runs/latest/market-pulse.html')
    sp.add_parser('validate')
    a=p.parse_args()
    if a.cmd=='validate':
        validate_records(load_records(ROOT/'examples/evidence/demo.json')); print('validation: OK')
    elif a.cmd=='demo': run(ROOT/'examples/evidence/demo.json',ROOT/a.output)
    else: run(a.input,a.output)
if __name__=='__main__': main()

