# AceEngineerCode File Inventory

> Generated: 2026-01-24
> Repository: /mnt/github/workspace-hub/aceengineercode

## Summary

| Category | File Count | Total Lines |
|----------|------------|-------------|
| Common Library (`/common/`) | 39 | 13,784 |
| Custom Modules (`/custom/`) | 91 | 10,266 |
| Entry Scripts (`/scripts/`) | 28 | 1,874 |
| YAML Configuration (`/config/`) | 298 | 92,661 |
| **Grand Total** | **456** | **118,585** |

---

## 1. Common Library (`/common/`)

Core shared utilities and components used across all analysis modules.

| Path | Lines | Description |
|------|-------|-------------|
| `common/__init__.py` | 0 | Package initialization |
| `common/API579_components.py` | 718 | API 579 fitness-for-service calculation components |
| `common/application_configuration.py` | 59 | Application configuration management |
| `common/ApplicationManager.py` | 373 | Central application manager pattern implementation |
| `common/BS7910_critical_flaw_limits.py` | 980 | BS7910 critical flaw limit calculations |
| `common/bsee_data_manager.py` | 76 | BSEE (Bureau of Safety and Environmental Enforcement) data management |
| `common/compare_tool_components.py` | 186 | Data comparison tool utilities |
| `common/data.py` | 963 | Core data handling utilities |
| `common/database.py` | 774 | SQL Server database connectivity and operations |
| `common/DataFrame_To_doc.py` | 41 | DataFrame to document conversion |
| `common/DataFrame_To_Image.py` | 38 | DataFrame to image conversion |
| `common/DataFrame_To_xlsx.py` | 87 | DataFrame to Excel conversion |
| `common/data_models_components.py` | 205 | Data model definition components |
| `common/documentation_components.py` | 91 | Documentation generation utilities |
| `common/engineering_units.py` | 29 | Engineering unit conversion utilities |
| `common/ETL_components.py` | 524 | Extract-Transform-Load pipeline components |
| `common/excel_utilities.py` | 106 | Excel file handling utilities |
| `common/fad.py` | 63 | Failure Assessment Diagram calculations |
| `common/fatigue_analysis_components.py` | 703 | Fatigue analysis calculation components |
| `common/FEAComponents.py` | 267 | Finite Element Analysis components |
| `common/finance_components.py` | 207 | Financial analysis and cost calculations |
| `common/fracture_mechanics_components.py` | 310 | Fracture mechanics calculation components |
| `common/front_end_components.py` | 172 | User interface components |
| `common/log_file_analysis_components.py` | 88 | Log file parsing and analysis |
| `common/math_solvers.py` | 88 | Mathematical solver algorithms |
| `common/ong_fd_components.py` | 1,111 | Oil and gas field development analysis components |
| `common/orcaflex_model_components.py` | 1,032 | OrcaFlex model generation and integration |
| `common/parallel_process_components.py` | 170 | Parallel processing utilities |
| `common/pipe_components.py` | 65 | Pipe geometry and property calculations |
| `common/set_logging.py` | 38 | Logging configuration |
| `common/shear7_model_components.py` | 134 | SHEAR7 VIV analysis model components |
| `common/time_series_components.py` | 503 | Time series data processing |
| `common/typical_riser_stack_up_calculations.py` | 231 | Riser stack-up calculation utilities |
| `common/update_deep.py` | 35 | Deep dictionary update utilities |
| `common/visualization_components.py` | 240 | Data visualization components |
| `common/visualizations.py` | 729 | Advanced visualization functions |
| `common/viv_analysis_components.py` | 326 | Vortex-induced vibration analysis components |
| `common/wellpath3D.py` | 1,985 | 3D wellpath trajectory calculations |
| `common/ymlInput.py` | 37 | YAML input file parsing |

**Subtotal:** 39 files, 13,784 lines

---

## 2. Custom Modules (`/custom/`)

Specialized analysis modules organized by engineering domain.

