# WHO Early Warning System

An AI-powered early warning system for global health crises using multi-agent orchestration. Integrates with WHO guidelines and provides multi-channel alerts via WhatsApp and SMS.

## Features
- Multi-agent health monitoring system
- WHO-compliant risk assessment
- Cultural context awareness
- Multi-language support
- WhatsApp/SMS integration

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

# Example data
data = {
    "health_metrics": {
        "case_numbers": "increasing",
        "severity_levels": "moderate"
    }
}

# Get risk assessment
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

# Test communication interface
python src/communication_interface.py
```

## Project Structure
```
global_health_warning/
├── src/
│   ├── global_health_warning.py
│   └── communication_interface.py
├── docs/
│   └── implementation_guides/
├── examples/
└── README.md
```

## Contributing
Contributions welcome! Please read our contributing guidelines.

## License
MIT License - see LICENSE file for details
