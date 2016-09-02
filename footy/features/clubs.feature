Feature: Clubs
  As a footy-fan
  I would like to see all clubs
  So that I can view details about clubs

  Scenario: Get Premier League Clubs for 2015-2016 season
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
      | Southampton    |
      | Sunderland     |
      | West Ham       |
      | Crystal Palace |
      | Man City       |
      | Liverpool      |

  Scenario: Get Premier League Clubs for 2014-2015 season
    Given Premier League data for 2014-2015 season
    When I get clubs in the Premier League for 2014-2015
    Then I should have 20 clubs
    Then I should have clubs
      | club_name      |
      | Arsenal        |
      | Leicester      |
      | Crystal Palace |
      | Man United     |
      | QPR            |
      | Sunderland     |
      | Stoke          |
      | Liverpool      |
      | West Ham       |
      | Newcastle      |
      | Burnley        |
      | Aston Villa    |
      | Chelsea        |
      | Everton        |
      | Southampton    |
      | Swansea        |
      | Hull           |
      | Tottenham      |
      | Man City       |
      | West Brom      |
