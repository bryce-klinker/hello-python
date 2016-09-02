Feature: Leagues
  As a footy-fan
  I want to see available leagues
  So that I can track clubs in each league

  Scenario: Get All Leagues
    When I get leagues
    Then I get all leagues
      | league_name    | start_year | end_year |
      | Premier League | 2015       | 2016     |
      | Premier League | 2014       | 2015     |
      | Championship   | 2015       | 2016     |