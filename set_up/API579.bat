REM API579
SET environment_label=%~n0

call conda env create -f %environment_label%.yaml
call activate %environment_label%
CALL pip install python-dateutil pytz --force-reinstall --upgrade
