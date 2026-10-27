# Phase 1 checklist — Group 7 / DS-18

Mark items off as you finish them. Person slots appear only in this checklist (and as matching `[Person N]` tags in the notebook). Work top to bottom; items marked *(parallel)* can run at the same time within that step.

**Learning guides:** see [`PERSON-GUIDES.md`](PERSON-GUIDES.md) for what each Person 1–4 task means, why it matters, and what “done” looks like.

## Person mapping

```
Person 1 → [MISSING: name]
Person 2 → [MISSING: name]
Person 3 → [MISSING: name]
Person 4 → [MISSING: name]
```

Shared boilerplate (load, cache, frozen split, pipeline, baseline) is already in the tree — every member must be able to explain it (§9.2).

**AI use (§8)** is not a Person slot. Anyone may use AI; whoever uses it exports the session into `ai-log/`, keeps `INDEX.md` / the notebook index honest, and helps keep the short group statement accurate.

Working assumptions the starter ships (group may switch before that section is locked):

| Choice | Current | Other options |
|--------|---------|---------------|
| Metric | ROC-AUC | per-class recall |
| Missing values | B (`add_indicator=True` on numeric imputer only) | A (§3.3 as written, no indicator) |
| Outliers | keep every row | cap named columns; drop rows with a justification other than “failed the fence” |
| Class balance | do not resample in Phase 1 | resample inside training rows only (never before the split) |

---

## 1. Setup

- [ ] Fill notebook header `[MISSING:]` fields (student numbers; demo session Tue 1 Dec or Fri 4 Dec 2026); map Person 1–4 above — **All**
- [ ] Create private GitHub repo naming group + dataset (e.g. `ds3000-group7-DS-18`); add instructor `[MISSING: GitHub username]` and TAs `[MISSING: TA GitHub usernames]`; push when ready — **All**

## 2. Measure, then lock the group choices *(parallel within this step)*

Do these before writing the metric / missing / outlier justifications.

- [ ] Confirm/switch metric after measuring `bad` rate (`pd.to_numeric`); options: ROC-AUC (current) vs per-class recall — **Person 1**
  - Tip: run the target-balance cell first; if defaults are rare, accuracy is a trap — keep ROC-AUC unless the group wants per-class recall for a clear reason.
- [ ] Measure missingness overall and by `bad`; confirm/switch A vs B (both listed; B current) — **Person 2**
  - Tip: compare missing rates for `bad=0` vs `bad=1` on the top missing columns; a real gap supports B (`add_indicator` on numeric).
- [ ] IQR outlier screen; confirm keep-all vs cap vs justified drop (all listed; keep-all current) — **Person 3**
  - Tip: treat the fence as a screen only; zero-inflated counts often look “extreme” at zero — that is usually a reason to **keep**, not drop.

## 3. Dictionary and figures *(parallel within this step; after load works)*

- [ ] Data dictionary (every column: type, meaning, missingness rate) — **Person 4**
  - Tip: replace every `[MISSING: column meaning]` with a one-line loan/credit definition (`loan`, `mortdue`, `debtinc`, …); rates are already computed.
- [ ] Figure 1 target balance + claim from printed numbers — **Person 1**
  - Tip: claim must cite the printed counts and default rate; rewrite if you re-run and numbers change.
- [ ] Figure 2 missingness by target + claim — **Person 2**
  - Tip: claim should name the top-missing feature and the `bad=0` vs `bad=1` gap (or say the gap is tiny).
- [ ] Figure 3 one numeric vs target + claim — **Person 3**
  - Tip: prefer `debtinc` (or another credit feature); claim compares mean/median for `bad=0` vs `bad=1` from the printed table.
- [ ] Figure 4 one categorical vs target + claim — **Person 4**
  - Tip: use `P(bad=1 | category)` from the crosstab; claim the range/spread across levels, not just “categories differ.”
- [ ] Figure 5 outlier screen + claim — **Person 3** *(after step-2 screen code)*
  - Tip: claim which column has the most fence breaches and that rows are kept (unless the group locked cap/drop).

## 4. Write-ups *(after the matching measure or figure)*

- [ ] Problem / usefulness / task type markdown — **Person 4**
  - Tip: one clear binary-classification sentence + one usefulness sentence in the group’s own words (lender / risk review), not template filler.
- [ ] Metric justification markdown (ties to target rate) — **Person 1** *(after step 2 metric measure)*
  - Tip: put the measured default rate in the sentence that locks ROC-AUC or per-class recall.
- [ ] Missing + outlier treatment write-up — **Person 2 + Person 3** *(after step 2 measures)*
  - Tip: P2 locks A/B with Fig 2 as evidence; P3 locks keep/cap/drop with Fig 5; both halves must agree with `src/features.py` and the screen decision.
- [ ] Split declaration markdown (seed 3000; test sealed) — **Person 2** *(after `apply_split` run once)*
  - Tip: state seed **3000**, ~60/20/20, path to `split_seed3000.npz`, and that test is not scored until Phase 3.

## 5. Baseline, then pipeline *(after split + features ready)*

- [ ] Baseline majority class on **validation** via `evaluate.py`; AUC note for constant = 0.5 — **Person 1**
  - Tip: score **validation only**; if metric is AUC, write that a constant predictor is 0.5 — do not call `roc_auc_score` on a constant vector.
- [ ] Fit pipeline on train only; transform val; leave `X_test` unused — **Person 2**
  - Tip: `prep.fit(X_train)` then `transform(X_val)` only; fitting on val/test is leakage. Print shapes; do not touch `X_test`.

## 6. Prior work *(last Phase 1 item)*

- [ ] §9.1 prior-work cell fill — **Person 4**
  - Tip: list public analyses you opened + how this project differs, **or** write explicitly that you used none — honesty beats fake citations.

## Later phases (revisable slots; do not design those notebooks yet)

- [ ] Phase 2 models notebook — Person `[MISSING: slot]`
- [ ] Phase 3 advanced notebook / test scoring — Person `[MISSING: slot]`
