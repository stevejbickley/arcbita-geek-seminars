---
paths:
  - "**/*.py"
  - "**/*.ipynb"
---

# Python conventions

## Every script starts the same way

```python
"""02_clean.py — harmonise waves and build the analysis sample.

Reads:  data/raw/survey_*.csv
Writes: data/clean/analysis.parquet
"""

from pathlib import Path
import numpy as np
import pandas as pd

RNG = np.random.default_rng(20260728)   # once, at the top

IN_DIR = Path("data") / "raw"
OUT_DIR = Path("data") / "clean"
OUT_DIR.mkdir(parents=True, exist_ok=True)
```

- `pathlib`, not string concatenation. It works on Windows and Mac without change.
- A module docstring naming inputs and outputs.
- A single seeded generator. Never the global `np.random` functions.

## Sample size discipline

```python
n_before = len(df)
df = df.dropna(subset=["income"])
print(f"Dropped {n_before - len(df)} rows missing income "
      f"({n_before} -> {len(df)})")
```

For merges, use `indicator=True` and inspect it before dropping:

```python
merged = left.merge(right, on=["municipality", "year"],
                    how="outer", indicator=True, validate="one_to_one")
print(merged["_merge"].value_counts())
```

`validate=` catches an unexpected many-to-many join, which is the failure that silently multiplies your sample.

## Large data

Do not try to load a file larger than memory. Convert to Parquet and query it.

```python
import duckdb

duckdb.sql("""
    COPY (SELECT * FROM read_csv_auto('data/raw/big.csv'))
    TO 'data/clean/big.parquet' (FORMAT PARQUET)
""")

out = duckdb.sql("""
    SELECT year, state, avg(rate) AS mean_rate
    FROM 'data/clean/big.parquet'
    GROUP BY year, state
""").df()
```

Parquet typically compresses tabular data by a factor of ten or more, and DuckDB reads only the columns a query needs, so aggregations over hundreds of millions of rows finish in seconds without loading anything.

## Style

- `snake_case`. Functions are verbs.
- Type hints on anything doing real work.
- No mutable default arguments.
- Comparisons to `None` use `is`.
- Lines under 100 characters. Format with `ruff` or `black` and stop thinking about it.
- Comments say why, not what.

## Notebooks

Fine for exploring, not for the pipeline. Anything a result depends on lives in a `.py` file that runs top to bottom. A notebook whose cells were run out of order is not reproducible and cannot be reviewed by diff.

## Environment

Record it. `pip freeze > docs/requirements.txt`, or use `uv` and commit the lock file.

## Checklist

```
[ ] Docstring names inputs and outputs
[ ] pathlib for all paths, all relative
[ ] One seeded Generator, no global np.random
[ ] Row counts reported at every transformation
[ ] merge uses validate= and indicator=
[ ] Large files as Parquet, queried with DuckDB
[ ] Pipeline in .py files, not notebooks
[ ] Outputs written to scripts/_outputs/
```
