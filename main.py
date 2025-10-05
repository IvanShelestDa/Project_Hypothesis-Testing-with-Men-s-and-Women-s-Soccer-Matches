import pandas as pd
import pingouin as pg

def filter_world_cup_after_2002(df):
    return df[(df['tournament'] == 'FIFA World Cup') & (df['date'] > '2002-01-01')]

men_results = pd.read_csv('men_results.csv')
women_results = pd.read_csv('women_results.csv')

men_world_cup_after_2002 = filter_world_cup_after_2002(men_results)
women_world_cup_after_2002 = filter_world_cup_after_2002(women_results)

men_goals = men_world_cup_after_2002['home_score'] + men_world_cup_after_2002['away_score']
women_goals = women_world_cup_after_2002['home_score'] + women_world_cup_after_2002['away_score']

t_test_result = pg.ttest(men_goals, women_goals)

p_val = t_test_result['p-val'].values[0]

significance_level = 0.10
if p_val < significance_level:
    result = "reject"
else:
    result = "fail to reject"

result_dict = {"p_val": p_val, "result": result}
print(result_dict)