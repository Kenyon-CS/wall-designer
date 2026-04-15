from wall_designer.placer import place_left_to_right

def generate(wall, artworks, scoring):
    # sort by largest first
    artworks = sorted(artworks, key=lambda a: a["width_ft"], reverse=True)

    placements = place_left_to_right(
        wall,
        artworks,
        scoring["wall_scoring"]["constraints"]
    )

    return placements
