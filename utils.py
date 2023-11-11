from matplotlib.colors import rgb2hex


def correct_fuel_laptimes(lap_time, lap_number, max_laps):
    total_fuel = 110
    current_fuel = total_fuel * (1 - (lap_number / max_laps))
    correction = 0.03 * current_fuel
    return lap_time - correction


def to_one(t):
    return tuple([elem / 255 for elem in t])


def comp_color(compound):
    match compound:
        case "HARD":
            return to_one((255, 255, 255))
        case "MEDIUM":
            return to_one((227, 207, 87))
        case "SOFT":
            return to_one((255, 48, 48))
        case "INTERMEDIATE":
            return to_one((0, 201, 87))
        case "WET":
            return to_one((28, 134, 238))

def team_color(team):
    match team:
        case "Mercedes":
            return to_one((0,210,90))
        case "Ferrari":
            return to_one((220,0,0))
        case "Red Bull Racing":
            return to_one((6,0,239))
        case "Alpine":
            return to_one((0,144,255))
        case "Haas F1 Team":
            return to_one((255,255,255))
        case "Aston Martin":
            return to_one((0,111,98))
        case "AlphaTauri":
            return to_one((43,69,98))
        case "McLaren":
            return to_one((255,135,0))
        case "Alfa Romeo":
            return to_one((144,0,0))
        case "Williams":
            return to_one((0,90,255))
        

def team_color_hex(team):
    return rgb2hex(team_color(team))