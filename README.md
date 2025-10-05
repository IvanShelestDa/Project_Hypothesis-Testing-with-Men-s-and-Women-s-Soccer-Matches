# Project: Hypothesis Testing with Men's and Women's Soccer Matches

**Author:** Completed independently by Ivan Shelest

**Based on DataCamp project:** [Hypothesis Testing with Men's and Women's Soccer Matches](https://app.datacamp.com/learn/projects/1611)

---

## Description

As a sports journalist specializing in soccer analysis, you have followed both men's and women's international matches for several years. Based on observation, you suspect that **women's international soccer matches tend to have more goals scored on average** than men's matches.

To verify this intuition with statistical evidence, you decide to perform a **hypothesis test** comparing the average number of goals scored in men's and women's matches. This investigation aims to provide a data-driven foundation for an analytical article that would interest your readers.

Because soccer has evolved over time, and performance can vary significantly across tournaments, the analysis focuses **only on official FIFA World Cup matches (excluding qualifiers) held after January 1, 2002**.

Two datasets were used in this analysis, containing results of every official men’s and women’s international football match since the 19th century. These datasets are stored in the files:

* `men_results.csv`
* `women_results.csv`

---

## Research Question

**Are more goals scored, on average, in women's international soccer matches than in men's?**

---

## Hypotheses

At a **10% significance level**, the hypotheses are defined as follows:

* **Null hypothesis (H₀):**
  The mean number of goals scored in women’s international soccer matches is equal to that in men’s matches.

* **Alternative hypothesis (H₁):**
  The mean number of goals scored in women’s international soccer matches is greater than that in men’s matches.

---

## Methodology

1. **Data Filtering:**
   Only official FIFA World Cup matches (excluding qualifiers) since January 1, 2002, are included.

2. **Variables of Interest:**

   * `home_score` and `away_score` columns are used to calculate the total number of goals per match.

3. **Statistical Test:**

   * A **two-sample t-test** (Welch’s t-test) is conducted to compare the mean number of goals in men’s and women’s matches.
   * The test assumes independence between matches and equal variance is not required.

4. **Decision Rule:**

   * If the **p-value < 0.10**, reject the null hypothesis.
   * Otherwise, fail to reject the null hypothesis.

---

## Code Summary

```python
import pandas as pd
import pingouin as pg

def filter_world_cup_after_2002(df):
    return df[(df['tournament'] == 'FIFA World Cup') & (df['date'] > '2002-01-01')]

men_results = pd.read_csv('men_results.csv')
women_results = pd.read_csv('women_results.csv')

men_wc = filter_world_cup_after_2002(men_results)
women_wc = filter_world_cup_after_2002(women_results)

men_goals = men_wc['home_score'] + men_wc['away_score']
women_goals = women_wc['home_score'] + women_wc['away_score']

t_test_result = pg.ttest(men_goals, women_goals)
p_val = t_test_result['p-val'].values[0]

significance_level = 0.10
result = "reject" if p_val < significance_level else "fail to reject"

result_dict = {"p_val": p_val, "result": result}
print(result_dict)
```

---

## Results

```
{'p_val': 0.0051961448009743005, 'result': 'reject'}
```

Since the **p-value (0.0052)** is well below the 0.10 significance threshold, we **reject the null hypothesis**.

This means there is **strong statistical evidence** that, on average, **women’s international soccer matches have more goals scored than men’s matches** in FIFA World Cups since 2002.

---

## Interpretation

The result supports the hypothesis that women’s soccer tends to feature higher-scoring matches compared to men’s. While several factors could contribute to this difference — such as tactical styles, defensive organization, or team parity — the analysis provides quantitative backing for this long-standing observation.

---

## Technologies Used

* Python 3.12
* pandas
* pingouin (or scipy.stats alternative)
* VS Code

---

## Repository Structure

```
Project_Hypothesis-Testing-with-Men-s-and-Women-s-Soccer-Matches/
│
├── main.py            # Main analysis script
├── men_results.csv    # Dataset of men’s international match results
├── women_results.csv  # Dataset of women’s international match results
└── README.md          # Project documentation
```

---

## Conclusion

Based on the hypothesis test, the analysis concludes that **women’s FIFA World Cup matches have a statistically higher mean number of goals** compared to men’s matches since 2002.

This finding demonstrates how statistical testing can validate intuitive observations in sports analytics, providing credible and data-driven insights.