CALL ..\SET_Directories

REM ================
REM FE Model
SET program=fea_model
REM CALL ACTIVATE %program%

CD %git_root%
REM CALL PYTHON %program%.py

SET file_name=0098_SALM_Dynamic_Rev1.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0098_SALM_Tanker_Dynamic_Rev1.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"


CD %working_directory%
SET working_directory%=
