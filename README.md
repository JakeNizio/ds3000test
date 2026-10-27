# DS3000 Group 7 — DS-18 (home-equity loan default)

| | |
|---|---|
| Catalog ID | DS-18 |
| OpenML id | **46483** |
| Target | `bad` (binary classification) |
| Split seed | **3000** (`data/splits/split_seed3000.npz`) |

## Private GitHub repository

This folder is a local starter. Leave git uninitialized here until the group is ready.

1. Create a **private** GitHub repository named so it identifies the group and dataset (for example `ds3000-group7-DS-18`).
2. Add the instructor (`[MISSING: instructor GitHub username]`) and TAs (`[MISSING: TA GitHub usernames]`) as collaborators.
3. Push this tree. Commit `data/splits/split_seed3000.npz` after the first Phase 1 run. Do **not** commit `data/raw/` or `data/interim/` (see `.gitignore`).

## Environment

- Python **3.11+**
- Install the packages listed in `requirements.txt` into whatever environment you prefer
- Select that environment as the Jupyter kernel for notebooks under `notebooks/`
- From this directory, a quick check is: `python -c "from src.data import load_dataset; print(load_dataset().shape)"`

December submission: replace `requirements.txt` with a freeze of the environment that actually runs the notebooks.

## Layout

See course instructions section 7.1. Phase 1 work lives in `notebooks/phase1-eda.ipynb` and `src/`. The test set is sealed in Phase 1 and scored once in Phase 3.