### 2.1 API 579 Module (`/custom/API579/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/API579/API579Methods.py` | 1 | API 579 method entry point |
| `custom/API579/customInputs.py` | 10 | Custom input handling |
| `custom/API579/temperatureDerating.py` | 17 | Temperature derating calculations |

### 2.2 API RP 2RD Module (`/custom/API_RP_2RD/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/API_RP_2RD/APIRP2RD_Methods.py` | 22 | API RP 2RD recommended practice methods |

### 2.3 API STD 2RD Module (`/custom/API_STD_2RD/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/API_STD_2RD/APISTD2RDMethods.py` | 163 | API STD 2RD standard methods |
| `custom/API_STD_2RD/extractData.py` | 26 | Data extraction utilities |
| `custom/API_STD_2RD/fileList.py` | 13 | File listing utilities |
| `custom/API_STD_2RD/Summary.py` | 55 | Summary generation |
| `custom/API_STD_2RD/temperatureDerating.py` | 9 | Temperature derating |
| `custom/API_STD_2RD/BurstPressure/APISTD2RD.py` | 48 | Burst pressure main module |
| `custom/API_STD_2RD/BurstPressure/APISTD2RDMethods.py` | 55 | Burst pressure calculation methods |
| `custom/API_STD_2RD/BurstPressure/temperatureDerating.py` | 9 | Burst pressure temperature derating |
| `custom/API_STD_2RD/BurstPressure/dataManager/checkPythonEnvironment.py` | 22 | Environment validation |
| `custom/API_STD_2RD/BurstPressure/dataManager/customUpdate.py` | 24 | Custom update utilities |
| `custom/API_STD_2RD/BurstPressure/dataManager/loadConfiguration.py` | 6 | Configuration loading |
| `custom/API_STD_2RD/BurstPressure/dataManager/ymlInput.py` | 18 | YAML input handling |
| `custom/API_STD_2RD/BurstPressure/dataManager/__init__.py` | 0 | Package init |
| `custom/API_STD_2RD/BurstPressure/logs/setLogging.py` | 39 | Logging setup |
| `custom/API_STD_2RD/BurstPressure/logs/__init__.py` | 0 | Package init |
| `custom/API_STD_2RD/BurstPressure/results/plotDefault.py` | 24 | Default plotting |
| `custom/API_STD_2RD/BurstPressure/results/saveData.py` | 7 | Data saving utilities |
| `custom/API_STD_2RD/BurstPressure/results/__init__.py` | 0 | Package init |

### 2.4 ASME B31 Module (`/custom/ASMEB31/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/ASMEB31/extractData.py` | 62 | ASME B31 data extraction |
| `custom/ASMEB31/fileList.py` | 13 | File listing |
| `custom/ASMEMethods.py` | 126 | ASME calculation methods |

### 2.5 Catenary Riser Module (`/custom/catenary/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/catenary/catenaryMethods.py` | 236 | Catenary riser calculation methods |
| `custom/catenary/catenaryRiserSummary.py` | 93 | Catenary riser summary generation |
| `custom/catenary/extractData.py` | 69 | Data extraction |
| `custom/catenary/fileList.py` | 13 | File listing |
| `custom/catenary/getFatigueLoading.py` | 138 | Fatigue loading calculations |
| `custom/catenary/orcaflexModel.py` | 612 | OrcaFlex model generation |
| `custom/catenary/pipeProperties.py` | 113 | Pipe property calculations |
| `custom/catenary/saveData.py` | 39 | Data saving utilities |
| `custom/catenary/__init__.py` | 0 | Package init |

### 2.6 DNV OS F101 Module (`/custom/DNV_OS_F101/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/DNV_OS_F101/AttributeDict.py` | 3 | Attribute dictionary class |
| `custom/DNV_OS_F101/ConfigurationManager.py` | 64 | Configuration management |
| `custom/DNV_OS_F101/RigidPipe.py` | 318 | Rigid pipe analysis per DNV OS F101 |
| `custom/DNV_OS_F101/solvePolynomialEquation.py` | 24 | Polynomial equation solver |
| `custom/DNV_OS_F101/sympyPolynomial.py` | 25 | SymPy polynomial utilities |
| `custom/DNV_OS_F101/user_setup/__init__.py` | 0 | Package init |

