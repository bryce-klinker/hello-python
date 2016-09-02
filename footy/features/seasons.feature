Feature: Seasons
  As a footy-fan
  I want to see seasons for a league
  So that I can track a league across years

  Scenario: Get Seasons for League
    When I get seasons for Premier League
    Then I should get seasons
      | start_year | end_year |
      | 2015       | 2016     |
      | 2014       | 2015     |