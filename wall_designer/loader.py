import yaml

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

def get_wall(gallery, wall_id):
    for room in gallery["gallery"]["rooms"]:
        for wall in room["walls"]:
            if wall["id"] == wall_id:
                return wall
    raise ValueError("Wall not found")

def get_artworks(art_data, ids):
    lookup = {a["id"]: a for a in art_data["art"]["artworks"]}
    return [lookup[i] for i in ids if i in lookup]
