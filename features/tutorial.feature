Feature: showing off behave

  Scenario: run a simple test
     Given launch firefox browser
     When open amazon home page
     Then verify the title of the home page
	 Then verify the amazon logo present
	 Then close browser