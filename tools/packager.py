#!/usr/bin/python3
# Bonobo packaging tool to take a Bonobo TOML configuration and a userscript and produce a packaged .bonobo file.
import tomllib, json, sys

if len(sys.argv) < 3: # 0th argument + TOML + userscript
    print("usage: ./packager.py <TOML> <USERSCRIPT>", file=sys.stderr)
    sys.exit(64)

f = open(sys.argv[1], "rb")
config = tomllib.load(f)
f.close()

f = open(sys.argv[2])
userscript = f.read()
f.close()

output = {
    "BUDFVersion": 1, #config["budf"]["version"],
    "version": config["userscript"]["version"],
    "name": config["userscript"]["name"],
    "id": config["userscript"]["id"],
    "match": config["userscript"]["match"],
    "code": userscript
}

print(json.dumps(output, separators=(',', ':')))
