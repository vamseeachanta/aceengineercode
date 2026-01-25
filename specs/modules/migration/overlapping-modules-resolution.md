# Overlapping Modules Resolution

> Generated: 2026-01-24
> Status: Phase 4 - Merge Overlapping Modules

## Summary

Based on detailed comparison of aceengineercode and digitalmodel modules, the resolution for overlapping modules is:

| Module | aceengineercode | digitalmodel | Decision |
|--------|-----------------|--------------|----------|
| catenary | 1,313 lines | 4,240 lines | **KEEP DIGITALMODEL** |
| fatigue | 176 lines | 9,624 lines | **KEEP DIGITALMODEL** |
| fea_model | 1,136 lines | 1,331 lines | **KEEP DIGITALMODEL** |
| orcaflex | 605 lines | 45,770 lines | **KEEP DIGITALMODEL** |
| API_STD_2RD | 518 lines | 714 lines | **KEEP DIGITALMODEL** |
| DNV_OS_F101 | 434 lines | 703 lines | **KEEP DIGITALMODEL** |
| API579 | 28 lines | 290 lines | **KEEP DIGITALMODEL** |
| API_RP_2RD | 22 lines | 31 lines | **KEEP DIGITALMODEL** |
| ASMEB31 | 75 lines | 75 lines (identical) | **NO ACTION** |

## Resolution Details

### catenary
- **aceengineercode**: 9 files, 1,313 lines
- **digitalmodel**: 2 modules totaling 4,240 lines
- **Decision**: Keep digitalmodel - more comprehensive implementation
- **Action**: No migration needed

### fatigue (Fatigue_Curves)
- **aceengineercode**: 6 files, 176 lines
- **digitalmodel**: fatigue_analysis module with 9,624 lines
- **Decision**: Keep digitalmodel - 54x more comprehensive
- **Action**: No migration needed

### fea_model
- **aceengineercode**: 11 files, 1,136 lines
- **digitalmodel**: fea module with 1,331 lines
- **Decision**: Keep digitalmodel - slightly more complete, similar structure
- **Action**: No migration needed

### orcaflex (OrcaFlex_Post)
- **aceengineercode**: 9 files, 605 lines
- **digitalmodel**: 60+ files, 45,770 lines
- **Decision**: Keep digitalmodel - 75x larger, production-ready
- **Action**: orcaflex_post_process.py already migrated as utility

### API_STD_2RD
- **aceengineercode**: 18 files, 518 lines
- **digitalmodel**: 714 lines, more complete
- **Decision**: Keep digitalmodel
- **Action**: No migration needed

### DNV_OS_F101
- **aceengineercode**: 6 files, 434 lines
- **digitalmodel**: 703 lines, more mature
- **Decision**: Keep digitalmodel
- **Action**: No migration needed

### API579
- **aceengineercode**: 3 files, 28 lines (stub)
- **digitalmodel**: pyintegrity module with 290+ lines
- **Decision**: Keep digitalmodel - actual implementation vs stub
- **Action**: No migration needed

### API_RP_2RD
- **aceengineercode**: 1 file, 22 lines
- **digitalmodel**: 31 lines
- **Decision**: Keep digitalmodel
- **Action**: No migration needed

### ASMEB31
- **aceengineercode**: 2 files, 75 lines
- **digitalmodel**: Identical 75 lines
- **Decision**: Files are identical
- **Action**: No action required

## Conclusion

All overlapping modules have been resolved with **KEEP DIGITALMODEL** decisions. The digitalmodel repository already has more comprehensive, mature implementations of all engineering analysis modules.

### What Was Actually Migrated

Unique content from aceengineercode that was migrated:
1. **Plate_Buckling** - 15 files, 3,300 lines (completely unique)
2. **Common utilities** - 15 unique files, 6,803 lines
3. **Configuration files** - 170 YAML files
4. **Supporting files** - ASMEMethods.py, MaterialProperties.py, etc.

### No Further Merge Actions Required

The overlapping modules don't require merge because:
- digitalmodel versions are consistently more complete
- aceengineercode versions are subsets of digitalmodel functionality
- No unique functionality exists in aceengineercode overlapping modules
