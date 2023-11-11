# %%
import fastf1 as f1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from utils import comp_color, correct_fuel_laptimes

# %%
race = f1.get_session(2023, "sao paulo", "race")
# %%
race.load()
# %%
tyre_performance = race.laps[["LapTime", "Compound", "TyreLife", "LapNumber"]]
tyre_performance.LapTime = (
    race.laps["LapTime"].dt.components["seconds"]
    + (race.laps["LapTime"].dt.components["milliseconds"] / 1000)
    + (race.laps["LapTime"].dt.components["minutes"] * 60)
)
tyre_performance["CorrectedLapTime"] = tyre_performance[["LapTime", "LapNumber"]].apply(
    lambda x: correct_fuel_laptimes(
        x["LapTime"], x["LapNumber"], race.laps.LapNumber.max()
    ),
    axis=1,
)
tyre_performance = tyre_performance.loc[
    (tyre_performance.CorrectedLapTime <= 1.07 * tyre_performance.CorrectedLapTime.min())
    & (tyre_performance.LapNumber > 3)
]
tyre_performance.info()
tyre_performance["color"] = tyre_performance["Compound"].apply(comp_color)
tyre_performance


# %%
def jitter(values, j):
    return values + np.random.normal(j, 0, values.shape)


sns.set(style="ticks", context="talk")
plt.style.use("dark_background")
plt.figure(figsize=(15, 15))
for name, group in tyre_performance.groupby("Compound"):
    if group.shape[0] < 10:
        continue
    sns.regplot(
        x=group.TyreLife,
        y=group.CorrectedLapTime,
        label=name,
        scatter=False,
        color=group.iloc[0]["color"],
        lowess=True,
    )
    plt.scatter(
        x=jitter(group.TyreLife, 1),
        y=group.CorrectedLapTime,
        # label=name,
        c=group.iloc[0]["color"],
        alpha=0.6,
        s=30,
    )
plt.legend()
plt.ylabel("Fuel corrected lap time [s]")
plt.xlabel("Tyre life [laps]")
plt.title("Sao Paulo GP 2023 - Tyre Degradation", fontdict={"fontsize": 30})
# plt.ylim((79, 88))
plt.show()
# %%
