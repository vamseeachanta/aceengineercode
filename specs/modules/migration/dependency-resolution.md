# Dependency Resolution Analysis

> Generated: 2026-01-24
> Status: Phase 0 - Preparation

## Summary of Conflicts

| Package | aceengineercode | digitalmodel | Resolution |
|---------|-----------------|--------------|------------|
| **Python** | >=3.9 | >=3.10 | Use **3.10** (more restrictive) |
| **cx-Oracle** | >=8.3.0 | ==6.3.1 | **CONFLICT** - Test with 8.3.0 |
| **numpy** | >=1.24.0 | >=1.24.0,<2.0.0 | Use digitalmodel range |
| **pandas** | >=2.1.4 | >=2.0.0,<3.0.0 | Compatible - keep >=2.1.4 |
| **Flask** | >=3.0.0 | Not present | Add to digitalmodel |
| **scikit-learn** | >=1.3.2 | ==1.3.2 | Compatible |
| **matplotlib** | >=3.7.4 | >=3.7.0,<4.0.0 | Compatible |
| **gunicorn** | >=21.2.0 | ==21.2.0 | Compatible |

## Critical Conflict: cx-Oracle

### Issue
- aceengineercode requires `cx-Oracle>=8.3.0` (2024 version)
- digitalmodel pins `cx-Oracle==6.3.1` (2019 version)

### Analysis
cx-Oracle 8.x has breaking changes from 6.x:
- Connection API changes
- Deprecated methods removed
- New features for Oracle Database 21c+

### Resolution Strategy
1. **Test aceengineercode code** with cx-Oracle 6.3.1 first
2. If incompatible, **upgrade digitalmodel** to cx-Oracle 8.3.0
3. Check Oracle client library compatibility

### Testing Commands
```bash
# In digitalmodel venv
uv pip install cx-Oracle==8.3.0
pytest tests/ -k oracle  # Run Oracle-specific tests
```

## Dependencies to Add to digitalmodel

These exist in aceengineercode but not in digitalmodel:

| Package | Version | Purpose |
|---------|---------|---------|
| `itsdangerous` | >=2.1.2 | Flask session security |
| (none critical) | - | Most deps already in digitalmodel |

## Dependencies Already in digitalmodel (No Action)

All major aceengineercode dependencies are present:
- numpy, pandas, matplotlib
- sqlalchemy, pymssql
- PyYAML, requests, beautifulsoup4
- scikit-learn
- Flask (not present but not needed for core analysis)

## pyproject.toml Updates Required

### digitalmodel pyproject.toml Changes

```toml
# Update cx-Oracle from pinned to range
# FROM: cx-Oracle==6.3.1
# TO:   cx-Oracle>=8.3.0

# Add Flask if web interface needed
# Flask>=3.0.0

# Verify Python version
requires-python = ">=3.10"  # Keep as-is
```

## Migration-Safe Dependency Set

Final recommended dependency set for merged repository:

```toml
dependencies = [
    # Core scientific computing
    "numpy>=1.24.0,<2.0.0",
    "pandas>=2.1.4,<3.0.0",
    "scipy>=1.10.0,<2.0.0",
    "scikit-learn>=1.3.2,<2.0.0",
    "matplotlib>=3.7.4,<4.0.0",

    # Database connectivity
    "sqlalchemy>=2.0.23,<3.0.0",
    "pymssql>=2.3.8",
    "cx-Oracle>=8.3.0",  # Updated

    # Data processing
    "PyYAML>=6.0.1,<7.0.0",
    "openpyxl>=3.1.0,<4.0.0",
    "xlrd>=2.0.0,<3.0.0",
    "xlsxwriter>=3.1.9,<4.0.0",

    # Web/HTTP (if needed)
    "requests>=2.31.0,<3.0.0",
    "beautifulsoup4>=4.12.3,<5.0.0",

    # CLI and utilities
    "Click>=8.1.7,<9.0.0",
    "python-dotenv>=1.1.0,<2.0.0",
    "loguru>=0.7.0,<1.0.0",
]
```

## Next Steps

1. [ ] Create test branch in digitalmodel with updated cx-Oracle
2. [ ] Run full test suite
3. [ ] Document any API changes needed
4. [ ] Update pyproject.toml after validation

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| cx-Oracle API changes | Medium | High | Pre-migration testing |
| numpy 2.0 breaking changes | Low | Medium | Upper bound prevents |
| Import path conflicts | High | Low | Systematic refactoring |
