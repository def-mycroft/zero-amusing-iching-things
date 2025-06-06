import json
import os
import random
import hashlib
from typing import List, Dict, Tuple

COLOR_SCHEMES = {
    "obsidian-field": {
        "yin": "#1b1b1b",
        "yang": "#e5e5e5",
        "bg": "#000000",
    },
    "solarized-dark": {
        "yin": "#073642",
        "yang": "#eee8d5",
        "bg": "#002b36",
    },
    "jade-dusk": {
        "yin": "#1f2d25",
        "yang": "#cbd5b1",
        "bg": "#0f1613",
    },
}

class DaoField:
    """Binary grid with per-cell interaction thresholds."""

    def __init__(self, grid: List[List[int]], props: List[List[Dict[str, float]]], theme: str = "obsidian-field"):
        self.grid = grid
        self.props = props
        self.theme = theme if theme in COLOR_SCHEMES else "obsidian-field"

    @classmethod
    def generate(cls, n: int, theme: str = "obsidian-field") -> "DaoField":
        grid = [[random.choice([0, 1]) for _ in range(n)] for _ in range(n)]
        # simple smoothing for clumps
        for _ in range(2):
            for i in range(n):
                for j in range(n):
                    neighbors = [grid[x][y]
                                 for x in range(max(0, i-1), min(n, i+2))
                                 for y in range(max(0, j-1), min(n, j+2))]
                    if sum(neighbors) > len(neighbors)/2:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        props = [[{
            "hover": random.random() * 0.2 + 0.05,
            "yin": random.random() * 0.3 + 0.1,
            "yang": random.random() * 0.3 + 0.1,
        } for _ in range(n)] for _ in range(n)]
        return cls(grid, props, theme)

    @classmethod
    def load(cls, path: str) -> "DaoField":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data["grid"], data["props"], data.get("theme", "obsidian-field"))

    def to_dict(self) -> Dict:
        return {"grid": self.grid, "props": self.props, "theme": self.theme}

    def save(self, directory: str) -> str:
        os.makedirs(directory, exist_ok=True)
        uid = self.hash()
        path = os.path.join(directory, f"{uid}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)
        return path

    def hash(self) -> str:
        hasher = hashlib.sha256()
        hasher.update(json.dumps(self.grid, sort_keys=True).encode("utf-8"))
        return hasher.hexdigest()

    def write_html(self, path: str) -> None:
        n = len(self.grid)
        scheme = COLOR_SCHEMES[self.theme]
        flat_props: List[Dict[str, float]] = []
        flat_grid: List[int] = []
        for row, prow in zip(self.grid, self.props):
            for cell, p in zip(row, prow):
                flat_grid.append(cell)
                flat_props.append(p)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self._build_html(n, scheme, flat_grid, flat_props))

    def _build_html(self, n: int, scheme: Dict[str, str], grid: List[int], props: List[Dict[str, float]]) -> str:
        grid_json = json.dumps(grid)
        props_json = json.dumps(props)
        return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>Dao Field</title>
<style>
  body {{background:{scheme['bg']}; margin:0; display:flex; justify-content:center; align-items:center; height:100vh;}}
  .grid {{display:grid; grid-template-columns: repeat({n}, 1fr); width:90vmin; height:90vmin;}}
  .cell {{width:100%; height:100%;}}
</style>
</head>
<body>
<div class='grid'></div>
<script>
const n = {n};
const gridData = {grid_json};
const propData = {props_json};
const yinColor = '{scheme['yin']}';
const yangColor = '{scheme['yang']}';

const container = document.querySelector('.grid');
for(let i=0;i<gridData.length;i++){{
  const div = document.createElement('div');
  div.className = 'cell';
  container.appendChild(div);
}}

function colorCell(idx){{
  const c = container.children[idx];
  c.style.backgroundColor = gridData[idx] ? yangColor : yinColor;
}}

function update(idx, action){{
  const p = propData[idx];
  const prob = p[action];
  if(Math.random() < prob){{
    gridData[idx] = gridData[idx] ? 0 : 1;
    colorCell(idx);
    if(Math.random() < 0.1){{
      const x = Math.floor(idx/n); const y = idx % n;
      [[x-1,y],[x+1,y],[x,y-1],[x,y+1]].forEach(([a,b])=>{{
        if(a>=0&&a<n&&b>=0&&b<n&&Math.random()<0.5){{
          const ni=a*n+b; gridData[ni]=gridData[ni]?0:1; colorCell(ni);
        }}
      }});
    }}
  }}

container.childNodes.forEach((cell, idx)=>{{
  colorCell(idx);
  cell.addEventListener('mouseover', ()=>update(idx,'hover'));
  cell.addEventListener('click', ()=>update(idx,'yang'));
  cell.addEventListener('contextmenu', (e)=>{{e.preventDefault(); update(idx,'yin');}});
}});
</script>
</body>
</html>"""

