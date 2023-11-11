# %%
import ergast_py as ep
# %%
e = ep.Ergast()
# %%
laps_mexico_2023 = e.season(2023).round().lap(10).get_lap().laps
laps_mexico_2023
# %%
e.season(2023).round().get_pit_stops()
# %%
