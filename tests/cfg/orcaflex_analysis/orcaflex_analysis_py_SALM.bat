CALL ..\SET_Directories

REM ================
REM FE Model
SET program=orcaflex_analysis
CALL ACTIVATE %program%

CD %git_root%
CALL PYTHON %program%.py

SET file_name=0198_NoTanker_static.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_dynamic_mean_ten.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_dynamic.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_static_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_dynamic_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_static_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_NoTanker_dynamic_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_WithTanker_static_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_WithTanker_dynamic_temp.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"


CD %working_directory%
SET working_directory%=
