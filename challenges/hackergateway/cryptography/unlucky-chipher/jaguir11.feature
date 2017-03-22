# language: en

Feature: Solve Unlucky Cipher challenge
  From site Hackergateway
  From Cryptography category
  With my username jaguir11

  Background:
    Given the fact that I am registered in site hackergateway
    And I have Windows 7 Operating System

  Scenario: Succesful solution
    Given an encoded message
    When I look at the message I see scrambled letters
    And I think it is most likely a caesar cipher
    And I see the first three letters are most likely "the"
    So I count the difference to get the shift cipher
    And I solve the challenge
    