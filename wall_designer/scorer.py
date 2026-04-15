def score_fit(wall, placements):
    if not placements:
        return 0

    end = placements[-1]["x_ft"]
    return 1.0 if end <= wall["width_ft"] else 0.0


def score_spacing(placements):
    if len(placements) < 2:
        return 1

    gaps = []
    for i in range(len(placements)-1):
        gaps.append(placements[i+1]["x_ft"] - placements[i]["x_ft"])

    avg = sum(gaps) / len(gaps)
    variance = sum(abs(g - avg) for g in gaps) / len(gaps)

    return max(0, 1 - variance)


def score_balance(wall, placements):
    if not placements:
        return 0

    left = placements[0]["x_ft"]
    right = placements[-1]["x_ft"]
    center = (left + right) / 2
    wall_center = wall["width_ft"] / 2

    return max(0, 1 - abs(center - wall_center) / wall_center)


def evaluate(wall, placements, scoring):
    weights = scoring["wall_scoring"]["weights"]

    fit = score_fit(wall, placements)
    spacing = score_spacing(placements)
    balance = score_balance(wall, placements)

    total = (
        weights["fit"] * fit +
        weights["spacing"] * spacing +
        weights["balance"] * balance
    )

    return {
        "total": round(total, 3),
        "components": {
            "fit": fit,
            "spacing": spacing,
            "balance": balance
        }
    }
