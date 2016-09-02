Feature: Clubs
  As a footy-fan
  I would like to see all clubs
  So that I can view details about clubs

  Scenario: Get Premier League Clubs
    Given Premier League data for 2015-2016 season
    When I get clubs in the Premier League for 2015-2016
    Then I should have 20 clubs
    Then I should have clubs
      | club_name      |
      | Arsenal        |
      | Bournemouth    |
      | Chelsea        |
      | Swansea        |
      | Everton        |
      | Tottenham      |
      | Leicester      |
      | Watford        |
      | Man United     |
      | Norwich        |
      | Newcastle      |
      | Stoke          |
      | West Brom      |
      | Aston Villa    |
      | Southhampton   |
      | Sunderland     |
      | West Ham       |
      | Crystal Palace |
      | Man City       |
      | Liverpool      |