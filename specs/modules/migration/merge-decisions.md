# Common Utilities Merge Decisions Report

> Generated: 2026-01-24
> Repositories Compared:
> - aceengineercode: `/mnt/github/workspace-hub/aceengineercode/common/`
> - digitalmodel/common: `/mnt/github/workspace-hub/digitalmodel/src/digitalmodel/common/`
> - digitalmodel/pyintegrity: `/mnt/github/workspace-hub/digitalmodel/src/digitalmodel/modules/pyintegrity/common/`

## Executive Summary

| Category | Count |
|----------|-------|
| **IDENTICAL** (no merge needed) | 24 files |
| **KEEP_DIGITALMODEL** | 13 files |
| **KEEP_ACEENGINEERCODE** | 0 files |
| **MERGE_REQUIRED** | 2 files |

---

## Part 1: Primary Overlapping Files (aceengineercode vs digitalmodel/common)

### 1. ETL_components.py

| Metric | aceengineercode | digitalmodel |
|--------|-----------------|--------------|
| Lines | 524 | 826 |
| Status | DIFFERENT | - |

**Analysis:**
- digitalmodel version is 57% larger (302 more lines)
- digitalmodel uses modern formatting (PEP 8 compliant)
- digitalmodel uses double-quotes consistently
- aceengineercode uses older single-quote style

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Larger, better formatted, more complete implementation

---

### 2. FEAComponents.py

| Metric | aceengineercode | digitalmodel |
|--------|-----------------|--------------|
| Lines | 267 | 316 |
| Status | DIFFERENT | - |

**Analysis:**
- digitalmodel version includes import statements at top (proper module structure)
- digitalmodel imports from `assetutilities.common` and `digitalmodel.custom.fea_model`
- aceengineercode uses inline imports (anti-pattern)
- digitalmodel class definition uses modern syntax `class FEAComponents:` vs `class FEAComponents():`

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Proper module structure with explicit imports, modern syntax

---

### 3. shear7_model_components.py

| Metric | aceengineercode | digitalmodel |
|--------|-----------------|--------------|
| Lines | 134 | 238 |
| Status | DIFFERENT | - |

**Analysis:**
- digitalmodel version is 78% larger (104 more lines)
- digitalmodel imports from `assetutilities.common.data`
- digitalmodel has better formatting and line breaks for readability
- aceengineercode has compact but less readable code

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** More complete implementation with better code organization

---

### 4. typical_riser_stack_up_calculations.py

| Metric | aceengineercode | digitalmodel |
|--------|-----------------|--------------|
| Lines | 231 | 551 |
| Status | DIFFERENT | - |

**Analysis:**
- digitalmodel version is 139% larger (320 more lines)
- digitalmodel has significantly expanded functionality
- digitalmodel uses better variable naming and formatting
- Major structural differences suggest enhanced capabilities

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Substantially more complete implementation

---

### 5. visualization_components.py (vs digitalmodel/common)

| Metric | aceengineercode | digitalmodel/common |
|--------|-----------------|---------------------|
| Lines | 240 | 281 |
| Status | DIFFERENT | - |

**Analysis:**
- digitalmodel version is 17% larger
- Both have same core functionality
- digitalmodel has improved formatting (PEP 8)
- String quotes standardized to double-quotes in digitalmodel

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Better formatting and consistent style

---

### 6. visualizations.py (vs digitalmodel/common)

| Metric | aceengineercode | digitalmodel/common |
|--------|-----------------|---------------------|
| Lines | 729 | 900 |
| Status | DIFFERENT | - |

**Analysis:**
- digitalmodel version is 23% larger (171 more lines)
- digitalmodel has enhanced plotting capabilities
- Better code organization in digitalmodel
- digitalmodel removes inline imports

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** More complete with additional visualization features

---

## Part 2: Pyintegrity Common Files (aceengineercode vs digitalmodel/pyintegrity/common)

### 7. API579_components.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 718 | 997 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity version is 39% larger (279 more lines)
- pyintegrity includes proper imports at file top
- pyintegrity imports from `pyintegrity.custom.API579` modules
- pyintegrity has enhanced GML analysis with better print statements
- pyintegrity version returns `self.cfg` from methods (better API)

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** More complete implementation with proper module structure

---

### 8. BS7910_critical_flaw_limits.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 980 | 1221 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity version is 25% larger (241 more lines)
- pyintegrity includes new method `update_cfg_with_library_file()`
- pyintegrity imports `WorkingWithYAML` utility
- pyintegrity has improved multiprocessing support
- Better code formatting and line breaks

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Extended functionality with library file handling

---

### 9. ApplicationManager.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 373 | 397 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity version is 6% larger (24 more lines)
- pyintegrity includes imports at file top (proper structure)
- pyintegrity has enhanced `get_custom_file()` with `pkgutil.get_data()` support
- pyintegrity supports package-relative file loading
- pyintegrity has better path handling for test data

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Enhanced package support and better file loading mechanisms

---

