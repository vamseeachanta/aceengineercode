# AceEngineerCode Retirement: Migration Plan (Cross-Reviewed)

## Executive Summary

**Objective:** Retire aceengineercode repository by migrating valuable assets.

**Migration Targets:**
- **digitalmodel** (PRIMARY) - All marine engineering code, analysis modules
- **worldenergydata** - Only BSEE/marine_safety content (mostly NO-OP - already exists)

---

## Critical Findings from Cross-Review

| Issue | Original Plan | Actual State |
|-------|---------------|--------------|
| File count | ~310 files | ~1,922 files |
| Timeline | Implied 2-3 weeks | **11 weeks required** |
| digitalmodel structure | "Primarily docs" | Already has `/src/` with 40+ modules |
| Module overlap | Not addressed | 5+ modules exist in BOTH repos |
| BSEE migration | 10-20 files | **NO-OP** - worldenergydata version more complete |
| Rollback plan | None | **Critical gap** |
| Integration tests | None | **Critical gap** |
| Git history | Not addressed | Use subtree merge |

---

## Phase 0: Preparation (Week 1)

### Pre-Migration Setup
1. Create backup tag: `git tag pre-migration-v1.0`
2. Create feature branch: `feature/aceengineercode-migration`
3. Create file inventory with line counts
4. Resolve dependency conflicts:
   - cx-Oracle: aceengineercode 8.3.0 vs digitalmodel 6.3.1
   - numpy upper bound differences
   - pandas version range alignment

### Rollback Checkpoints
- Full aceengineercode backup in git tag
- Document rollback procedure (2 hours for full rollback)

---

## Phase 1: Common Utilities Migration (Weeks 2-3)

### Source: `/common/` (39 Python files, 13,784 lines)

**Files that DON'T exist in digitalmodel (direct copy):**
| File | Lines | Description |
|------|-------|-------------|
| `API579_components.py` | 718 | API 579 calculations |
| `BS7910_critical_flaw_limits.py` | 980 | Fracture mechanics |
| `ong_fd_components.py` | 1,111 | O&G field development |
| `shear7_model_components.py` | - | SHEAR7 VIV analysis |
| `wellpath3D.py` | 1,985 | 3D wellpath calculations |

**Files that NEED MERGE (exist in both):**
| File | Action |
|------|--------|
| `visualization_components.py` | Compare and merge |
| `fatigue_analysis_components.py` | Merge with digitalmodel version |
| `viv_analysis_components.py` | Merge with digitalmodel version |
| `orcaflex_model_components.py` | Merge with 60+ digitalmodel files |

### Import Path Refactoring
260 import references to `common.*` across 76 files need updating:
```python
# FROM: relative imports
from common.database import get_db_connection

# TO: package imports
from digitalmodel.common.database import get_db_connection
```

---

## Phase 2: Configuration Migration (Week 4)

### Source: `/config/` + `/set_up/` (1,220 YAML files)

| Config Type | Target Path | Count |
|-------------|-------------|-------|
| API 579 | `/config/api579/` | ~50 files |
| Fatigue | `/config/fatigue/` | ~30 files |
| Pipeline | `/config/pipeline/` | ~40 files |
| VIV | `/config/viv/` | ~20 files |
| OrcaFlex | `/config/orcaflex/` | ~30 files |
| Environment | `/config/env/` | 84 files |

**Path Updates Required:**
Windows-style paths → Linux-compatible:
```python
# FROM
filename = os.path.join('data_manager\\sql', 'query.sql')
# TO
filename = Path('data_manager/sql/query.sql')
```

---

## Phase 3: Core Analysis Modules (Weeks 5-7)

### Unique Modules (Direct Migration)

| Module | Source | Target | Lines |
|--------|--------|--------|-------|
| `API579/` | `/custom/` | `/src/modules/api579/` | ~2,000 |
| `DNV_OS_F101/` | `/custom/` | `/src/modules/pipeline/` | ~1,500 |
| `API_RP_2RD/` | `/custom/` | `/src/modules/pipeline/` | ~800 |
| `ASMEB31/` | `/custom/` | `/src/modules/pipeline/` | ~600 |
| `Plate_Buckling/` | `/custom/` | `/src/modules/structural/` | ~1,000 |
| `fracture_mechanics/` | `/custom/` | `/src/modules/fracture/` | ~1,200 |

---

## Phase 4: Overlapping Modules - MERGE Required (Weeks 8-9)

### Modules Existing in BOTH Repositories

| Module | aceengineercode | digitalmodel | Strategy |
|--------|-----------------|--------------|----------|
| catenary | `/custom/catenary/` | `/modules/catenary_riser/` | Compare, keep best |
| viv_analysis | `/custom/viv_analysis/` | `/modules/viv_analysis/` | Merge features |
| fatigue | `/custom/Fatigue_Curves/` | `/modules/fatigue_analysis/` | Merge features |
| fea_model | `/custom/fea_model/` | `/modules/fea/` | Merge features |
| orcaflex | `/custom/OrcaFlex_Post/` | `/modules/orcaflex/` (60+ files) | Careful merge |

### Merge Procedure
1. Compare implementations file by file
2. Identify unique functionality in each
3. Create unified implementation
4. Write tests validating both behaviors

---

## Phase 5: BSEE Migration to worldenergydata (Week 10)

### Critical Finding: MOSTLY NO-OP

worldenergydata already has MORE COMPLETE BSEE implementation:
- More advanced web scrapers
- Same SQL queries (duplicate in legacy)
- `bsee_data_refresh.py` identical copy

