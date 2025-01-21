import os
from autogen import ConversableAgent
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from enum import Enum

# Configuration - API Key
OPENAI_API_KEY = 
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class RiskLevel(Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    SEVERE = "SEVERE"
    CRITICAL = "CRITICAL"

class WHO_Categories(Enum):
    INFECTIOUS_DISEASE = "INFECTIOUS_DISEASE"
    ENVIRONMENTAL_HEALTH = "ENVIRONMENTAL_HEALTH"
    MENTAL_HEALTH = "MENTAL_HEALTH"
    NON_COMMUNICABLE = "NON_COMMUNICABLE"
    EMERGENCY_RESPONSE = "EMERGENCY_RESPONSE"

class GlobalHealthWarningSystem:
    def __init__(self, api_key: str):
        self.llm_config = {
            "config_list": [{
                "model": "gpt-3.5-turbo",
                "api_key": api_key
            }]
        }
        
        # Initialize core agents
        self.orchestrator = self._create_orchestrator()
        self.risk_assessor = self._create_risk_assessor()
        self.cultural_analyst = self._create_cultural_analyst()
        self.pattern_detector = self._create_pattern_detector()
        self.alert_generator = self._create_alert_generator()
        
        # Initialize regional experts for WHO regions
        self.regional_experts = self._create_regional_experts()
        
        # Risk assessment matrix
        self.risk_matrix = self._initialize_risk_matrix()
        
    def _create_orchestrator(self) -> ConversableAgent:
        """Creates the main orchestration agent"""
        return ConversableAgent(
            name="orchestrator",
            system_message="""You are the Global Health Warning System Orchestrator who:
            - Coordinates all analysis and response activities
            - Manages agent hierarchies and communication flows
            - Ensures WHO guidelines compliance
            - Maintains global risk assessment overview
            - Triggers appropriate response chains""",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
    
    def _create_risk_assessor(self) -> ConversableAgent:
        return ConversableAgent(
            name="risk_assessor",
            system_message="""You are the Risk Assessment Expert who:
            - Evaluates health threats based on WHO criteria
            - Calculates risk probabilities across regions
            - Generates detailed risk matrices
            - Tracks threat evolution patterns
            - Provides early warning indicators""",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )

    def _create_cultural_analyst(self) -> ConversableAgent:
        return ConversableAgent(
            name="cultural_analyst",
            system_message="""You are the Cultural Analysis Expert who:
            - Analyzes regional health behaviors
            - Identifies cultural barriers to health measures
            - Suggests culturally appropriate interventions
            - Maps community health practices
            - Ensures cultural sensitivity in responses""",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )

    def _create_pattern_detector(self) -> ConversableAgent:
        return ConversableAgent(
            name="pattern_detector",
            system_message="""You are the Pattern Detection Expert who:
            - Identifies early warning signs
            - Analyzes health data trends
            - Detects anomalous patterns
            - Maps disease spread patterns
            - Tracks intervention effectiveness""",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )

    def _create_alert_generator(self) -> ConversableAgent:
        return ConversableAgent(
            name="alert_generator",
            system_message="""You are the Alert Generation Expert who:
            - Creates multilingual health alerts
            - Crafts region-specific messages
            - Ensures clear communication
            - Manages alert priorities
            - Coordinates response protocols""",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )

    def _create_regional_experts(self) -> Dict[str, ConversableAgent]:
        """Creates WHO regional expert agents"""
        regions = ["AFRO", "AMRO", "EMRO", "EURO", "SEARO", "WPRO"]
        return {
            region: ConversableAgent(
                name=f"{region.lower()}_expert",
                system_message=f"""You are the WHO {region} Regional Expert who:
                - Specializes in {region}'s health systems
                - Understands regional challenges
                - Knows regional capabilities
                - Monitors local conditions
                - Provides regional context""",
                llm_config=self.llm_config,
                human_input_mode="NEVER"
            )
            for region in regions
        }

    def _initialize_risk_matrix(self) -> Dict[WHO_Categories, Dict[str, float]]:
        """Initializes the WHO risk assessment matrix"""
        return {
            category: {
                "base_risk": 0.0,
                "cultural_factor": 1.0,
                "regional_factor": 1.0,
                "temporal_factor": 1.0,
                "severity_score": 0.0
            }
            for category in WHO_Categories
        }

    async def analyze_health_patterns(
        self, 
        data: Dict[str, any], 
        region: str,
        timeframe: str
    ) -> Tuple[Dict[str, float], RiskLevel]:
        """Analyzes health-related patterns and generates risk assessment"""
        
        # Initial pattern analysis
        pattern_results = self.pattern_detector.initiate_chat(
            recipient=self.orchestrator,
            message=f"""Analyze health patterns for:
            Data: {data}
            Region: {region}
            Timeframe: {timeframe}
            
            Identify:
            1. Warning indicators
            2. Health trajectories
            3. Risk patterns
            4. Critical thresholds""",
            max_turns=2
        )
        
        # Cultural context analysis
        cultural_context = self.cultural_analyst.initiate_chat(
            recipient=self.regional_experts[region],
            message=f"""Analyze cultural context of:
            Pattern Analysis: {pattern_results.chat_history[-1]["content"]}
            Region: {region}
            
            Provide:
            1. Cultural interpretation
            2. Regional significance
            3. Local implications
            4. Response considerations""",
            max_turns=2
        )
        
        # Risk assessment
        risk_assessment = self.risk_assessor.initiate_chat(
            recipient=self.orchestrator,
            message=f"""Evaluate health risks based on:
            Patterns: {pattern_results.chat_history[-1]["content"]}
            Cultural Context: {cultural_context.chat_history[-1]["content"]}
            
            Generate:
            1. Risk scores by WHO category
            2. Overall threat level
            3. Confidence metrics
            4. Priority areas""",
            max_turns=2
        )
        
        # Update risk matrix
        self._update_risk_matrix(risk_assessment.chat_history[-1]["content"])
        
        # Generate alerts if needed
        if self._should_generate_alert(risk_assessment.chat_history[-1]["content"]):
            await self._generate_alerts(
                risk_assessment.chat_history[-1]["content"],
                region
            )
        
        return self._calculate_risk_metrics(risk_assessment.chat_history[-1]["content"])

    def _update_risk_matrix(self, risk_data: str):
        """Updates the risk assessment matrix with new data"""
        # Implementation for updating risk metrics
        pass

    def _should_generate_alert(self, risk_data: str) -> bool:
        """Determines if an alert should be generated"""
        # Implementation for alert threshold logic
        return True

    async def _generate_alerts(self, risk_data: str, region: str):
        """Generates appropriate alerts based on risk assessment"""
        alert_message = self.alert_generator.initiate_chat(
            recipient=self.orchestrator,
            message=f"""Generate health alert for:
            Risk Assessment: {risk_data}
            Region: {region}
            
            Include:
            1. Threat description
            2. Risk level
            3. Recommended actions
            4. Contact information""",
            max_turns=2
        )
        
        # Alert distribution would be handled by communication_interface.py
        return alert_message.chat_history[-1]["content"]

    def _calculate_risk_metrics(self, risk_data: str) -> Tuple[Dict[str, float], RiskLevel]:
        """Calculates final risk metrics"""
        # Implementation for risk calculation
        return ({}, RiskLevel.MODERATE)

def main():
    # Example usage
    system = GlobalHealthWarningSystem(OPENAI_API_KEY)
    
    # Sample health data
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
        },
        "environmental_factors": {
            "climate_conditions": "contributing",
            "population_density": "high",
            "travel_patterns": "significant"
        }
    }
    
    region = "AFRO"  # WHO African Region
    timeframe = "2024-Q1"
    
    import asyncio
    risk_metrics, risk_level = asyncio.run(
        system.analyze_health_patterns(data, region, timeframe)
    )
    
    print("\nWHO Early Warning System Analysis Complete!")
    print(f"\nRisk Level: {risk_level.value}")
    print("\nRisk Metrics:")
    for metric, value in risk_metrics.items():
        print(f"{metric}: {value}")

if __name__ == "__main__":
    main()
