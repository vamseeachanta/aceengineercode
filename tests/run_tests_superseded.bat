hostname >temp
SET /p computer_to_run=<temp
DEL temp
SET working_directory=%cd%

IF "%computer_to_run%"=="LHO3RQFLQ2"
(
  SET run_environment=work
  SET fe_environment=False
  SET git_root="K:\aceengineer\"
)
ELSE IF "%computer_to_run%"=="AceEngineer_Server3"
(
  SET run_environment=home
  SET fe_environment=True
  SET git_root="C:\Users\achantv\Documents\Utilities\aceengineer"
)
ELSE
(
  SET run_environment=home
  SET fe_environment=False
  SET git_root="C:\Users\achantv\Documents\Utilities\aceengineer"
)

REM ================
REM FE Model
SET program=vertical_riser
CALL ACTIVATE %program%

SET file_name=2500ft_WT_0875_64ppg.yml
CD %git_root%
CALL PYTHON %program%.py "%working_directory%\%file_name%"
CD %working_directory%

REM ================
REM Run FE Simulation for Effective Tension QA
CALL PAUSE

IF "%fe_environment%"=="True"
(
SET program=orcaflex_analysis
CALL ACTIVATE %program%

SET file_name=effective_tension_2500ft_WT_0875_64pcf.yml
CD %git_root%
CALL PYTHON %program%.py "%working_directory%\%file_name%"
CD %working_directory%
)

REM ================
REM Run Effective Tension QA
SET program=compare_tool
CALL ACTIVATE %program%

SET file_name=QA_2500ft_WT_0875_64ppg.yml
CD %git_root%
CALL PYTHON %program%.py "%working_directory%\%file_name%"
CD %working_directory%

REM ================
REM Run vertical_riser tests on West Boreas Model
SET program=vertical_riser
CALL ACTIVATE %program%

SET file_name=vertical_riser_py_west_boreas.yml
CD %git_root%
CALL PYTHON %program%.py "%working_directory%\%file_name%"
CD %working_directory%

