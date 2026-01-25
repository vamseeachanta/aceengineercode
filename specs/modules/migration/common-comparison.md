# Common Directory Comparison Report

> Generated: 2026-01-24
> Purpose: Migration analysis for aceengineercode to digitalmodel

## Directory Paths

| Repository | Common Directory Path |
|------------|----------------------|
| aceengineercode | `/mnt/github/workspace-hub/aceengineercode/common/` |
| digitalmodel | `/mnt/github/workspace-hub/digitalmodel/src/digitalmodel/common/` |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Files UNIQUE to aceengineercode (MIGRATE) | 27 |
| Files UNIQUE to digitalmodel (KEEP) | 20 |
| Files in BOTH repositories (NEED MERGE) | 7 |
| **Total unique files across both** | **54** |

---

## Detailed File Comparison

### Files UNIQUE to aceengineercode (MIGRATE)

These files exist only in aceengineercode and should be migrated to digitalmodel:

| # | Filename | Description/Purpose |
|---|----------|---------------------|
| 1 | `__init__.py` | Package initialization file |
| 2 | `API579_components.py` | API 579 fitness-for-service components |
| 3 | `ApplicationManager.py` | Central application management system |
| 4 | `BS7910_critical_flaw_limits.py` | BS7910 standard critical flaw calculations |
| 5 | `DataFrame_To_Image.py` | DataFrame to image conversion utilities |
| 6 | `DataFrame_To_doc.py` | DataFrame to document conversion utilities |
| 7 | `DataFrame_To_xlsx.py` | DataFrame to Excel conversion utilities |
| 8 | `application_configuration.py` | Application configuration management |
| 9 | `bsee_data_manager.py` | BSEE (Bureau of Safety) data management |
| 10 | `compare_tool_components.py` | Data comparison tool utilities |
| 11 | `data.py` | Core data handling utilities |
| 12 | `data_models_components.py` | Data model definitions and components |
| 13 | `database.py` | Database connectivity and operations |
| 14 | `documentation_components.py` | Documentation generation utilities |
| 15 | `engineering_units.py` | Engineering unit conversions |
| 16 | `excel_utilities.py` | Excel file handling utilities |
| 17 | `fad.py` | Failure Assessment Diagram calculations |
| 18 | `fatigue_analysis_components.py` | Fatigue analysis calculations |
| 19 | `finance_components.py` | Financial analysis utilities |
| 20 | `fracture_mechanics_components.py` | Fracture mechanics calculations |
| 21 | `front_end_components.py` | Frontend/UI components |
| 22 | `log_file_analysis_components.py` | Log file analysis utilities |
| 23 | `math_solvers.py` | Mathematical solver algorithms |
| 24 | `ong_fd_components.py` | Oil & gas field development components |
| 25 | `orcaflex_model_components.py` | OrcaFlex integration components |
| 26 | `parallel_process_components.py` | Parallel processing utilities |
| 27 | `pipe_components.py` | Pipeline analysis components |
| 28 | `set_logging.py` | Logging configuration utilities |
| 29 | `time_series_components.py` | Time series analysis utilities |
| 30 | `update_deep.py` | Deep update utilities for nested structures |
| 31 | `viv_analysis_components.py` | Vortex-induced vibration analysis |
| 32 | `wellpath3D.py` | 3D wellpath calculations |
| 33 | `ymlInput.py` | YAML input processing utilities |
| 34 | `exe/wkhtmltopdf.exe` | PDF generation executable (Windows) |

---

### Files UNIQUE to digitalmodel (KEEP)

These files exist only in digitalmodel and should be preserved:

| # | Filename | Description/Purpose |
|---|----------|---------------------|
| 1 | `basic_statistics.py` | Basic statistical analysis functions |
| 2 | `cathodic_protection.py` | Cathodic protection calculations |
| 3 | `code_dnvrph103_hydrodynamics_circular.py` | DNV-RP-H103 hydrodynamics (circular) |
| 4 | `code_dnvrph103_hydrodynamics_rectangular.py` | DNV-RP-H103 hydrodynamics (rectangular) |
| 5 | `cp_DNV_RP_F103_2010.py` | DNV-RP-F103 cathodic protection |
| 6 | `fatigue_analysis.py` | Fatigue analysis (different from aceengineercode) |
| 7 | `parallel_processing.py` | Parallel processing (different name) |
| 8 | `path_utils.py` | Path utility functions |
| 9 | `pipe_properties.py` | Pipe property calculations |
| 10 | `plate_buckling.py` | Plate buckling analysis |
| 11 | `plotDefault.py` | Default plotting configurations |
| 12 | `send_email.py` | Email notification utilities |
| 13 | `ship_design.py` | Ship design calculations |
| 14 | `ship_fatigue_analysis.py` | Ship-specific fatigue analysis |
| 15 | `visualization_unused.py` | Deprecated visualization code |
| 16 | `visualizations_interactive.py` | Interactive visualization functions |
| 17 | `viv_fatigue_analysis_components.py` | VIV fatigue analysis |
| 18 | `utilities/data_compare.py` | Data comparison utilities (subfolder) |
| 19 | `utilities/data_extraction.py` | Data extraction utilities (subfolder) |
| 20 | `utilities/histograms.py` | Histogram generation utilities |
| 21 | `utilities/visualization_plotly.py` | Plotly visualization utilities |

