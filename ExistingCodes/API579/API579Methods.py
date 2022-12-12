import math
from collections import OrderedDict

import numpy as np

from common.plotContourf import plotContourf


def API579GML(df, cfg, fileIndex):

    customdata = {"tmin": cfg['Geometry']['tmin'],
                "NominalID": cfg['Geometry']['NominalOD'] - 2*cfg['Geometry']['DesignWT'],
                "RSFa": cfg['API579Parameters']['RSFa'],
                "NominalWT": cfg['Geometry']['DesignWT'],
                "Age": cfg['API579Parameters']['Age'],
                "FCARateFloor": cfg['API579Parameters']['FCARateFloor'],
                "FutureCorrosionRate": cfg['ReadingSets'][fileIndex]['FCARate']
                }

    # Perform AssementLengthEvaluation for all data
    data  = GMLAssessmentLengthEvaluation(df.min(axis=None, skipna=True), customdata)
    # AssessmentLength determination
    if cfg['Default']['Analysis']['GML']['Circumference']:
        RemainingLife_df = df.copy()
        FutureCorrosionRate_df = df.copy()
        HistoricalCorrosionRate_df = df.copy()
        Tmin_df = df.copy()
        Tmax_df = df.copy()
        Tmean_df = df.copy()
        WTAcceptabilityRatio_df=df.copy()
        AveragingLength_df=df.copy()
        COVWT_df=df.copy()
        MAWP_df=df.copy()

        if (cfg['Geometry']['AssessmentLengthCeilingFactor_Circumference'] != None):
            LengthCeilLimit = cfg['Geometry']['AssessmentLengthCeilingFactor_Circumference']*math.pi*cfg['Geometry']['NominalOD']
            if data['AveragingLength'] > LengthCeilLimit:
                data['AveragingLength'] = LengthCeilLimit

        AveragingIndexRange = get_nearest_vector_index(df.columns, data['AveragingLength'])
        if AveragingIndexRange < len(df.columns):
            data['AveragingLength'] = df.columns[AveragingIndexRange]
        else:
            data['AveragingLength'] = df.columns[-1]
        # Construct thickness profile array
        for MarchingLengthIndex in range(0, len(df)):
            for MarchingCircumIndex in range(0, len(df.columns)):
                DataArray = []
                for dataIndex in range(MarchingCircumIndex, MarchingCircumIndex+AveragingIndexRange):
                    if dataIndex >= len(df.columns):
                        ColumnIndex = dataIndex - len(df.columns)
                    else:
                        ColumnIndex = dataIndex
                    # Construct thickness profile array
                    DataArray.append(df.iloc[MarchingLengthIndex, ColumnIndex])

                if MarchingLengthIndex ==9:
                    debuggingIndex = 1
                data  = GMLAssessmentLengthEvaluation(DataArray, customdata)

                if (cfg['Geometry']['AssessmentLengthCeilingFactor_Circumference'] != None):
                    LengthCeilLimit = cfg['Geometry']['AssessmentLengthCeilingFactor_Circumference']*math.pi*cfg['Geometry']['NominalOD']
                    if data['AveragingLength'] > LengthCeilLimit:
                        data['AveragingLength'] = LengthCeilLimit

                AveragingIndexRange2 = get_nearest_vector_index(df.columns, data['AveragingLength'])
                if AveragingIndexRange2 < len(df.columns):
                    data['AveragingLength'] = df.columns[AveragingIndexRange2]
                else:
                    data['AveragingLength'] = df.columns[-1]
                # Perform averaging again
                for dataIndex in range(MarchingCircumIndex, MarchingCircumIndex+AveragingIndexRange2-1):
                    if dataIndex >= len(df.columns):
                        ColumnIndex = dataIndex - len(df.columns)
                    else:
                        ColumnIndex = dataIndex
                    # Construct thickness profile array
                    DataArray.append(df.iloc[MarchingLengthIndex, ColumnIndex])

                data  = GMLAssessmentLengthEvaluation(DataArray, customdata)

                if (cfg['Geometry']['AssessmentLengthCeilingFactor_Circumference'] != None):
                    LengthCeilLimit = cfg['Geometry']['AssessmentLengthCeilingFactor_Circumference']*math.pi*cfg['Geometry']['NominalOD']
                    if data['AveragingLength'] > LengthCeilLimit:
                        data['AveragingLength'] = LengthCeilLimit
                elif (data['AveragingLength'] > math.pi*cfg['Geometry']['NominalOD']):
                    data['AveragingLength'] = math.pi*cfg['Geometry']['NominalOD']

                if AveragingIndexRange2 < len(df.columns):
                    data['AveragingLength'] = df.columns[AveragingIndexRange2]
                else:
                    data['AveragingLength'] = df.columns[-1]

                customdata.update(data)
                data = GMLAcceptability(customdata)
                customdata.update(data)

                RemainingLife_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['remainingLife']
                FutureCorrosionRate_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['futureCorrosionRate']
                HistoricalCorrosionRate_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['HistoricalCorrosionRate']
                Tmin_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['tmm']
                Tmax_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['tmax']
                Tmean_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['tam']
                WTAcceptabilityRatio_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['WTAcceptabilityRatio']
                AveragingLength_df.iloc[MarchingLengthIndex, ColumnIndex] = customdata['AveragingLength']

        PrefixFileName = 'results//Data//' + cfg['FileName'] + '_Circumference_' + str(fileIndex) + '_'
        SaveResults(RemainingLife_df, PrefixFileName + 'RemainingLife_df')
        SaveResults(FutureCorrosionRate_df, PrefixFileName + 'FutureCorrosionRate_df')
        SaveResults(HistoricalCorrosionRate_df, PrefixFileName + 'HistoricalCorrosionRate_df')
        SaveResults(Tmin_df, PrefixFileName + 'Tmin_df')
        SaveResults(Tmax_df, PrefixFileName + 'Tmax_df')
        SaveResults(Tmean_df, PrefixFileName + 'Tmean_df')
        SaveResults(WTAcceptabilityRatio_df, PrefixFileName + 'WTAcceptabilityRatio_df')
        SaveResults(AveragingLength_df, PrefixFileName + 'AveragingLength_df')

        summary = { "Description": cfg['ReadingSets'][fileIndex]['Label'],
                    "Rem. Life (yrs)": RemainingLife_df.min(axis=None, skipna=True).min(),
                    "Corr. Rate (inch/year)": FutureCorrosionRate_df.max(axis=None, skipna=True).max(),
                    #  "Max Historical Corrosion Rate (inch/year)": HistoricalCorrosionRate_df.max(axis=None, skipna=True).max(),
                    "Min WT (inch)": Tmin_df.min(axis=None, skipna=True).min(),
                    "Max WT (inch)": Tmax_df.max(axis=None, skipna=True).max(),
                    "Avg. WT (inch)": Tmean_df.min(axis=None, skipna=True).min(),
                    #  "Min WT Acceptability Ratio": WTAcceptabilityRatio_df.min(axis=None, skipna=True).min(),
                    "Len (inch)": AveragingLength_df.min(axis=None, skipna=True).min()
                    }

        GMLMAWPResults = []
        for FCAIndex in range(0, len(cfg['ReadingSets'][fileIndex]['FCA'])):
            FCA = cfg['ReadingSets'][fileIndex]['FCA'][FCAIndex]
            t = Tmean_df.min(axis=None, skipna=True).min() - FCA

            customdata = {"S": cfg['Material']['SMYS'],
                "t" : t,
                "D" : cfg['Geometry']['NominalOD'],
                "Pi": cfg['Design']['InternalPressure'],
                "Po": cfg['Design']['ExternalPressure'],
                "F" : cfg['DesignFactors']['Pressure'],
                "WeldFactor" : cfg['Material']['WeldFactor']['Seamless'],
                "T" : cfg['DesignFactors']['TemperatureDerating']
            }
            MAWP = getMAWP(customdata)
            GMLResult = {"FCA": FCA, "t": t, "MAWP": MAWP}
            GMLMAWPResults.append(GMLResult)

    return summary, GMLMAWPResults

