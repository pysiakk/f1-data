# %%

# %%
fig, ax = plt.subplots(figsize=(8,6))
for label, df in pd.concat({'VER':race.laps.pick_driver('VER').pick_compounds('MEDIUM').pick_fastest().telemetry, 'NOR':race.laps.pick_driver('NOR').pick_compounds('MEDIUM').pick_fastest().telemetry}).reset_index().rename(columns={'level_0': 'Driver'}).groupby('Driver'):
    df.plot(x='Time', y='Speed', kind='line', ax=ax, label=label)

plt.legend()