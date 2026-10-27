# Phase 1 person guides — Group 7 / DS-18

**This is your Phase 1 playbook.** Map your name in `CHECKLIST.md`, then work only your Person section here. Mark boxes in the checklist when each item is truly done.

---

## Person 1 — Metric, Figure 1, baseline

**You own:** how we score defaults, how imbalanced `bad` is, and how bad a dumb guess is.

### Must know

- `bad = 1` = default. Accuracy is weak when most loans are paid.
- **ROC-AUC:** do defaults rank above non-defaults? A constant guess has AUC **0.5**.
- **Per-class recall:** hit rate within each class (use only if the group locks it for a clear reason).
- **Majority baseline:** always predict the common class on **validation** only. Phase 2/3 must beat this story.

### Your tasks (in order)

1. **Measure** `bad` **rate** (`pd.to_numeric`) → confirm ROC-AUC (current) or switch to per-class recall.

   *Tip:* if defaults are rare, accuracy is a trap — keep ROC-AUC unless the group has a clear recall reason.
2. **Figure 1** — target balance + claim.

   *Tip:* claim cites printed counts and default rate.
3. **Metric justification** markdown.

   *Tip:* put the measured default rate in the sentence that locks the metric.
4. **Baseline** on validation via `evaluate.py`.

   *Tip:* validation only; for AUC, state constant → 0.5 — do **not** call `roc_auc_score` on a constant vector.

### Done when

- [ ] Metric cell locks **which** metric and **why**, with the default rate in the sentence
- [ ] `results/figures/01-target-balance.png` + claim matches printed counts
- [ ] Baseline cell run; majority label + val accuracy printed; AUC note = 0.5 if using AUC
- [ ] You can answer: Why not accuracy? What does AUC 0.5 mean for our baseline?

---

## Person 2 — Missingness, Figure 2, split, pipeline

**You own:** what’s missing, the frozen split, and train-only encoding (no peeking at val/test).

### Must know

- Missingness can track default risk here — measure **overall and by** `bad` before locking treatment.
- **A** = §3.3 recipe (median/scale; most-frequent/one-hot). **B** (current) = A + `add_indicator=True` on the **numeric** imputer only.
- **Split:** seed **3000** → ~60% train / 20% val / 20% test in `data/splits/split_seed3000.npz`. Never re-roll the seed. **Test sealed until Phase 3.**
- **Leakage:** `fit` on train only; `transform` val. Never fit or score on `X_test` in Phase 1.

### Your tasks (in order)

1. **Measure missingness** overall and by `bad` → confirm A vs B (B current).

   *Tip:* a real `bad=0` vs `bad=1` gap on top missing columns supports B.
2. **Figure 2** — missingness by target + claim.

   *Tip:* name the top-missing feature and the gap (or say the gap is tiny).
3. **Missing-values half** of the missing + outlier write-up (with Person 3).

   *Tip:* lock A/B with Fig 2 as evidence; keep `src/features.py` in sync if you switch.
4. **Split declaration** markdown (after `apply_split` runs once).

   *Tip:* seed 3000, ~60/20/20, path to `split_seed3000.npz`, test not scored until Phase 3.
5. **Fit pipeline** on train; transform val; leave test unused.

   *Tip:* `prep.fit(X_train)` then `transform(X_val)` only; print shapes; do not touch `X_test`.

### Done when

- [ ] `02-missingness-by-target.png` + claim mentions the `bad=0` / `bad=1` gap (or lack of one)
- [ ] “Missing values” markdown locks A or B and points at Fig 2
- [ ] Split markdown complete; `split_seed3000.npz` exists after first run
- [ ] Pipeline cell: fit train → transform val; no fit on val/test
- [ ] You can answer: Why fit only on train? What does `add_indicator` buy us? What fraction is test?

---

## Person 3 — Outliers, Figures 3 and 5

**You own:** whether extreme values are signal or noise, and the keep / cap / drop lock.

### Must know

