# Wall Designer (Python)

This project provides a simple testbed for designing artwork layouts on a **single gallery wall**.

Students will:
- Select a wall
- Choose candidate artworks
- Apply a scoring function
- Write algorithms to generate wall layouts

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt

python -m wall_designer.main \
  --gallery data/gallery.yaml \
  --art data/art.yaml \
  --scoring data/wall_scoring.yaml \
  --wall R1-N \
  --candidates A1,A2,A3,A4,A5 \
  --algorithm student_algorithms/wall_greedy_v1.py
```

## What You Implement

You will edit:
```
student_algorithms/wall_greedy_v1.py
```
### Your function:
```
def generate(wall, artworks, scoring):
```
should return:
```
[
  {
    "artwork_id": "...",
    "x_ft": ...,
    "y_ft": ...,
    "locked": False
  }
]
```
## Goal

Create better wall layouts by improving:

  - spacing
  - balance
  - fit
  - visual consistency
## Files
| File	| Purpose |
| gallery.yaml |	walls and dimensions |
| art.yaml |	artwork sizes + metadata |
| wall_scoring.yaml |	scoring weights |
| wall_greedy_v1.py |	your algorithm |

## Start Simple

Try:

  - sorting by size
  - evenly spacing artworks
  - centering layouts

Then improve.