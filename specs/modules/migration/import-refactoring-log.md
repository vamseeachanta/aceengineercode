# Import Path Refactoring Log

> Generated: 2025-01-24
> Target: /mnt/github/workspace-hub/digitalmodel/src/digitalmodel/common/

## Summary

| Metric | Value |
|--------|-------|
| **Total import statements found** | 90 |
| **Import statements fixed** | 90 |
| **Files processed** | 16 |
| **Pattern replaced** | `from common.` -> `from digitalmodel.common.` |

## Files Processed

| File | Imports Fixed |
|------|---------------|
| application_configuration.py | 2 |
| compare_tool_components.py | 5 |
| data_models_components.py | 7 |
| ETL_components.py | 11 |
| fatigue_analysis_components.py | 18 |
| FEAComponents.py | 1 |
| finance_components.py | 3 |
| front_end_components.py | 7 |
| log_file_analysis_components.py | 2 |
| ong_fd_components.py | 11 |
| orcaflex_model_components.py | 1 |
| ship_design.py | 1 |
| time_series_components.py | 6 |
| visualization_components.py | 5 |
| viv_analysis_components.py | 9 |
| viv_fatigue_analysis_components.py | 3 |

## Referenced Modules

The following modules are referenced via imports:

| Module | Import Count | Status |
|--------|--------------|--------|
| data | 50 | MISSING - needs copy from pyintegrity/common |
| visualizations | 17 | EXISTS |
| database | 11 | MISSING - needs copy from pyintegrity/common |
| visualization_components | 3 | EXISTS |
| ETL_components | 3 | EXISTS |
| documentation_components | 2 | EXISTS |
| ymlInput | 1 | MISSING - needs copy from pyintegrity/common |
| update_deep | 1 | MISSING - needs copy from pyintegrity/common |
| ship_fatigue_analysis | 1 | EXISTS |
| math_solvers | 1 | MISSING - needs copy from pyintegrity/common |
| bsee_data_manager | 1 | MISSING - needs copy from aceengineercode/common |

## Missing Dependencies

The following modules need to be copied to `digitalmodel/common/`:

### From pyintegrity/common/ (5 files):
- `data.py` - Core data utilities (ReadData, SaveData, Transform, AttributeDict, etc.)
- `database.py` - Database connectivity (Database, get_db_connection)
- `ymlInput.py` - YAML input utilities
- `update_deep.py` - Deep dictionary update utilities
- `math_solvers.py` - Mathematical solvers (Geometry, etc.)

### From aceengineercode/common/ (1 file):
- `bsee_data_manager.py` - BSEE data management (BSEEData)

## Detailed Import List

### application_configuration.py
```python
line 5: from digitalmodel.common.update_deep import update_deep_dictionary
line 6: from digitalmodel.common.ymlInput import ymlInput
```

### compare_tool_components.py
```python
line 21: # from digitalmodel.common.visualizations import Visualization (commented)
line 26: from digitalmodel.common.data import DefineData, ReadData
line 53: from digitalmodel.common.data import ReadData
line 162: from digitalmodel.common.visualization_components import VisualizationComponents
line 167: from digitalmodel.common.visualizations import Visualization
```

### data_models_components.py
```python
line 10: from digitalmodel.common.database import Database
line 21: from digitalmodel.common.database import Database
line 41: from digitalmodel.common.database import Database
line 91: from digitalmodel.common.database import Database
line 164: from digitalmodel.common.data import GetData
line 186: from digitalmodel.common.database import Database
line 202: from digitalmodel.common.data import ReadData
```

### ETL_components.py
```python
line 6: from digitalmodel.common.data import ReadData, SaveData
line 82: from digitalmodel.common.data import SaveData
line 213: from digitalmodel.common.data import ReadData
line 302: from digitalmodel.common.data import ReadData
line 335: from digitalmodel.common.ETL_components import ETL_components
line 383: from digitalmodel.common.data import SaveData
line 614: from digitalmodel.common.data import ReadData
line 638: from digitalmodel.common.data import ReadData
line 715: from digitalmodel.common.data import ReadData
line 809: from digitalmodel.common.data import SaveData
```