**Only Migrate If Newer:**
| File | Action |
|------|--------|
| `/config/data_models/bsee_*.yml` | Compare timestamps, keep newer |
| 10 SQL query files | Verify identical, no action |
| `/config/ong_field_development/BSEE_*.yml` | Migrate 2 configs |

**Total BSEE Migration: ~5 files max**

---

## Phase 6: Entry Scripts & CLI (Week 10)

### Source: `/scripts/` (33 analysis scripts)

**Register in digitalmodel pyproject.toml:**
```toml
[project.scripts]
api579 = "digitalmodel.modules.api579.cli:main"
fatigue = "digitalmodel.modules.fatigue.cli:main"
viv = "digitalmodel.modules.viv.cli:main"
orcaflex = "digitalmodel.modules.orcaflex.cli:main"
```

---

## Phase 7: Validation & Cleanup (Week 11)

### Integration Testing Strategy

**Test Phases:**
1. **Import tests** - Verify all imports resolve
2. **Instantiation tests** - Classes/functions can be created
3. **Functional tests** - Core calculations produce expected results
4. **Integration tests** - Module interactions work

**Test Data:**
- `/data_manager/` - Sample data and SQL queries
- `/config/` - YAML test configurations

### Rollback Procedure (if needed)
```bash
# Full rollback (2 hours)
cd digitalmodel
git checkout main
git branch -D feature/aceengineercode-migration

# Restore aceengineercode
cd aceengineercode
git checkout pre-migration-v1.0
```

---

## Git History Preservation

### Use Subtree Merge
```bash
cd digitalmodel
git remote add aceengineercode /path/to/aceengineercode
git fetch aceengineercode
git merge -s ours --no-commit --allow-unrelated-histories aceengineercode/main
git read-tree --prefix=migrated/aceengineercode/ -u aceengineercode/main
git commit -m "Merge aceengineercode history"
```

---

## Files NOT to Migrate

| Content | Reason |
|---------|--------|
| `/ExistingCodes/` (~200 files) | Legacy/superseded, contains `z_superseded/` |
| `/ExistingCodes/websites/hairbyliz/` | Unrelated personal website |
| `/ExistingCodes/websites/dynamic_app_heroku/` | Demo Flask apps |
| `/.agent-os/` (46 files) | Project-specific Agent OS config |
| `/specs/` | Project-specific specifications |
| `*.backup*` files (7 found) | Backup artifacts |
| `/tests/` with client data | Potentially sensitive |

---

## Dependency Resolution Required

| Package | aceengineercode | digitalmodel | Resolution |
|---------|-----------------|--------------|------------|
| cx-Oracle | >=8.3.0 | ==6.3.1 | Test with 8.3.0 |
| numpy | >=1.24.0 | >=1.24.0,<2.0.0 | Use digitalmodel range |
| pandas | >=2.1.4 | >=2.0.0,<3.0.0 | Compatible |
| Python | >=3.9 | >=3.10 | Use 3.10 (more restrictive) |

---

## Final Structure: digitalmodel After Migration

```
digitalmodel/
├── src/digitalmodel/
│   ├── modules/
│   │   ├── api579/              # NEW - unique to aceengineercode
│   │   ├── orcaflex/            # MERGED - 60+ existing + new
│   │   ├── fatigue_analysis/    # MERGED - existing + new curves
│   │   ├── viv_analysis/        # MERGED - existing + SHEAR7
│   │   ├── pipeline/            # NEW - DNV/API/ASME standards
│   │   ├── riser/               # MERGED - catenary + vertical
│   │   ├── structural/          # NEW - buckling analysis
│   │   ├── fea/                 # MERGED - existing + new
│   │   ├── fracture/            # NEW - BS7910, fracture mechanics
│   │   └── drilling/            # NEW - wellpath3D
│   ├── common/
│   │   ├── (existing utils)
│   │   ├── api579_components.py # NEW
│   │   ├── bs7910_components.py # NEW
│   │   ├── ong_fd_components.py # NEW
│   │   └── wellpath3d.py        # NEW
│   └── cli/
│       └── (new entry points)
├── config/
│   ├── api579/                  # NEW
│   ├── fatigue/                 # NEW
│   ├── pipeline/                # NEW
│   └── (others)
└── docs/
    └── migration/
        └── aceengineercode-migration.md
```

---

## Timeline Summary

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| 0: Preparation | 1 week | Backups, inventory, dependency fixes |
| 1: Common Utils | 2 weeks | `/common/` migrated with imports fixed |
| 2: Configuration | 1 week | YAML configs migrated |
| 3: Core Modules | 3 weeks | Unique modules migrated |
| 4: Merge Modules | 2 weeks | Overlapping modules merged |
| 5: BSEE | < 1 week | ~5 files verified/migrated |
| 6: CLI | < 1 week | Entry points registered |
| 7: Validation | 1 week | Tests passing, docs updated |
| **TOTAL** | **11 weeks** | |

---

## Post-Migration

1. Archive aceengineercode with final tag: `archived-v1.0`
2. Update workspace-hub references
3. Update any CI/CD pipelines
4. Create migration documentation in digitalmodel
5. Monitor for issues for 2-4 weeks before deletion consideration

---

## Verification Checklist

- [ ] All imports resolve without errors
- [ ] API 579 analysis runs with sample data
- [ ] OrcaFlex integration works
- [ ] Fatigue analysis produces expected results
- [ ] VIV analysis executes correctly
- [ ] Pipeline standards calculations match baseline
- [ ] No regression in existing digitalmodel functionality
- [ ] worldenergydata BSEE module still works
- [ ] All CLI entry points functional
