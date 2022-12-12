REM Screening
CALL python catenaryRiser.py 16OD_SE1200_HE1500_1LC.yml

REM FJ Extension Sensitivity to help with strength and fatigue
CALL python catenaryRiser.py 16OD_SE1200_HE1500_TSJ2in.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_TSJ2p25in.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_TSJ3p0in.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_TSJ3p0in_20ft.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_TSJ3p0in_30ft.yml
REM Buoyancy Ratio Sensitivity
CALL python catenaryRiser.py 16OD_SE1200_HE1500_BF_Low.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_BF_High.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_BF_vHigh.yml

REM Declination Angle Sensitivity
CALL python catenaryRiser.py 16OD_SE1200_HE1500_Ang06.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_Ang10.yml
CALL python catenaryRiser.py 16OD_SE1200_HE1500_Ang12.yml

REM Configuration Sensitivity
REM CALL python catenaryRiser.py 16OD_SE0500_HE0800.yml
REM CALL python catenaryRiser.py 16OD_SCR.yml

REM Flexjoint Stiffness Sensitivity
REM CALL python catenaryRiser.py 16OD_SE1200_HE1500_FJX2.yml
REM CALL python catenaryRiser.py 16OD_SE1200_HE1500_FJInf.yml

REM Pressure Sensitivty
REM CALL python catenaryRiser.py 16OD_SE1200_HE1500_DP8000.yml