---

### Files in BOTH Repositories (NEED MERGE)

These files exist in both repositories and require careful merge analysis:

| # | Filename | Action Required |
|---|----------|-----------------|
| 1 | `ETL_components.py` | **MERGE** - Compare implementations |
| 2 | `FEAComponents.py` | **MERGE** - Compare implementations |
| 3 | `shear7_model_components.py` | **MERGE** - Compare implementations |
| 4 | `typical_riser_stack_up_calculations.py` | **MERGE** - Compare implementations |
| 5 | `visualization_components.py` | **MERGE** - Compare implementations |
| 6 | `visualizations.py` | **MERGE** - Compare implementations |

---

## Files Requiring Merge Analysis

### 1. ETL_components.py

| Repository | Path |
|------------|------|
| aceengineercode | `common/ETL_components.py` |
| digitalmodel | `src/digitalmodel/common/ETL_components.py` |

**Recommended Action:** Compare line counts, function signatures, and capabilities to determine which version is more complete or if a true merge is needed.

### 2. FEAComponents.py

| Repository | Path |
|------------|------|
| aceengineercode | `common/FEAComponents.py` |
| digitalmodel | `src/digitalmodel/common/FEAComponents.py` |

**Recommended Action:** Compare FEA analysis capabilities in both implementations.

### 3. shear7_model_components.py

| Repository | Path |
|------------|------|
| aceengineercode | `common/shear7_model_components.py` |
| digitalmodel | `src/digitalmodel/common/shear7_model_components.py` |

**Recommended Action:** Compare Shear7 VIV analysis implementations.

### 4. typical_riser_stack_up_calculations.py

| Repository | Path |
|------------|------|
| aceengineercode | `common/typical_riser_stack_up_calculations.py` |
| digitalmodel | `src/digitalmodel/common/typical_riser_stack_up_calculations.py` |

**Recommended Action:** Compare riser stack-up calculation implementations.

### 5. visualization_components.py

| Repository | Path |
|------------|------|
| aceengineercode | `common/visualization_components.py` |
| digitalmodel | `src/digitalmodel/common/visualization_components.py` |

**Recommended Action:** Compare visualization capabilities and merge features.

### 6. visualizations.py

| Repository | Path |
|------------|------|
| aceengineercode | `common/visualizations.py` |
| digitalmodel | `src/digitalmodel/common/visualizations.py` |

**Recommended Action:** Compare visualization functions and merge if necessary.

---

## Similar Files with Different Names

These files may have overlapping functionality despite different names:

| aceengineercode | digitalmodel | Potential Overlap |
|-----------------|--------------|-------------------|
| `parallel_process_components.py` | `parallel_processing.py` | Parallel processing functionality |
| `fatigue_analysis_components.py` | `fatigue_analysis.py` | Fatigue analysis calculations |
| `pipe_components.py` | `pipe_properties.py` | Pipe-related calculations |
| `viv_analysis_components.py` | `viv_fatigue_analysis_components.py` | VIV analysis functionality |
| `compare_tool_components.py` | `utilities/data_compare.py` | Data comparison utilities |

**Recommendation:** Review these pairs for potential consolidation during migration.

---

## Migration Recommendations

### Phase 1: Direct Migration (No Conflicts)
Migrate these 27 unique aceengineercode files directly:
- All files listed in "Files UNIQUE to aceengineercode" section
- Create `__init__.py` in digitalmodel common if needed

### Phase 2: Merge Analysis Required
For the 6 overlapping files:
1. Generate diff reports for each pair
2. Identify unique functions in each version
3. Create merged versions preserving all functionality
4. Update imports and references

### Phase 3: Similar File Consolidation
Review the 5 similar file pairs for potential consolidation:
1. Compare function signatures and capabilities
2. Decide on naming conventions
3. Consolidate or maintain as separate modules

---

## Notes

- The `exe/wkhtmltopdf.exe` in aceengineercode is a Windows binary for PDF generation
- digitalmodel has a `utilities/` subfolder structure that aceengineercode lacks
- digitalmodel common directory does NOT have an `__init__.py` file
- `__pycache__` directories in digitalmodel contain compiled Python files (excluded from migration)

---

## Next Steps

1. [ ] Run detailed diff analysis on 6 overlapping files
2. [ ] Review similar file pairs for consolidation opportunities
3. [ ] Create migration script for unique files
4. [ ] Plan merge strategy for overlapping files
5. [ ] Update import statements in dependent modules
6. [ ] Test migrated functionality
