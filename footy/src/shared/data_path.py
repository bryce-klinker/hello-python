from os import path
from itertools import islice


def get_league_name(data_path):
    file_name = path.basename(data_path)
    parts = islice(file_name.split("_"), 2, None)
    league_name_with_extension = " ".join(parts)
    return league_name_with_extension.split(".")[0]


def get_start_year(data_path):
    base_path = path.basename(data_path)
    parts = base_path.split("_")
    return int(parts[0])


def get_end_year(data_path):
    base_path = path.basename(data_path)
    parts = base_path.split("_")
    return int(parts[1])
