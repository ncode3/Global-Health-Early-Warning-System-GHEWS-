# WHO Early Warning System

An AI-powered early warning system for global health crises that analyzes emotional arcs across multiple languages to detect early signs of health emergencies. The system uses multi-agent orchestration to integrate WHO guidelines and Berlin Call principles for proactive health crisis prevention.

## Features
- Emotional arc analysis for early crisis detection
- Multi-agent pattern recognition system
- WHO-compliant risk assessment
- Cultural context awareness across regions
- Multi-language alert generation
- Dynamic risk matrices

## Architecture
- Pattern Recognition Agent: Detects early warning signs
- Cultural Context Agent: Handles regional/cultural analysis
- Health Risk Assessment Agent: Evaluates threats
- Alert Generation Agent: Creates warnings

## Quick Start
```bash
# Clone the repository
git clone https://github.com/ncode3/global_health_warning.git
cd global_health_warning

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Unix/MacOS

# Install dependencies
pip install -r requirements.txt
```

## Usage Example
```python
from global_health_warning import GlobalHealthWarningSystem

# Initialize system
system = GlobalHealthWarningSystem(your_api_key)

# Example health pattern data
data = {
    "health_metrics": {
        "case_numbers": "increasing",
        "severity_levels": "moderate",
        "spread_rate": "accelerating"
    },
    "regional_data": {
        "healthcare_capacity": "strained",
        "response_readiness": "moderate",
        "resource_availability": "limited"
    }
}

# Get analysis and risk assessment
risk_metrics, risk_level = system.analyze_health_patterns(
    data, 
    region="AFRO",
    timeframe="2024-Q1"
)
```

## Implementation Options
This system can be implemented at three levels:
1. No-Code (M365 Agent Builder)
2. Low-Code (Copilot Studio)
3. Pro-Code (Current Implementation)

See `/docs/implementation_guides` for details on each approach.

## Testing
```bash
# Test main system
python src/global_health_warning.py

# Test pattern analysis
python src/global_health_warning.py --test-patterns

# Test risk assessment
python src/global_health_warning.py --test-risk
```

## Project Structure
```
global_health_warning/
├── src/
│   ├── global_health_warning.py
│   └── communication_interface.py
├── docs/
│   └── implementation_guides/
│       ├── no_code_guide.md
│       ├── low_code_guide.md
│       └── pro_code_guide.md
├── examples/
│   ├── pattern_analysis_example.py
│   ├── risk_assessment_example.py
│   └── who_integration_example.py
├── tests/
│   └── test_who_system.py
├── requirements.txt
└── README.md
```

## Key Capabilities
- Early detection through emotional arc analysis
- Region-specific cultural context consideration
- WHO guideline compliance
- Multilingual support
- Autonomous agent collaboration
- Dynamic risk assessment

## Contributing
Contributions welcome! Please read our contributing guidelines.

## License
MIT License - see LICENSE file for details

## Acknowledgments
- WHO Guidelines Framework
- Berlin Call Principles
- AutoGen Framework for AI Agents
