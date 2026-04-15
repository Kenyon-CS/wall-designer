import yaml

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_wall(gallery_data, wall_id):
    gallery = gallery_data.get("gallery", {})
    for room in gallery.get("rooms", []):
        for wall in room.get("walls", []):
            current_id = wall.get("id") or wall.get("wall_id")
            if current_id == wall_id:
                normalized = dict(wall)
                normalized["wall_id"] = current_id
                normalized["room_id"] = room.get("id") or room.get("room_id")
                return normalized
    raise ValueError(f"Wall '{wall_id}' not found")


def build_artwork_lookup(art_data):
    artworks = art_data.get("art", {}).get("artworks", [])
    lookup = {}
    duplicates = []

    for art in artworks:
        art_id = art.get("id")
        if not art_id:
            continue
        if art_id in lookup:
            duplicates.append(art_id)
            continue
        lookup[art_id] = art

    return lookup, duplicates


def get_candidate_artworks(art_data, candidate_ids, *, eligible_only=True, max_width_ft=None, max_height_ft=None):
    lookup, duplicates = build_artwork_lookup(art_data)

    selected = []
    missing = []
    skipped = []

    for art_id in candidate_ids:
        art = lookup.get(art_id)
        if not art:
            missing.append(art_id)
            continue

        if eligible_only and art.get("eligible") is False:
            skipped.append((art_id, "eligible=false"))
            continue

        width = art.get("width_ft")
        height = art.get("height_ft")

        if max_width_ft is not None and isinstance(width, (int, float)) and width > max_width_ft:
            skipped.append((art_id, f"width_ft>{max_width_ft}"))
            continue

        if max_height_ft is not None and isinstance(height, (int, float)) and height > max_height_ft:
            skipped.append((art_id, f"height_ft>{max_height_ft}"))
            continue

        selected.append(art)

    return {
        "artworks": selected,
        "missing_ids": missing,
        "skipped": skipped,
        "duplicate_ids_in_catalog": duplicates,
    }
