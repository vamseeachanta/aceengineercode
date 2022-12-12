CALL ..\SET_Directories

REM ================
REM FE Model
SET program=orcaflex_analysis
CALL ACTIVATE %program%

CD %git_root%

REM SET file_name=0198_WithTanker_static.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_static.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_WithTanker_dynamic_hawser_histograms.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_WithTanker_dynamic_hawser_mean_ten.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_WithTanker_dynamic.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_WithTanker_dynamic_mean_ten.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_dynamic_inclination_stats.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_dynamic_buoy_inclination_pm.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_dynamic_buoy_inclination.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_WithTanker_static_temp.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_dynamic_mean_ten.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_dynamic.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_static_temp.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"
REM 
REM SET file_name=0198_NoTanker_dynamic_temp.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=csv_files_RAOs.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

REM SET file_name=0198_NoTanker_dynamic_Spectral.yml
REM CALL PYTHON %program%.py "%working_directory%\%file_name%"

SET file_name=0198_WithTanker_dynamic_Spectral.yml
CALL PYTHON %program%.py "%working_directory%\%file_name%"

CD %working_directory%
SET working_directory%=