def GMLAssessmentLengthEvaluation(DataArray, data):
    tmm = min(DataArray)
    tam = np.nanmean(DataArray)
    tmax = max(DataArray)

    FCAml = tam - data['tmin']
    nominalWTml = data['tmin'] - FCAml
    IDml = (data['NominalID']) + 2*FCAml
    Rt = (tmm - FCAml)/nominalWTml

    if (Rt < data['RSFa']):
        lengthParameter = 1.123 * math.sqrt( ((1-Rt)/(1-Rt/data['RSFa']))**2 -1 )
    else:
        lengthParameter = 50.00

    AveragingLength = lengthParameter * math.sqrt( IDml * nominalWTml);

    AssessmentLengthResult = {"AveragingLength": AveragingLength, "tmm" : tmm,
                    "FCAml": FCAml, "tam": tam, "LengthParameter":lengthParameter, "tmax": tmax}
    return AssessmentLengthResult

def GMLAcceptability(data):
    LHS = data['tmm'] - data['FCAml']
    RHS = max(0.5*data['tmin'], max(0.2*data['NominalWT'], 0.1))
    WTAcceptabilityRatio = LHS/RHS; # >1 acceptable else unacceptable

    # Remaining Life Calculation
    HistoricalCorrosionRate = (data['NominalWT'] - data['tam'])/data['Age']
    if data['FutureCorrosionRate'] == 'Historical':
        if HistoricalCorrosionRate < data['FCARateFloor']:
            futureCorrosionRate = data['FCARateFloor']
        else:
            futureCorrosionRate = HistoricalCorrosionRate
    else:
        futureCorrosionRate = data['FutureCorrosionRate']

    remainingLife = (data['tam'] - data['tmin'])/futureCorrosionRate

    result = {"WTAcceptabilityRatio": WTAcceptabilityRatio, "remainingLife": remainingLife, 
            "futureCorrosionRate": futureCorrosionRate, "HistoricalCorrosionRate": HistoricalCorrosionRate}

    return result