### 2.7 Fatigue Curves Module (`/custom/Fatigue_Curves/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/Fatigue_Curves/FatigueBasiccurve.py` | 68 | Basic fatigue curve calculations |
| `custom/Fatigue_Curves/FatiguecurveRawdata.py` | 6 | Fatigue curve raw data |
| `custom/Fatigue_Curves/LinearslopeCal.py` | 42 | Linear slope calculations |
| `custom/Fatigue_Curves/ll2.py` | 22 | Auxiliary calculations |
| `custom/Fatigue_Curves/Shear7dataCal.py` | 38 | SHEAR7 data calculations |
| `custom/Fatigue_Curves/__init__.py` | 0 | Package init |

### 2.8 FEA Model Module (`/custom/fea_model/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/fea_model/buoy_components.py` | 182 | Buoyancy component definitions |
| `custom/fea_model/Constraint_components.py` | 88 | Constraint definitions |
| `custom/fea_model/environment_components.py` | 234 | Environmental loading components |
| `custom/fea_model/general_components.py` | 47 | General FEA components |
| `custom/fea_model/group_components.py` | 29 | Group definition components |
| `custom/fea_model/LineType_components.py` | 213 | Line type definitions |
| `custom/fea_model/line_components.py` | 154 | Line component definitions |
| `custom/fea_model/shape_components.py` | 29 | Shape component definitions |
| `custom/fea_model/VariableData_components.py` | 48 | Variable data components |
| `custom/fea_model/VesselType_components.py` | 36 | Vessel type definitions |
| `custom/fea_model/Vessel_components.py` | 76 | Vessel component definitions |

### 2.9 OrcaFlex Post-Processing Module (`/custom/OrcaFlex_Post/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/OrcaFlex_Post/ASCII_To_DataFrame.py` | 53 | ASCII to DataFrame conversion |
| `custom/OrcaFlex_Post/DataFrame_to_image2_NotWorking.py` | 78 | DataFrame to image (deprecated) |
| `custom/OrcaFlex_Post/DF_Format_check.py` | 16 | DataFrame format validation |
| `custom/OrcaFlex_Post/OrcaFlexAnalysis_Fatigue.py` | 107 | OrcaFlex fatigue analysis |
| `custom/OrcaFlex_Post/plotCustomFatigue.py` | 72 | Custom fatigue plotting |
| `custom/OrcaFlex_Post/postProcess.py` | 165 | Post-processing utilities |
| `custom/OrcaFlex_Post/postProcessPlotting.py` | 50 | Post-process plotting |
| `custom/OrcaFlex_Post/temp.py` | 9 | Temporary utilities |
| `custom/OrcaFlex_Post/xlsx_To_DataFrame.py` | 55 | Excel to DataFrame conversion |

### 2.10 Plate Buckling Module (`/custom/Plate_Buckling/`)

| Path | Lines | Description |
|------|-------|-------------|
| `custom/Plate_Buckling/calculations/plateBucklingCal_G.py` | 298 | Plate buckling calculation variant G |
| `custom/Plate_Buckling/calculations/plateBucklingCal_H.py` | 298 | Plate buckling calculation variant H |
| `custom/Plate_Buckling/calculations/plateBucklingCal_i.py` | 297 | Plate buckling calculation variant I |
| `custom/Plate_Buckling/calculations/plateBucklingCal_J.py` | 297 | Plate buckling calculation variant J |
| `custom/Plate_Buckling/calculations/plateBucklingCal_K.py` | 297 | Plate buckling calculation variant K |
| `custom/Plate_Buckling/calculations/__init__.py` | 0 | Package init |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/ConfigurationManager.py` | 63 | Stiffener buckling configuration |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/plateBuckling.py` | 245 | Plate buckling main module |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/StiffnerBuckling_Cal(Draft1).py` | 455 | Stiffener buckling draft 1 |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/StiffnerBuckling_Cal(Draft2).py` | 665 | Stiffener buckling draft 2 |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/StiffnerBuckling_Cal.py` | 245 | Stiffener buckling calculations |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/DataProvision/dataProvision.py` | 0 | Data provision (empty) |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/DataProvision/parameters_stiffnerbuckling.py` | 140 | Stiffener buckling parameters |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/DataProvision/__init__.py` | 0 | Package init |
| `custom/Plate_Buckling/StiffnerBuckling_Cal/user_setup/__init__.py` | 0 | Package init |

