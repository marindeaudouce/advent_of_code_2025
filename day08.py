import click
import numpy as np

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # already in same cluster
        
        # union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    # Read the input file
    with open(file_path) as file:
        content = file.read()

    positions = np.array([[int(x) for x in line.split(',')] for line in content.splitlines()])

    distances = dict()
    for p_idx, pos in enumerate(positions):
        nearests = np.linalg.norm(positions - pos, axis=1)
        nearests = nearests[np.where(nearests != 0)]
        for n_idx, n in enumerate(nearests):
            distances[n] = (p_idx, n_idx)
    
    # Union-Find (Disjoint Set Union) implementation
    uf = UnionFind(len(positions))
    num_clusters = len(positions)    
    for min_distance in sorted(distances.keys())[:1000]:
        x, y = distances[min_distance]
        if uf.union(x, y):
            num_clusters -= 1
            if num_clusters == 1:
                break

    # Build clusters from parent array
    clusters_dict = dict()
    for i in range(len(positions)):
        root = uf.find(i)
        if root not in clusters_dict:
            clusters_dict[root] = set()
        clusters_dict[root].add(i)
    clusters = list(clusters_dict.values())
    result = sorted(clusters, key=len)
    print(f"Output part 1: {len(result[-3]) * len(result[-2]) * len(result[-1])}")

    last_x_product = 0
    for min_distance in sorted(distances.keys()):
        x, y = distances[min_distance]
        if uf.union(x, y):
            num_clusters -= 1
            last_x_product = positions[x][0] * positions[y][0]
            if num_clusters == 1:
                break
    print(f"Output part 2: {last_x_product}")

if __name__ == "__main__":
    main()