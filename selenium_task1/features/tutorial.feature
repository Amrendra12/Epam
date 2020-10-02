Feature: behave project

  Background: common steps
     Given launch firefox browser
     When login to amazon home page
	 
	 	 
  Scenario: check title of the home page
     Then verify the title of the home page

	 
  Scenario: check amazon logo
	 Then verify the amazon logo present

	 
  Scenario: add item to kart
	 Then type item in search box and add to kart

  Scenario: remove item from kart
	 Then remove item from kart
	 
  Scenario: close the browser
	 Then close browser