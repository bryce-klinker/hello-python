from behave import *

from footy.src.clubs.club_gateway import ClubGateway
from footy.test_data.test_data_paths import premier_league_2015_2016_path

use_step_matcher("re")


@given("(.*) data for (.\d+)-(.\d+) season")
def step_impl(context, league, start_year, end_year):
    pass


@when("I get clubs in the (.*) for (.\d+)-(.\d+)")
def step_impl(context, league, start_year, end_year):
    context.clubs = ClubGateway(premier_league_2015_2016_path).get_all()


@then("I should have (.\d+) clubs")
def step_impl(context, club_count):
    assert len(context.clubs) is int(club_count)


@then("I should have clubs")
def step_impl(context):
    club_names = [club.club_name for club in context.clubs]
    for row in context.table:
        assert row['club_name'] in club_names
