import sys
import json
from client import ZXGraphRewriter

def handle_call(name, arguments):
    if name == "fuse":
        p1 = arguments["phase1"]
        p2 = arguments["phase2"]
        zx = ZXGraphRewriter()
        z1 = zx.add_spider('Z', p1)
        z2 = zx.add_spider('Z', p2)
        zx.add_edge(z1, z2)
        zx.spider_fusion()
        return {"fused_phase": list(zx.nodes.values())[0]["phase"]}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
