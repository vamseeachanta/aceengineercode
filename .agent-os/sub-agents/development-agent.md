# Development Agent Configuration

> Repository: AceEngineerCode
> Created: 2025-07-31
> Version: 1.0.0

## Agent Purpose

This development agent provides marine offshore structural engineering analysis development workflows specifically optimized for AceEngineerCode platform, focusing on API 579, OrcaFlex integration, VIV analysis, and specialized engineering calculations.

## Development Patterns

### Engineering Analysis Modules
- **Modular Architecture**: 25+ specialized analysis modules with Application Manager
- **Configuration**: YAML-based configuration system with templates
- **Industry Standards**: API 579, DNVGL, ASME compliance implementation
- **Integration**: Seamless OrcaFlex API connectivity

### Analysis Development Workflow
- **Module Structure**: Independent analysis modules with common utilities
- **Data Processing**: NumPy/SciPy for mathematical computations
- **Visualization**: D3.js and matplotlib integration
- **Database**: SQL Server connectivity for project data

## Engineering Standards

### Code Organization
```python
# Module template for engineering analysis
class AnalysisModule:
    def __init__(self, config_path):
        self.config = self.load_yaml_config(config_path)
        self.results = {}
    
    def analyze(self, input_data):
        # Industry standard implementation
        return self.process_analysis(input_data)
```

### Industry Compliance
- **API 579**: Complete fitness-for-service implementation
- **OrcaFlex**: Dynamic analysis integration
- **DNVGL Standards**: Offshore structural analysis
- **Quality Assurance**: Extensive validation against known solutions

## Team Synchronization

### Engineering Collaboration
- **Shared Configurations**: YAML-based analysis parameters
- **Version Control**: Git integration for code and configurations
- **Documentation**: Engineering calculation documentation
- **Standards**: Consistent engineering calculation patterns