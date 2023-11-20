@echo off
REM Replace the path below with the actual path to scraping.py.
python C:...\wheater_report_scraping\src\scraping.py
REM --------------------

REM Set Up Task Scheduler:
REM a. Open the Task Scheduler on your Windows machine. You can do this by searching for "Task Scheduler" in the Start menu.
REM b. In the Task Scheduler, click on "Create Basic Task..." in the right-hand Actions pane.
REM c. Follow the wizard to set a name and description for your task.
REM d. Choose the trigger "Daily" and set the start date and time to 12:00 PM.
REM e. Set the action to "Start a program" and browse to the location where your batch file (run_python_script.bat) is located.
REM f. Complete the wizard, review your settings, and click "Finish."
