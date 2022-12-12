REM Default # Working without any errors
cd..
call python APISTD2RD.py

REM Custom # We need update the code passing unused data in custom yml file
call python APISTD2RD.py 10.yml
call python APISTD2RD.py 11.yml
call python APISTD2RD.py 12.yml
call python APISTD2RD.py 14.yml
call python APISTD2RD.py 16.yml