def get_nearest_vector_index(array, value):
    vector_index = None
    for i in range(0, len(array)):
        if array[i] > value:
            vector_index = i
            break
    
    if vector_index !=None:
        return vector_index
    else:
        return len(array)

def SaveResults(df, FileName):
    df.to_csv(FileName+'.csv')

def API579LML(df, cfg, fileIndex):
    LMLResults = LMLAcceptability(df, cfg, fileIndex)
    return LMLResults

def LMLAcceptability(df, cfg, fileIndex):
    # dfLTA = df.iloc[[cfg['LML']['LTA'][fileIndex]['sIndex'][0]: cfg['LML']['LTA'][fileIndex]['sIndex'][1]], \
    #         [cfg['LML']['LTA'][fileIndex]['cIndex'][0]: cfg['LML']['LTA'][fileIndex]['cIndex'][1]]]
    sIndex0 = cfg['LML']['LTA'][fileIndex]['sIndex'][0]
    sIndex1 = cfg['LML']['LTA'][fileIndex]['sIndex'][1]
    cIndex0 = cfg['LML']['LTA'][fileIndex]['cIndex'][0]
    cIndex1 = cfg['LML']['LTA'][fileIndex]['cIndex'][1]
    dfLTA = df.iloc[sIndex0:sIndex1, cIndex0:cIndex1].copy()
    print(dfLTA)

    customdata = { "Index_Name" : 'Length',
        "Columns_Name" : 'Circumference',
        "FileName" : 'results\\Plots\\Flaw_' + cfg['LML']['LTA'][fileIndex]['io'].split('\\')[1].split('.')[0] + '_' + cfg['LML']['LTA'][fileIndex]['Label'],
        "PltSupTitle": cfg['PlotSettings']['Data']['PltSupTitle'],
        "PltTitle": cfg['PlotSettings']['Data']['PltTitle'] + ' '+ cfg['LML']['LTA'][fileIndex]['Label'] + ', Tnom: {0} inch, Tmin: {1} inch' .format(cfg['Geometry']['DesignWT'], cfg['Geometry']['tmin']),
        "PltXLabel": cfg['PlotSettings']['Data']['PltXLabel'],
        "PltYLabel" : cfg['PlotSettings']['Data']['PltYLabel'],
        "PltLims" : cfg['LML']['LTA'][fileIndex]['Contour'],
        # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
        "PltOrigin" : 'upper',
        "PltShowContourLines" : False,
        "DataFrameRowReversed" : True
        }
    # plotHeatMap(df, customdata)
    plotContourf(dfLTA, customdata)


    dfrd = df.copy()
    dfrd.iloc[sIndex0:sIndex1, cIndex0:cIndex1] = np.nan
    trd = dfrd.mean(axis=None, skipna=True).mean()

    LMLResults = []
    for FCAIndex in range(0, len(cfg['LML']['LTA'][fileIndex]['FCA'])):
        FCA = cfg['LML']['LTA'][fileIndex]['FCA'][FCAIndex]
        FCAOutsideFlaw = FCA*cfg['LML']['LTA'][fileIndex]['FCANonFlawRatio']
        tc = trd - FCAOutsideFlaw
        s = dfLTA.index.max() - dfLTA.index.min()
        c = dfLTA.columns.max() - dfLTA.columns.min()

        tmm = dfLTA.min(axis=None, skipna=True).min()
        Rt = (tmm - FCA)/tc
        cfg['Geometry']['NominalID'] = cfg['Geometry']['NominalOD'] - 2*cfg['Geometry']['DesignWT']
        LongitudinalFlawLengthParameter = 1.285*s/math.sqrt(cfg['Geometry']['NominalID']*tc)

        if (Rt >= 0.2) and (tmm-FCA >= 0.05) and (cfg['LML']['LTA'][fileIndex]['Lmsd'] >= 1.8*math.sqrt(cfg['Geometry']['NominalID']*tc) ):
            customdata = {"S": cfg['Material']['SMYS'],
                "t" : tc,
                "D" : cfg['Geometry']['NominalOD'],
                "Pi": cfg['Design']['InternalPressure'],
                "Po": cfg['Design']['ExternalPressure'],
                "F" : cfg['DesignFactors']['Pressure'],
                "WeldFactor" : cfg['Material']['WeldFactor']['Seamless'],
                "T" : cfg['DesignFactors']['TemperatureDerating']
            }
            MAWP = getMAWP(customdata)
        else:
            MAWP = None
            Level1Outcome = 'Fail'
            raise Exception("LML Level 1 and 2 are failed.")

        if MAWP != None:
            customData = {"LongitudinalFlawLengthParameter": LongitudinalFlawLengthParameter,
                "Rt" : Rt,
                "RSFa": cfg['API579Parameters']['RSFa'],
                "MAWP": MAWP,
                "tc": tc,
                "NominalID": cfg['Geometry']['NominalID']
            }

            # Level 1 Evaluation
            data = LMLMAWPrEvaluation(customData, cfg, Level = 1)
            MAWPrL1 = data['MAWPr']
            MtL1 = data['Mt']
            MAWPrEvaluationL1 = data['MAWPrEvaluation']
            RSFL1 = data['RSF']

            # Level 2 Evaluation
            (tavgiL2, sL2) = LMLLevel2Evaluation(dfLTA, customData)
            RSFL2 = []
            MAWPrL2 = []
            MtL2 = []
            MAWPrEvaluationL2 = []
            for L2EvalIndex in range(0, len(tavgiL2)):
                AARatio = (tavgiL2[L2EvalIndex]-FCA)/tc
                LongitudinalFlawLengthParameter = 1.285*sL2[L2EvalIndex]/math.sqrt(cfg['Geometry']['NominalID']*tc)
                customData.update({"AARatio": AARatio, "LongitudinalFlawLengthParameter": LongitudinalFlawLengthParameter})
                data = LMLMAWPrEvaluation(customData, cfg, Level = 2)
                RSFL2.append(data['RSF'])
                MAWPrL2.append(data['MAWPr'])
                MtL2.append(data['Mt'])
                MAWPrEvaluationL2.append(data['MAWPrEvaluation'])

        LMLResult = {"FCA": FCA, "tc": tc, "s": s, "c": c, "tmm": tmm,
        "MAWP": MAWP, "Rt": Rt,
        "Flaw Parameter": LongitudinalFlawLengthParameter,
        "Mt, L1": MtL1,
        "MAWPrEval, L1": MAWPrEvaluationL1,
        "RSF, L1": RSFL1,
        "MAWPr, L1": MAWPrL1,
        "MAWPr, L2": min(MAWPrL2),
        "RSF, L2": min(RSFL2),
        "Mt, L2": min(MtL2),
        "tavg": trd
        }
        LMLResults.append(LMLResult)

    return LMLResults

