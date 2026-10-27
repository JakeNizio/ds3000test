"""Metrics in one place. Phase 1: majority-class baseline on validation labels."""
import numpy as np
from sklearn.metrics import accuracy_score

# Primary metric options (group may switch before locking Phase 1):
#   ROC-AUC — current. A constant prediction has AUC 0.5 by definition;
#              do not call roc_auc_score on a constant prediction vector.
#   per-class recall — alternative when you care about each class's hit rate
#                      under imbalance; would use recall_score(..., average=None).


def majority_baseline(y_true):
    """Return majority label, accuracy on y_true, and AUC note for a constant score."""
    values, counts = np.unique(y_true, return_counts=True)
    majority = values[np.argmax(counts)]
    pred = np.full_like(y_true, majority)
    acc = accuracy_score(y_true, pred)
    # Constant score → ROC-AUC is 0.5; do not call roc_auc_score here.
    auc_constant = 0.5
    return majority, acc, auc_constant
