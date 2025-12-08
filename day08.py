import click
import numpy as np
    
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
    
    clusters = [{x} for x in range(len(positions))]
    while len(clusters) != 1:
        min_distance = np.min(list(distances.keys()))
        x, y = distances[min_distance]
        x_idx = -1
        y_idx = -1
        for idx, cluster in enumerate(clusters):
            if x in cluster and y in cluster:
                # already connected
                break
            elif x in cluster:
                x_idx = idx
                if y_idx != -1:
                    clusters[y_idx] = clusters[y_idx].union(clusters[x_idx])
                    clusters.pop(x_idx)
                    break
            elif y in cluster:
                y_idx = idx
                if x_idx != -1:
                    clusters[x_idx] = clusters[x_idx].union(clusters[y_idx])
                    clusters.pop(y_idx)
                    break
        distances.pop(min_distance)
        last_x_product = positions[x][0] * positions[y][0]

    # result = sorted(clusters, key=len)
    # print(f"Output part 1: {len(result[-3]) * len(result[-2]) * len(result[-1])}")
    print(f"Output part 2: {last_x_product}")

if __name__ == "__main__":
    main()