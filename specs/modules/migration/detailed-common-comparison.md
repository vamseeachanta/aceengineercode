# Detailed Common Utilities Comparison

> Generated: 2025-01-24
> Source: /mnt/github/workspace-hub/aceengineercode/common/
> Destinations:
> - digitalmodel/src/digitalmodel/common/
> - digitalmodel/src/digitalmodel/modules/pyintegrity/common/

## Summary

| Category | Count |
|----------|-------|
| **UNIQUE (Must Migrate)** | 10 |
| **DUPLICATE (Need Comparison/Merge)** | 29 |
| **Already in digitalmodel/common Only** | 7 |
| **Already in pyintegrity/common Only** | 11 |
| **In Both digitalmodel Locations** | 11 |

---

## Complete File Comparison Table

| File | aceengineercode | digitalmodel/common | pyintegrity/common | Action |
|------|-----------------|---------------------|-------------------|--------|
| `__init__.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `API579_components.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `ApplicationManager.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `BS7910_critical_flaw_limits.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `DataFrame_To_Image.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `DataFrame_To_doc.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `DataFrame_To_xlsx.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `ETL_components.py` | YES | YES | NO | **DUPLICATE** - Compare/Merge |
| `FEAComponents.py` | YES | YES | NO | **DUPLICATE** - Compare/Merge |
| `application_configuration.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `bsee_data_manager.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `compare_tool_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `data.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `data_models_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `database.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `documentation_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `engineering_units.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `excel_utilities.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `fad.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `fatigue_analysis_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `finance_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `fracture_mechanics_components.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `front_end_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `log_file_analysis_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `math_solvers.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `ong_fd_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `orcaflex_model_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `parallel_process_components.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `pipe_components.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `set_logging.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `shear7_model_components.py` | YES | YES | NO | **DUPLICATE** - Compare/Merge |
| `time_series_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `typical_riser_stack_up_calculations.py` | YES | YES | NO | **DUPLICATE** - Compare/Merge |
| `update_deep.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |
| `visualization_components.py` | YES | YES | YES | **DUPLICATE** - Compare/Merge (Both) |
| `visualizations.py` | YES | YES | YES | **DUPLICATE** - Compare/Merge (Both) |
| `viv_analysis_components.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `wellpath3D.py` | YES | NO | NO | **UNIQUE** - Must Migrate |
| `ymlInput.py` | YES | NO | YES | **DUPLICATE** - Compare/Merge |

---

## Categorized Lists

### UNIQUE_FILES (Must Migrate - 18 files)

These files exist only in aceengineercode and must be migrated to digitalmodel:

| # | File | Description |
|---|------|-------------|
| 1 | `application_configuration.py` | Application configuration utilities |
| 2 | `bsee_data_manager.py` | BSEE data management |
| 3 | `compare_tool_components.py` | Comparison tool components |
| 4 | `data_models_components.py` | Data model components |
| 5 | `documentation_components.py` | Documentation generation |
| 6 | `engineering_units.py` | Engineering unit conversions |
| 7 | `excel_utilities.py` | Excel file utilities |
| 8 | `fatigue_analysis_components.py` | Fatigue analysis components |
| 9 | `finance_components.py` | Finance calculation components |
| 10 | `front_end_components.py` | Front-end UI components |
| 11 | `log_file_analysis_components.py` | Log file analysis |
| 12 | `ong_fd_components.py` | Oil & Gas fluid dynamics |
| 13 | `orcaflex_model_components.py` | OrcaFlex model components |
| 14 | `time_series_components.py` | Time series analysis |
| 15 | `viv_analysis_components.py` | VIV analysis components |
| 16 | `wellpath3D.py` | 3D well path calculations |

---

### DUPLICATE_FILES (Need Comparison/Merge - 21 files)

These files exist in both aceengineercode and digitalmodel. **Content comparison required** to determine merge strategy:

#### In pyintegrity/common Only (17 files)

| # | File | aceengineercode | pyintegrity/common |
|---|------|-----------------|-------------------|
| 1 | `__init__.py` | YES | YES |
| 2 | `API579_components.py` | YES | YES |
| 3 | `ApplicationManager.py` | YES | YES |
| 4 | `BS7910_critical_flaw_limits.py` | YES | YES |
| 5 | `DataFrame_To_Image.py` | YES | YES |
| 6 | `DataFrame_To_doc.py` | YES | YES |
| 7 | `DataFrame_To_xlsx.py` | YES | YES |
| 8 | `data.py` | YES | YES |
| 9 | `database.py` | YES | YES |
| 10 | `fad.py` | YES | YES |
| 11 | `fracture_mechanics_components.py` | YES | YES |
| 12 | `math_solvers.py` | YES | YES |
| 13 | `parallel_process_components.py` | YES | YES |
| 14 | `pipe_components.py` | YES | YES |
| 15 | `set_logging.py` | YES | YES |
| 16 | `update_deep.py` | YES | YES |
| 17 | `ymlInput.py` | YES | YES |

#### In digitalmodel/common Only (4 files)

| # | File | aceengineercode | digitalmodel/common |
|---|------|-----------------|---------------------|
| 1 | `ETL_components.py` | YES | YES |
| 2 | `FEAComponents.py` | YES | YES |
| 3 | `shear7_model_components.py` | YES | YES |
| 4 | `typical_riser_stack_up_calculations.py` | YES | YES |

#### In Both digitalmodel Locations (2 files)

| # | File | aceengineercode | digitalmodel/common | pyintegrity/common |
|---|------|-----------------|---------------------|-------------------|
| 1 | `visualization_components.py` | YES | YES | YES |
| 2 | `visualizations.py` | YES | YES | YES |

---

### FILES ONLY IN digitalmodel (Not in aceengineercode)

#### digitalmodel/common Exclusive Files

| # | File | Purpose |
|---|------|---------|
| 1 | `basic_statistics.py` | Statistical utilities |
| 2 | `cathodic_protection.py` | Cathodic protection calcs |
| 3 | `code_dnvrph103_hydrodynamics_circular.py` | DNV hydrodynamics (circular) |
| 4 | `code_dnvrph103_hydrodynamics_rectangular.py` | DNV hydrodynamics (rectangular) |
| 5 | `cp_DNV_RP_F103_2010.py` | DNV RP F103 standard |
| 6 | `fatigue_analysis.py` | Fatigue analysis |
| 7 | `parallel_processing.py` | Parallel processing |
| 8 | `path_utils.py` | Path utilities |
| 9 | `pipe_properties.py` | Pipe properties |
| 10 | `plate_buckling.py` | Plate buckling calcs |
| 11 | `plotDefault.py` | Default plotting |
| 12 | `send_email.py` | Email utilities |
| 13 | `ship_design.py` | Ship design calcs |
| 14 | `ship_fatigue_analysis.py` | Ship fatigue analysis |
| 15 | `visualization_unused.py` | Unused visualization |
| 16 | `visualizations_interactive.py` | Interactive visualizations |
| 17 | `viv_fatigue_analysis_components.py` | VIV fatigue analysis |
| 18 | `utilities/data_compare.py` | Data comparison |
| 19 | `utilities/data_extraction.py` | Data extraction |
| 20 | `utilities/histograms.py` | Histogram utilities |
| 21 | `utilities/visualization_plotly.py` | Plotly visualization |

#### pyintegrity/common Exclusive Files

| # | File | Purpose |
|---|------|---------|
| 1 | `saveData.py` | Data saving utilities |
| 2 | `utilities.py` | General utilities |
| 3 | `yml_utilities.py` | YAML utilities |

---

## Migration Recommendations

### Priority 1: UNIQUE FILES (Must Migrate)

These 16 files contain functionality not available in digitalmodel and should be migrated first:

1. **Engineering-Critical:**
   - `viv_analysis_components.py` - VIV analysis
   - `orcaflex_model_components.py` - OrcaFlex integration
   - `fatigue_analysis_components.py` - Fatigue analysis
   - `engineering_units.py` - Unit conversions

2. **Infrastructure:**
   - `application_configuration.py` - Configuration management
   - `excel_utilities.py` - Excel I/O
   - `data_models_components.py` - Data models

3. **Domain-Specific:**
   - `bsee_data_manager.py` - BSEE data
   - `wellpath3D.py` - Well path calcs
   - `ong_fd_components.py` - Oil & Gas fluid dynamics
   - `finance_components.py` - Financial calcs

4. **Utilities:**
   - `compare_tool_components.py` - Comparison tools
   - `documentation_components.py` - Documentation
   - `front_end_components.py` - UI components
   - `log_file_analysis_components.py` - Log analysis
   - `time_series_components.py` - Time series

### Priority 2: DUPLICATE FILES (Need Comparison)

For the 21 duplicate files, perform content diff to determine:
- **Identical:** Skip (already migrated)
- **aceengineercode newer:** Update digitalmodel version
- **digitalmodel newer:** Keep digitalmodel version
- **Different features:** Merge both versions

### Priority 3: Cross-Reference Check

Verify that aceengineercode modules importing from `common/` will work after migration:
- Check import statements in all aceengineercode modules
- Update import paths if needed
- Test module functionality post-migration

---

## Next Steps

1. [ ] Run content diff on all 21 DUPLICATE files
2. [ ] Determine merge strategy for each duplicate
3. [ ] Migrate 16 UNIQUE files to appropriate location
4. [ ] Update import statements across modules
5. [ ] Run test suite to validate migration
