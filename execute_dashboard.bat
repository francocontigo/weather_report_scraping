@echo off

rem Set the path to the virtual environment activate script
set VENV_PATH=venv\Scripts\activate

rem Activate the virtual environment
call %VENV_PATH%

rem Execute the Python script
streamlit run src\dashboard_streamlit.py

rem Pause for user input before deactivating the virtual environment
pause

rem Deactivate the virtual environment
deactivate