- **1.5-IQR fence** is a **screen**, not an auto-delete rule.
- Removal is **not** the default. Cap named columns only with a reason. Drop only with a justification other than “failed the fence.”
- Zero-inflated counts often sit outside a fence at zero — usually a reason to **keep**.
- Numeric-vs-target claim comes from the printed summary, not vibes.

### Your tasks (in order)

1. **IQR outlier screen** → confirm keep-all (current) vs cap vs justified drop.

   *Tip:* fence = diagnostic; zero-inflated “extremes” usually argue keep, not drop.
2. **Figure 3** — one numeric vs target + claim.

   *Tip:* prefer `debtinc` (or another credit feature); claim compares mean/median for `bad=0` vs `bad=1`.
3. **Figure 5** — outlier screen + claim *(after the screen code)*.

   *Tip:* which column has the most breaches, and that rows are kept (unless the group locked cap/drop).
4. **Outlier half** of the missing + outlier write-up (with Person 2).

   *Tip:* lock keep/cap/drop with Fig 5; must match the screen decision in the notebook.

### Done when

- [ ] Screen table printed; “Outliers” markdown states the decision in plain English
- [ ] `03-numeric-vs-target.png` and `05-outlier-screen.png` with claims that match printed numbers
- [ ] Keep-all includes a *why*; cap/drop names columns/rules and a non-fence justification for drops
- [ ] You can answer: What did the IQR screen find? Why didn’t we delete those rows?

---

## Person 4 — Dictionary, Figure 4, problem, prior work

**You own:** what the columns mean, how categories relate to default, what the project is for, and prior-work honesty.

### Must know

- Dictionary = type + meaning + missingness rate for **every** column (no mystery codes).
- Categorical plot: does `reason` / `job` / etc. change default risk?
- Problem cell: binary classification + a usefulness sentence that sounds human (lender / risk review).
- **§9.1:** list public analyses you opened and how you differ — or write that you used none. No fake citations.

### Your tasks (in order)

1. **Data dictionary** — fill every `[MISSING: column meaning]`.

   *Tip:* one-line loan/credit definitions; missingness rates are already computed.
2. **Figure 4** — one categorical vs target + claim.

   *Tip:* claim the range of `P(bad=1 | category)` across levels, not just “categories differ.”
3. **Problem / usefulness** markdown.

   *Tip:* one task-type sentence + one usefulness sentence in the group’s own words.
4. **§9.1 prior-work** cell.

   *Tip:* sources + “we differ by …” **or** an explicit “we used none.”

### Done when

- [ ] No `[MISSING: column meaning]` left
- [ ] `04-categorical-vs-target.png` + claim cites printed rates / spread
- [ ] Problem cell polished (not template filler)
- [ ] Prior-work cell filled honestly
- [ ] You can answer: What does `reason` mean? Why would a lender care about this prediction?

---

## Group order (sit-down)

```
1. All — env runs; notebook load works
2. Parallel — P1 metric measure | P2 missingness | P3 IQR screen
3. Parallel — Figures 1–4 + dictionary; then P3 Figure 5
4. Write-ups — P4 problem; P1 metric; P2+P3 missing/outlier
5. P2 split declaration → P1 baseline → P2 pipeline
6. P4 prior work
7. All — header, GitHub, dry-run §9.2; each person exports any AI sessions they used
```

## Finish line

| Person | Your figures | Your locks | Demo |
|--------|--------------|------------|------|
| 1 | `01-…` | Metric + baseline | Why not accuracy? AUC 0.5? |
| 2 | `02-…` | A/B + split + pipeline | Fit on train only? Test sealed? |
| 3 | `03-…`, `05-…` | Keep / cap / drop | IQR find? Why keep? |
| 4 | `04-…` | Problem + dictionary + §9.1 | Column meanings? Usefulness? |

When every row for your Person is checked in `CHECKLIST.md` and you can answer the demo questions, Phase 1 for your slot is done.
