hostname >temp
SET /p computer_to_run=<temp
DEL temp

SET run_environment=home
SET fe_environment=False
SET git_root="K:\aceengineer"

IF "%computer_to_run%"=="LHO3RQFLQ2" (
  SET run_environment=work
  SET fe_environment=False
  SET git_root="C:\Users\achantv\Documents\Utilities\aceengineer"
)

IF "%computer_to_run%"=="DESKTOP-K82UDB4" (
  SET run_environment=home
  SET fe_environment=True
  SET git_root="K:\aceengineer"
) 

IF "%computer_to_run%"=="AceEngineer-011" (
  SET run_environment=home
  SET fe_environment=True
  SET git_root="D:\aceengineer"
)

SET working_directory=%cd%

