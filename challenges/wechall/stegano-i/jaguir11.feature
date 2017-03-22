# language: en

Feature: Solve Stegano I challenge
  From site wechall
  From Training category
  With my username jaguir11

  Background:
    Given the fact that I am registered in site wechall
    And I have Windows 7 Operating System
    And I downloaded the image stegano1.bmp

  Scenario: First failed attempt
    Given the image stegano1.bmp
    When I open it with the Windows Photo Viewer
    I see some pixeled colors in the image but no message
    Then I do not solve the challenge
    But I conlcude I have to look at the image another way

  Scenario: Succesful solution
    Given the image stegano1.bmp
    When I opened with a text editior, Brackets, I see the Hex edit
    And I see the message
    And I solve the challenge