### 2.11 Standalone Custom Files

| Path | Lines | Description |
|------|-------|-------------|
| `custom/bsee_data_refresh.py` | 77 | BSEE data refresh utilities |
| `custom/exception_examples.py` | 25 | Exception handling examples |
| `custom/MaterialProperties.py` | 91 | Material property definitions |
| `custom/orcaflex_analysis_components.py` | 947 | OrcaFlex analysis components |
| `custom/orcaflex_post_process.py` | 168 | OrcaFlex post-processing |
| `custom/PipeCapacity.py` | 676 | Pipe capacity calculations |
| `custom/PipeSizing.py` | 193 | Pipe sizing calculations |
| `custom/postProcessPlotting.py` | 50 | Post-process plotting utilities |
| `custom/temperatureDerating.py` | 17 | Temperature derating calculations |
| `custom/vertical_riser_components.py` | 289 | Vertical riser analysis components |

**Subtotal:** 91 files, 10,266 lines

---

## 3. Entry Scripts (`/scripts/`)

Main entry point scripts for executing analysis workflows.

| Path | Lines | Description |
|------|-------|-------------|
| `scripts/API579.py` | 60 | API 579 fitness-for-service analysis entry |
| `scripts/catenary_riser.py` | 184 | Catenary riser analysis entry |
| `scripts/catenary_riser_summary.py` | 88 | Catenary riser summary generation |
| `scripts/compare_tool.py` | 18 | Data comparison tool entry |
| `scripts/data_models.py` | 22 | Data models management entry |
| `scripts/design_calculations.py` | 70 | Design calculations entry |
| `scripts/ETL.py` | 80 | ETL pipeline entry |
| `scripts/fatigue_analysis.py` | 69 | Fatigue analysis entry |
| `scripts/fea_model.py` | 21 | FEA model generation entry |
| `scripts/finance.py` | 24 | Financial analysis entry |
| `scripts/fracture_mechanics.py` | 63 | Fracture mechanics analysis entry |
| `scripts/front_end.py` | 28 | Front-end interface entry |
| `scripts/log_file_analysis.py` | 58 | Log file analysis entry |
| `scripts/logic_based_text_analytics.py` | 104 | Text analytics entry |
| `scripts/oda.py` | 67 | ODA (Offshore Design Analysis) entry |
| `scripts/ong_field_development.py` | 63 | Oil and gas field development entry |
| `scripts/OrcaFlexAnalysis.py` | 104 | OrcaFlex analysis entry (legacy) |
| `scripts/orcaflex_analysis.py` | 19 | OrcaFlex analysis entry |
| `scripts/pdf_parse.py` | 72 | PDF parsing entry |
| `scripts/pipe.py` | 68 | Pipe analysis entry |
| `scripts/statistical_assessment.py` | 81 | Statistical assessment entry |
| `scripts/statistical_describe.py` | 91 | Statistical description entry |
| `scripts/time_series.py` | 87 | Time series analysis entry |
| `scripts/timeline.py` | 74 | Timeline/scheduling entry |
| `scripts/vertical_riser.py` | 66 | Vertical riser analysis entry |
| `scripts/visualization.py` | 61 | Visualization generation entry |
| `scripts/viv_analysis.py` | 82 | VIV analysis entry |
| `scripts/tools/manage-agent-resources.py` | 50 | Agent resource management tool |

**Subtotal:** 28 files, 1,874 lines

---

