from client import ZXGraphRewriter

def main():
    print("=== Testing ZX-Calculus Graph Rewriter ===")
    zx = ZXGraphRewriter()
    z1 = zx.add_spider('Z', 0.5)
    z2 = zx.add_spider('Z', 1.0)
    zx.add_edge(z1, z2)

    print(f"Initial spiders count: {len(zx.nodes)}")
    fused = zx.spider_fusion()
    print(f"Spider fusion applied: {fused}. Remaining count: {len(zx.nodes)}")
    assert len(zx.nodes) == 1
    rem = list(zx.nodes.values())[0]
    print(f"Fused spider phase: {rem['phase']}")
    assert abs(rem['phase'] - 1.5) < 1e-5
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
