CALL ..\SET_Directories

REM ================
REM FE Model
SET program=orcaflex_analysis
CALL ACTIVATE %program%

CD %git_root%
CALL PYTHON %program%.py

SET file_name=0198_NoTanker_static_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_dynamic_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=orcaflex_analysis_csv_filenames.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=csv_files_timetraces_with_out_summary.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=csv_files_timetraces_with_summary.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=yml_files_timetraces_with_summary.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"


CD %working_directory%
SET working_directory%=
