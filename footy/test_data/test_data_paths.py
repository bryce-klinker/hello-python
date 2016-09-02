from os import path

seasons_path = path.realpath(path.join(__file__, '..', 'seasons'))

premier_league_2015_2016_path = path.realpath(path.join(seasons_path, '2015_2016_Premier_League.csv'))

def get_season_path(league, start_year, end_year):
    league_name = league.replace(" ", "_")
    csv_name = str.format("{0}_{1}_{2}.csv", start_year, end_year, league_name)
    return path.realpath(path.join(seasons_path, csv_name))
