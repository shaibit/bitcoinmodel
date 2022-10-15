import pandas as pd
import  random as rnd

def check_basic_trend(old_value, new_value, minimum_profit_precent):
    return new_value >= old_value * (1+minimum_profit_precent/100)


df = pd.read_csv('Binance_BTCUSDT_2022_minute.csv', skiprows=1)

precent = 0.3
trend = []
col = "close"
c = df[col]
for ind in df.index:
    if ind != 0:
        trend.append(check_basic_trend(c[ind],c[ind-1],precent))
trend = [False] + trend
new_cl_name = f"trend_{col}_{precent}%"
df[new_cl_name] = trend
print(df.head())
print(df.iloc[-1])
s = sum(trend)
print(f"sum {s}")