def getMAWP(data):
    data = ASMEB31XInternalPressure(data)
    return data['MaximumDesignPressure']

def ASMEB31XInternalPressure(data):
    Stress_Hoop = data['S']*data['F']*data['WeldFactor']*data['T']

    if data['D']/data['t'] >= 30:
        DesignPressure = 2*data['S']*data['t']/data['D']*data['F']*data['WeldFactor']*data['T']
    else:
        DesignPressure = 2*data['S']*data['t']/(data['D']-data['t'])*data['F']*data['WeldFactor']*data['T']

    data.update({"MaximumDesignPressure": DesignPressure})
    return data

def LMLMAWPrEvaluation(data, cfg, Level):
    if data['LongitudinalFlawLengthParameter'] <= 0.354:
        RtFloor = 0.2
    elif data['LongitudinalFlawLengthParameter']< 20:
        RSFa = data['RSFa']
    # TO DO: Bring Table into an Excel sheet format or array format
        Mt = np.interp(data['LongitudinalFlawLengthParameter'], cfg['API579Parameters']['FoliasFactor']['FlawParameter'], cfg['API579Parameters']['FoliasFactor']['Mt']['Cylindrical'])
        RtFloor = (RSFa - RSFa/Mt)/(1-RSFa/Mt)
    elif data['LongitudinalFlawLengthParameter'] > 20:
        RtFloor = 0.9

    if data['Rt'] > RtFloor:
        MAWPrEvaluation = False
        MAWPr = data['MAWP']
        RSF = 1
    else:
        if Level == 1:
            RSF = data['Rt']/(1-(1-data['Rt'])/Mt)
        elif Level == 2:
            RSF = data['AARatio']/(1 - (1-data['AARatio'])/Mt)
        if RSF >=RSFa:
            MAWPrEvaluation = False
            MAWPr = data['MAWP']
        else:
            MAWPrEvaluation = True
            MAWPr = data['MAWP']*RSF/RSFa

    result = {"MAWPrEvaluation": MAWPrEvaluation,
    "Mt" : Mt,
    "MAWPr": MAWPr,
    "RSF": RSF
    }

    return result