### 10. DataFrame_To_Image.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 38 | 40 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity version has 2 additional lines
- pyintegrity adds proper cleanup: `fig.clf()`, `plt.cla()`, `plt.close()`
- pyintegrity adds configurable `col_width` and `font_size` parameters
- pyintegrity removes hardcoded path `'results//API_STD_2RD//'`

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Better memory management, configurable parameters, no hardcoded paths

---

### 11. DataFrame_To_xlsx.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 87 | 87 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity includes proper border import: `from openpyxl.styles.borders import BORDER_THIN, Border, Side`
- pyintegrity uses `writer._save()` (underscore prefix - protected method)
- aceengineercode uses `writer.save()` (public method)
- This is a **compatibility difference** - newer openpyxl versions use `_save()`

**Decision:** `MERGE_REQUIRED`
**Reason:** Need to verify openpyxl version compatibility; pyintegrity likely more current

---

### 12. fracture_mechanics_components.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 310 | 424 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity version is 37% larger (114 more lines)
- pyintegrity includes imports at top with `WorkingWithYAML`
- pyintegrity adds `update_cfg_with_library_file()` method
- pyintegrity has better code organization

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Extended functionality with library file support

---

### 13. pipe_components.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 65 | 72 |
| Status | DIFFERENT | - |

**Analysis:**
- pyintegrity version is 11% larger (7 more lines)
- pyintegrity includes imports at file top
- pyintegrity imports from `pyintegrity.custom.*` modules
- aceengineercode uses inline imports

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** Proper module structure with explicit imports

---

### 14. ymlInput.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 37 | 37 |
| Status | DIFFERENT | - |

**Analysis:**
- **SIGNIFICANT STRUCTURAL DIFFERENCES**
- aceengineercode: Complex YAML merging with `default_yaml` support
- pyintegrity: Simplified implementation with `update_deep()` function
- aceengineercode uses `yaml.Loader` (potentially unsafe)
- pyintegrity uses `yaml.safe_load()` (secure)
- aceengineercode supports chained YAML files via `default_yaml` key
- pyintegrity has self-contained `update_deep()` function

**Decision:** `MERGE_REQUIRED`
**Reason:** Both have unique features - need to combine safe_load with default_yaml support

---

### 15. data.py

| Metric | aceengineercode | pyintegrity |
|--------|-----------------|-------------|
| Lines | 963 | 963 |
| Status | DIFFERENT | - |

**Analysis:**
- Same line count, tiny difference
- Line 42 difference: `result = pd.read_excel(['io'],` vs `result = pd.read_excel(cfg_temp['io'],`
- aceengineercode version has a **BUG** - `['io']` should be `cfg_temp['io']`

**Decision:** `KEEP_DIGITALMODEL`
**Reason:** pyintegrity version has the bug fixed

---

## Part 3: Identical Files (No Action Required)

### Files in digitalmodel/common (24 files)

| File | Lines | Status |
|------|-------|--------|
| application_configuration.py | 59 | IDENTICAL |
| compare_tool_components.py | 186 | IDENTICAL |
| data_models_components.py | 205 | IDENTICAL |
| documentation_components.py | 91 | IDENTICAL |
| engineering_units.py | 29 | IDENTICAL |
| excel_utilities.py | 106 | IDENTICAL |
| fatigue_analysis_components.py | 703 | IDENTICAL |
| finance_components.py | 207 | IDENTICAL |
| front_end_components.py | 172 | IDENTICAL |
| log_file_analysis_components.py | 88 | IDENTICAL |
| ong_fd_components.py | 1111 | IDENTICAL |
| orcaflex_model_components.py | 1032 | IDENTICAL |
| time_series_components.py | 503 | IDENTICAL |
| viv_analysis_components.py | 326 | IDENTICAL |
| wellpath3D.py | 1985 | IDENTICAL |

### Files in pyintegrity/common

| File | Lines | Status |
|------|-------|--------|
| database.py | 774 | IDENTICAL |
| DataFrame_To_doc.py | 41 | IDENTICAL |
| fad.py | 63 | IDENTICAL |
| math_solvers.py | 88 | IDENTICAL |
| parallel_process_components.py | 170 | IDENTICAL |
| set_logging.py | 38 | IDENTICAL |
| update_deep.py | 35 | IDENTICAL |
| visualization_components.py (vs pyintegrity) | 240 | IDENTICAL |
| visualizations.py (vs pyintegrity) | 729 | IDENTICAL |

---

## Part 4: Files Unique to Each Repository

### Unique to aceengineercode/common (6 files)

| File | Lines | Notes |
|------|-------|-------|
| bsee_data_manager.py | - | BSEE-specific data management |
| __init__.py | - | Package initialization |

### Unique to digitalmodel/common (16 files)

