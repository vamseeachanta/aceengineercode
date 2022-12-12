import numpy as np
import pandas as pd

fatigueData = pd.read_excel("F:\\aceengineer\\dataManager\\Fatigue_Curves\\Calculations\\SN_CurveDefinitions.xlsx",sheetname= 'Raw Data')
fatigueRawdata = fatigueData.rename(columns=fatigueData.iloc[23]).drop(fatigueData.index[:23]).reset_index(drop = True).drop(fatigueData.index[:1]).drop(['Check Flag Status', 'Lookup Index','Log s1'],axis=1)
fatigueRawdata.to_excel("F:\\aceengineer\\dataManager\\Fatigue_Curves\\FatigueRawdata.xlsx")
