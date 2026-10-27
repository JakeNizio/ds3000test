"""ColumnTransformer from course §3.3, plus the group's missingness choice."""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_preprocessor(X_train):
    num = X_train.select_dtypes(include="number").columns
    cat = X_train.select_dtypes(exclude="number").columns

    # Missingness options (group may switch before locking Phase 1):
    #   A — §3.3 as written: SimpleImputer(strategy="median") with no indicator
    #   B — current: A plus add_indicator=True on the numeric imputer only
    # Categorical imputer stays without add_indicator unless the group writes why.
    prep = ColumnTransformer(
        [
            (
                "num",
                Pipeline(
                    [
                        ("impute", SimpleImputer(strategy="median", add_indicator=True)),
                        ("scale", StandardScaler()),
                    ]
                ),
                num,
            ),
            (
                "cat",
                Pipeline(
                    [
                        ("impute", SimpleImputer(strategy="most_frequent")),
                        ("encode", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                cat,
            ),
        ]
    )
    return prep