| File | Lines | Notes |
|------|-------|-------|
| basic_statistics.py | - | Statistical utilities |
| cathodic_protection.py | - | CP calculations |
| code_dnvrph103_hydrodynamics_circular.py | - | DNV standard implementation |
| code_dnvrph103_hydrodynamics_rectangular.py | - | DNV standard implementation |
| cp_DNV_RP_F103_2010.py | - | DNV CP code |
| fatigue_analysis.py | - | Additional fatigue module |
| parallel_processing.py | - | Parallel utilities |
| path_utils.py | - | Path handling |
| pipe_properties.py | - | Pipe property calculations |
| plate_buckling.py | - | Buckling analysis |
| plotDefault.py | - | Default plotting |
| send_email.py | - | Email utilities |
| ship_design.py | - | Ship design calculations |
| ship_fatigue_analysis.py | - | Ship-specific fatigue |
| visualization_unused.py | - | Deprecated visualizations |
| visualizations_interactive.py | - | Interactive viz components |
| viv_fatigue_analysis_components.py | - | VIV fatigue analysis |

### Unique to pyintegrity/common (3 files)

| File | Lines | Notes |
|------|-------|-------|
| saveData.py | - | Data persistence |
| utilities.py | - | General utilities |
| yml_utilities.py | - | YAML handling utilities |

---

## Summary Decision Table

| File | Decision | Action |
|------|----------|--------|
| ETL_components.py | `KEEP_DIGITALMODEL` | Use digitalmodel/common version |
| FEAComponents.py | `KEEP_DIGITALMODEL` | Use digitalmodel/common version |
| shear7_model_components.py | `KEEP_DIGITALMODEL` | Use digitalmodel/common version |
| typical_riser_stack_up_calculations.py | `KEEP_DIGITALMODEL` | Use digitalmodel/common version |
| visualization_components.py | `KEEP_DIGITALMODEL` | Use digitalmodel/common version |
| visualizations.py | `KEEP_DIGITALMODEL` | Use digitalmodel/common version |
| API579_components.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common version |
| BS7910_critical_flaw_limits.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common version |
| ApplicationManager.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common version |
| DataFrame_To_Image.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common version |
| DataFrame_To_xlsx.py | `MERGE_REQUIRED` | Verify openpyxl compatibility |
| fracture_mechanics_components.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common version |
| pipe_components.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common version |
| ymlInput.py | `MERGE_REQUIRED` | Combine safe_load with default_yaml |
| data.py | `KEEP_DIGITALMODEL` | Use pyintegrity/common (bug fix) |

---

## Merge Required: Detailed Instructions

### 1. DataFrame_To_xlsx.py

**Current State:**
- aceengineercode uses `writer.save()` (older openpyxl API)
- pyintegrity uses `writer._save()` (newer openpyxl API)

**Merge Strategy:**
```python
# Add compatibility check
try:
    writer.save()
except AttributeError:
    writer._save()
```

**Or ensure openpyxl version consistency across both repos.**

---

### 2. ymlInput.py

**Current State:**
- aceengineercode: Supports `default_yaml` chaining, uses `yaml.Loader`
- pyintegrity: Uses `yaml.safe_load()`, has inline `update_deep()`

**Merge Strategy:**
Create unified version that:
1. Uses `yaml.safe_load()` for security
2. Supports `default_yaml` chaining from aceengineercode
3. Imports `update_deep` from dedicated module
4. Handles errors gracefully

**Proposed merged implementation:**
```python
from collections.abc import Mapping
import yaml
import sys

from common.update_deep import update_deep_dictionary

def ymlInput(applicationYml, customYml=None):
    with open(applicationYml, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    if customYml is not None:
        try:
            with open(customYml, 'r') as ymlfile:
                cfgCustomValues = yaml.safe_load(ymlfile)

            default_yaml_file = cfgCustomValues.get('default_yaml', None)

            if default_yaml_file is not None:
                with open(default_yaml_file, 'r') as fp:
                    default_file_data = yaml.safe_load(fp)
                cfgCustomValues = update_deep_dictionary(default_file_data, cfgCustomValues)

            cfg = update_deep_dictionary(cfg, cfgCustomValues)

        except Exception as e:
            print(f"Update Input file could not be loaded successfully: {e}")
            print("Running with default values")

    return cfg
```

---

## Recommended Migration Order

1. **Phase 1: Identical files** - Simply verify no action needed
2. **Phase 2: KEEP_DIGITALMODEL files** - Copy digitalmodel versions to aceengineercode
3. **Phase 3: MERGE_REQUIRED files** - Manual merge with testing
4. **Phase 4: Update imports** - Refactor import paths throughout codebase
5. **Phase 5: Testing** - Run full test suite to verify compatibility

---

## Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Import path changes | HIGH | Systematic search/replace with testing |
| openpyxl version mismatch | MEDIUM | Pin version in requirements.txt |
| YAML security (Loader vs safe_load) | MEDIUM | Use safe_load consistently |
| Feature regression | LOW | Comprehensive testing before merge |
| Bug in data.py fix | LOW | Already fixed in digitalmodel |

---

## Appendix: File Comparison Commands

```bash
# Compare any two files
diff file1.py file2.py

# Check if identical
diff -q file1.py file2.py

# Line count comparison
wc -l file1.py file2.py
```