## 4. YAML Configuration (`/config/`)

Configuration files organized by analysis module.

| Subdirectory | File Count | Description |
|--------------|------------|-------------|
| `config/api579/` | 10 | API 579 analysis configurations |
| `config/compare_tool/` | 12 | Data comparison tool configurations |
| `config/data/` | 7 | Data file configurations |
| `config/data_models/` | 15 | Database model configurations |
| `config/etl/` | 12 | ETL pipeline configurations |
| `config/fatigue_analysis/` | 3 | Fatigue analysis configurations |
| `config/fracture_mechanics/` | 20 | Fracture mechanics configurations |
| `config/ong_field_development/` | 44 | Oil and gas field development configurations |
| `config/pdf_parse/` | 3 | PDF parsing configurations |
| `config/pipe/` | 35 | Pipe analysis configurations |
| `config/results/` | 74 | Results output configurations |
| `config/visualization/` | 45 | Visualization configurations |
| `config/viv_analysis/` | 18 | VIV analysis configurations |
| **Total** | **298** | **92,661 lines** |

---

## 5. Module Analysis Summary

### By Engineering Domain

| Domain | Files | Lines | Key Modules |
|--------|-------|-------|-------------|
| API Standards | 25 | 1,891 | API579, API_RP_2RD, API_STD_2RD |
| OrcaFlex Integration | 15 | 3,268 | orcaflex_model_components, OrcaFlex_Post |
| Fatigue Analysis | 12 | 1,847 | fatigue_analysis_components, Fatigue_Curves |
| VIV Analysis | 5 | 598 | viv_analysis_components, shear7_model_components |
| Structural Analysis | 20 | 3,485 | Plate_Buckling, pipe_components, BS7910 |
| Data Management | 18 | 3,754 | database, ETL_components, data_models |
| Visualization | 6 | 1,397 | visualizations, visualization_components |
| Field Development | 3 | 1,254 | ong_fd_components, bsee_data_manager |

### Files by Size Category

| Category | Count | Total Lines |
|----------|-------|-------------|
| Large (500+ lines) | 12 | 12,567 |
| Medium (100-499 lines) | 45 | 8,834 |
| Small (<100 lines) | 101 | 4,523 |

### Largest Files (Top 10)

| Rank | File | Lines |
|------|------|-------|
| 1 | `common/wellpath3D.py` | 1,985 |
| 2 | `common/ong_fd_components.py` | 1,111 |
| 3 | `common/orcaflex_model_components.py` | 1,032 |
| 4 | `common/BS7910_critical_flaw_limits.py` | 980 |
| 5 | `common/data.py` | 963 |
| 6 | `custom/orcaflex_analysis_components.py` | 947 |
| 7 | `common/database.py` | 774 |
| 8 | `common/visualizations.py` | 729 |
| 9 | `common/API579_components.py` | 718 |
| 10 | `common/fatigue_analysis_components.py` | 703 |

---

## 6. Package Dependencies

### Internal Import Analysis

The following files have the most internal dependencies:

1. **ApplicationManager.py** - Central orchestrator, imports from most common modules
2. **orcaflex_model_components.py** - Heavy integration with pipe, visualization, and data modules
3. **fatigue_analysis_components.py** - Dependencies on fracture mechanics, time series, and visualization

### External Package Requirements

Based on codebase analysis, key external dependencies include:

- **numpy** - Numerical computations
- **pandas** - Data manipulation
- **scipy** - Scientific computing
- **matplotlib** - Static visualization
- **plotly** - Interactive visualization
- **openpyxl** - Excel file handling
- **pyyaml** - YAML configuration parsing
- **pyodbc** / **pymssql** - SQL Server connectivity
- **OrcFxAPI** - OrcaFlex integration

---

## Notes

1. **Empty `__init__.py` files** are not counted toward functionality but indicate Python package structure
2. **Line counts** include comments and blank lines
3. **Deprecated files** (marked NotWorking, Draft) are included for completeness
4. **Configuration files** contain extensive parameterization for different analysis scenarios
