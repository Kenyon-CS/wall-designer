import argparse
import importlib.util

from wall_designer.loader import load_yaml, get_wall, get_artworks
from wall_designer.scorer import evaluate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gallery")
    parser.add_argument("--art")
    parser.add_argument("--scoring")
    parser.add_argument("--wall")
    parser.add_argument("--candidates")
    parser.add_argument("--algorithm")

    args = parser.parse_args()

    gallery = load_yaml(args.gallery)
    art = load_yaml(args.art)
    scoring = load_yaml(args.scoring)

    wall = get_wall(gallery, args.wall)
    ids = args.candidates.split(",")

    artworks = get_artworks(art, ids)

    spec = importlib.util.spec_from_file_location("algo", args.algorithm)
    algo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(algo)

    placements = algo.generate(wall, artworks, scoring)
    score = evaluate(wall, placements, scoring)

    print("\n=== RESULT ===")
    print("Wall:", args.wall)
    print("Placements:", placements)
    print("Score:", score)


if __name__ == "__main__":
    main()
