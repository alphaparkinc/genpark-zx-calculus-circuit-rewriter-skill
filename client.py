import math

class ZXGraphRewriter:
    """
    ZX-Calculus Graph Rewrite Rules.
    Spiders: Z-spider (green), X-spider (red) with phase angles.
    Rules:
    - Spider Fusion: Connected spiders of same color fuse, adding phases mod 2pi.
    """
    def __init__(self):
        self.nodes = {}
        self.next_id = 0

    def add_spider(self, stype, phase=0.0):
        nid = self.next_id
        self.next_id += 1
        self.nodes[nid] = {'type': stype, 'phase': phase % (2 * math.pi), 'neighbors': set()}
        return nid

    def add_edge(self, u, v):
        self.nodes[u]['neighbors'].add(v)
        self.nodes[v]['neighbors'].add(u)

    def spider_fusion(self):
        fused = False
        for u in list(self.nodes.keys()):
            if u not in self.nodes:
                continue
            for v in list(self.nodes[u]['neighbors']):
                if v in self.nodes and self.nodes[u]['type'] == self.nodes[v]['type']:
                    self.nodes[u]['phase'] = (self.nodes[u]['phase'] + self.nodes[v]['phase']) % (2 * math.pi)
                    self.nodes[u]['neighbors'].remove(v)
                    self.nodes[v]['neighbors'].remove(u)
                    for w in self.nodes[v]['neighbors']:
                        self.nodes[w]['neighbors'].remove(v)
                        self.nodes[w]['neighbors'].add(u)
                        self.nodes[u]['neighbors'].add(w)
                    del self.nodes[v]
                    fused = True
                    break
        return fused