### fatigue_analysis_components.py
```python
line 32: from digitalmodel.common.data import ReadData
line 34: from digitalmodel.common.data import SaveData
line 83: from digitalmodel.common.data import ReadData
line 117: from digitalmodel.common.data import SaveData
line 172: from digitalmodel.common.data import SaveData
line 208: from digitalmodel.common.visualizations import Visualization
line 271: from digitalmodel.common.visualizations import Visualization
line 303: from digitalmodel.common.data import ReadData
line 360: from digitalmodel.common.ETL_components import ETL_components
line 365: from digitalmodel.common.data import SaveData
line 435: from digitalmodel.common.data import FromString, ReadData
line 454: from digitalmodel.common.data import ReadData
line 468: from digitalmodel.common.data import SaveData
line 497: from digitalmodel.common.data import SaveData
line 575: from digitalmodel.common.visualizations import Visualization
line 589: from digitalmodel.common.data import ReadData, SaveData
line 590: from digitalmodel.common.visualizations import Visualization
```

### FEAComponents.py
```python
line 29: from digitalmodel.common.database import Database
```

### finance_components.py
```python
line 7: from digitalmodel.common.data import AttributeDict
line 49: from digitalmodel.common.visualizations import Visualization
line 175: from digitalmodel.common.visualizations import Visualization
```

### front_end_components.py
```python
line 10: from digitalmodel.common.data import AttributeDict
line 16: from digitalmodel.common.database import Database
line 33: from digitalmodel.common.data import Transform
line 57: from digitalmodel.common.data import Transform
line 104: from digitalmodel.common.data import ReadData
line 112: from digitalmodel.common.documentation_components import JinjaLib
line 146: from digitalmodel.common.documentation_components import PDFReports
```

### log_file_analysis_components.py
```python
line 11: from digitalmodel.common.data import ReadData
line 23: from digitalmodel.common.data import ReadData
```

### ong_fd_components.py
```python
line 5: from digitalmodel.common.data import DateTimeUtility
line 7: from digitalmodel.common.bsee_data_manager import BSEEData
line 8: from digitalmodel.common.database import get_db_connection
line 9: from digitalmodel.common.database import Database
line 10: from digitalmodel.common.data import AttributeDict, transform_df_datetime_to_str
line 157: from digitalmodel.common.data import Transform
line 502: from digitalmodel.common.math_solvers import Geometry
line 681: from digitalmodel.common.data import Transform
line 738: from digitalmodel.common.data import Transform
line 888: from digitalmodel.common.visualization_components import VisualizationComponents
line 911: from digitalmodel.common.data import SaveData
```

### orcaflex_model_components.py
```python
line 801: from digitalmodel.common.data import SaveData
```

### ship_design.py
```python
line 1: from digitalmodel.common.ship_fatigue_analysis import ShipFatigueAnalysis
```

### time_series_components.py
```python
line 41: from digitalmodel.common.data import SaveData
line 80: from digitalmodel.common.database import Database
line 160: from digitalmodel.common.data import PandasChainedAssignent
line 222: from digitalmodel.common.data import PandasChainedAssignent
line 253: from digitalmodel.common.data import PandasChainedAssignent
line 272: from digitalmodel.common.data import PandasChainedAssignent
line 362: from digitalmodel.common.visualization_components import VisualizationComponents
```

### visualization_components.py
```python
line 44: from digitalmodel.common.database import Database
line 60: from digitalmodel.common.data import SaveData
line 97: from digitalmodel.common.visualizations import Visualization
line 154: from digitalmodel.common.data import ReadData
line 173: from digitalmodel.common.visualizations import Visualization
```

### viv_analysis_components.py
```python
line 83: from digitalmodel.common.visualizations import Visualization
line 100: from digitalmodel.common.visualizations import Visualization
line 144: from digitalmodel.common.data import ReadData
line 163: from digitalmodel.common.visualizations import Visualization
line 195: from digitalmodel.common.visualizations import Visualization
line 236: from digitalmodel.common.visualizations import Visualization
line 261: from digitalmodel.common.data import ReadData
line 271: from digitalmodel.common.visualizations import Visualization
line 292: from digitalmodel.common.visualizations import Visualization
```

### viv_fatigue_analysis_components.py
```python
line 611: from digitalmodel.common.ETL_components import ETL_components
line 619: from digitalmodel.common.data import SaveData
line 767: from digitalmodel.common.data import SaveData
```

## Next Steps

1. Copy missing dependencies from `pyintegrity/common/` to `digitalmodel/common/`:
   - data.py
   - database.py
   - ymlInput.py
   - update_deep.py
   - math_solvers.py

2. Copy `bsee_data_manager.py` from `aceengineercode/common/` to `digitalmodel/common/`

3. After copying, update imports in the copied files (they may also have `from common.` patterns)

4. Run import verification tests to ensure all modules can be imported successfully

## Notes

- One import is commented out (compare_tool_components.py line 21)
- All 90 active imports were successfully converted from `from common.` to `from digitalmodel.common.`
- No `import common.` or `from common import` patterns were found
