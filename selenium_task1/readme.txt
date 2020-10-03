How to run the test?

Answer: Come inside the project folder i.e "selenium_task1" and type: behave
========================================================================================											|
Test run report:									|
											|
C:\Users\amresing\Desktop\Desktop\hel\fixturetest\testfolder\behaveProject>behave	|
Feature: behave project # features/tutorial.feature:1					|
											|
  Background: common steps  # features/tutorial.feature:3				|
											|
  Scenario: check title of the home page   # features/tutorial.feature:8		|
    Given launch firefox browser           # features/steps/tutorial.py:10		|
    When login to amazon home page         # features/steps/tutorial.py:19		|
    Then verify the title of the home page # features/steps/tutorial.py:39		|
											|
  Scenario: check amazon logo           # features/tutorial.feature:12			|
    Given launch firefox browser        # features/steps/tutorial.py:10			|
    When login to amazon home page      # features/steps/tutorial.py:19			|
    Then verify the amazon logo present # features/steps/tutorial.py:45			|
											|
  Scenario: add item to kart                     # features/tutorial.feature:16		|
    Given launch firefox browser                 # features/steps/tutorial.py:10	|
    When login to amazon home page               # features/steps/tutorial.py:19	|
    Then type item in search box and add to kart # features/steps/tutorial.py:52	|
											|
  Scenario: remove item from kart  # features/tutorial.feature:19			|
    Given launch firefox browser   # features/steps/tutorial.py:10			|
    When login to amazon home page # features/steps/tutorial.py:19			|
    Then remove item from kart     # features/steps/tutorial.py:73			|
											|
  Scenario: close the browser      # features/tutorial.feature:22			|
    Given launch firefox browser   # features/steps/tutorial.py:10			|
    When login to amazon home page # features/steps/tutorial.py:19			|
    Then close browser             # features/steps/tutorial.py:86			|
											|
1 feature passed, 0 failed, 0 skipped							|
5 scenarios passed, 0 failed, 0 skipped							|
15 steps passed, 0 failed, 0 skipped, 0 undefined					|
Took 3m17.542s										|
========================================================================================