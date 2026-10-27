"""Load DS-18 from cache or OpenML; apply the frozen train/val/test split."""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
INTERIM = ROOT / "data" / "interim" / "ds18.parquet"
SPLIT_PATH = ROOT / "data" / "splits" / "split_seed3000.npz"
SEED = 3000
TARGET = "bad"


def load_dataset() -> pd.DataFrame:
    if INTERIM.exists():
        df = pd.read_parquet(INTERIM)
    else:
        try:
            data = fetch_openml(data_id=46483, as_frame=True, parser="auto")
        except TypeError:
            # sklearn pandas ARFF path can choke on integer categories; liac-arff works.
            data = fetch_openml(data_id=46483, as_frame=True, parser="liac-arff")
        df = data.frame
        INTERIM.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(INTERIM)
    df = df.copy()
    df.columns = [c.lower() for c in df.columns]
    return df.reset_index(drop=True)


def apply_split(df: pd.DataFrame):
    """Return X/y for train, val, and test. Do not use test until Phase 3."""
    y = pd.to_numeric(df[TARGET], errors="coerce")
    X = df.drop(columns=[TARGET])

    if SPLIT_PATH.exists():
        split = np.load(SPLIT_PATH)
        train_idx, val_idx, test_idx = split["train"], split["val"], split["test"]
        X_train, y_train = X.loc[train_idx], y.loc[train_idx]
        X_val, y_val = X.loc[val_idx], y.loc[val_idx]
        X_test, y_test = X.loc[test_idx], y.loc[test_idx]
    else:
        X_dev, X_test, y_dev, y_test = train_test_split(
            X, y, test_size=0.20, random_state=SEED, stratify=y
        )
        X_train, X_val, y_train, y_val = train_test_split(
            X_dev, y_dev, test_size=0.25, random_state=SEED, stratify=y_dev
        )
        SPLIT_PATH.parent.mkdir(parents=True, exist_ok=True)
        np.savez(
            SPLIT_PATH,
            train=X_train.index.to_numpy(),
            val=X_val.index.to_numpy(),
            test=X_test.index.to_numpy(),
        )

    return X_train, X_val, X_test, y_train, y_val, y_test
