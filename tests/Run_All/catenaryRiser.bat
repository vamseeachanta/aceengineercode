REM Default # keyerror "EnvironmentLoad" Need to update code with passing the unused data.
cd..
call python catenaryRiser.py 

REM API579 custom # Working without any errors
call python catenaryRiser.py 16OD_SE0500_HE0800.yml
call python catenaryRiser.py 16OD_SE1200_HE1500.yml
call python catenaryRiser.py 16OD_SE1200_HE1500_1LC.yml