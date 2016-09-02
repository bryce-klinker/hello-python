from behave import *

from footy.src.leagues.league_gateway import LeagueGateway
from footy.test_data.test_data_paths import seasons_path

use_step_matcher("re")


@when("I get seasons for (.*)")
def step_impl(context, league):
    context.league = LeagueGateway(seasons_path).get_league(league)


@then("I should get seasons")
def step_impl(context):
    for row in context.table:
        season = [season for season in context.league.seasons if season.start_year == int(row["start_year"])][0]
        assert season.end_year == int(row["end_year"])