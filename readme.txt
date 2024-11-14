to execute all the tests in file test_prezent_ai_cases.py run

pytest test_prezent_ai_cases.py -s -v

to execute all the tests with dashboard report in file test_prezent_ai_cases.py run

pytest test_prezent_ai_cases.py -s -v --dashboard

to execute all the tests with dashboard report and pytest html report in file test_prezent_ai_cases.py run

pytest test_prezent_ai_cases.py -s -v --dashboard --html=report.html

report will be generated under test package as dashboard.html and as report.html

to execute desired test case with pytest marker run

pytest -m {markername}
example :
pytest -m download_generated_ppt -s -v





