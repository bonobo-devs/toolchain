#!/usr/bin/python3
# Given a .bonobo file, extract the userscript code. This tool is compliant with the BUDFv1 standard.
import sys, json
if len(sys.argv) < 2: # 0th argument + .bonobo file path
    print("usage: ./unpackager.py <FILE>", file=sys.stderr)
    sys.exit(64)


with open(sys.argv[1]) as f:
    print(json.loads(f.read())["code"])
