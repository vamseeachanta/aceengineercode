CALL SET_Directories

REM ================
REM FE Model
SET program=time_series
CALL ACTIVATE %program%

CD %git_root%

REM CALL PYTHON %program%.py

SET file_name=time_series_disys_all_tables_R2_run2_bd_vessel_pos.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

CD %working_directory%

