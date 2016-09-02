from behave import *

use_step_matcher("re")


@given("(.*) data for (.\d+)-(.\d+) season")
def step_impl(context, league, start_year, end_year):
    pass


@when("I get clubs in the (.*) for (.\d+)-(.\d+)")
def step_impl(context, league, start_year, end_year):
    context.clubs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


@then("I should have (.\d+) clubs")
def step_impl(context, club_count):
    assert len(context.clubs) is int(club_count)