def GMLMAWPrEvaluation(data, cfg):
    if data['Rt'] > RtFloor:
        MAWPrEvaluation = False
        MAWPr = data['MAWP']
        RSF = 1
    else:
        if Level == 1:
            RSF = data['Rt']/(1-(1-data['Rt'])/Mt)
        elif Level == 2:
            RSF = data['AARatio']/(1 - (1-data['AARatio'])/Mt)
        if RSF >=RSFa:
            MAWPrEvaluation = False
            MAWPr = data['MAWP']
        else:
            MAWPrEvaluation = True
            MAWPr = data['MAWP']*RSF/RSFa

    result = {"MAWPrEvaluation": MAWPrEvaluation,
    "Mt" : Mt,
    "MAWPr": MAWPr,
    "RSF": RSF
    }

    return result


def LMLLevel2Evaluation(dfLTA, data):
    tavgi = []
    s = []
    for i in range(0, len(dfLTA.columns)):
        LongitudinalCTP = dfLTA.iloc[:, i].values
        LongitudinalCTPAscending = sorted(LongitudinalCTP)
        for j in range(1, len(LongitudinalCTPAscending)):
            s.append((j+1)*(dfLTA.index[1]-dfLTA.index[0]))
            tavgi.append(sum(LongitudinalCTPAscending[0:j])/len(LongitudinalCTPAscending[0:j]))

    return(tavgi, s)