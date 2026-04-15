def place_left_to_right(wall, artworks, constraints):
    width = wall["width_ft"]
    gap = constraints["min_gap_ft"]
    margin = constraints["wall_edge_margin_ft"]
    y = constraints["target_center_y_ft"]

    x = margin
    placements = []

    for art in artworks:
        w = art["width_ft"]

        if x + w > width - margin:
            break

        placements.append({
            "artwork_id": art["id"],
            "x_ft": round(x, 2),
            "y_ft": y,
            "locked": False
        })

        x += w + gap

    return placements
