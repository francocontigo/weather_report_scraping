@echo off
REM Replace the path below with the actual absolute path to scraping.py.
python C:...\wheater_report_scraping\src\scraping.py
REM --------------------

REM Set Up Task Scheduler:
REM 1. Open the Task Scheduler on your Windows machine. You can do this by searching for "Task Scheduler" in the Start menu.
REM 2. In the Task Scheduler, click on "Create Basic Task..." in the right-hand Actions pane.
REM 3. Follow the wizard to set a name and description for your task.
REM 4. Choose the trigger "Daily" and set the start date and time to 12:00 PM.
REM 5. Set the action to "Start a program" and browse to the location where your batch file (run_python_script.bat) is located.
REM 6. Complete the wizard, review your settings, and click "Finish."
