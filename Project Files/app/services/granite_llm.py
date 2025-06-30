import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import SecretStr

# Load environment variables
load_dotenv()

# Check for required environment variables
required_env_vars = ["WATSONX_MODEL_ID", "WATSONX_PROJECT_ID", "WATSONX_URL", "WATSONX_API_KEY"]
missing = [var for var in required_env_vars if os.getenv(var) is None]
if missing:
    raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")

# Initialize IBM Watsonx LLM
watsonx_llm = WatsonxLLM(
    model_id=os.getenv("WATSONX_MODEL_ID"),
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    url=os.getenv("WATSONX_URL"),
    apikey=SecretStr(os.getenv("WATSONX_API_KEY")),
    params={
        "max_new_tokens": 300,
        "temperature": 0.7,
        "decoding_method": "sample"
    }
)

# === GENERIC ASK FUNCTION ===
def ask_granite(prompt: str) -> str:
    try:
        prompt_template = PromptTemplate(
            input_variables=["prompt"],
            template="{prompt}"
        )
        llm_chain = LLMChain(prompt=prompt_template, llm=watsonx_llm)
        return llm_chain.run(prompt=prompt).strip()
    except Exception as e:
        print("Error in ask_granite:", e)
        return "Error: Could not process request."

# === ECO TIP FUNCTION ===
def generate_eco_tip(topic: str = "daily life") -> str:
    try:
        prompt_template = PromptTemplate(
            input_variables=["topic"],
            template="Give an eco-friendly tip related to {topic}."
        )
        llm_chain = LLMChain(prompt=prompt_template, llm=watsonx_llm)
        return llm_chain.run(topic=topic).strip()
    except Exception as e:
        print("Error in generate_eco_tip:", e)
        return "Could not generate eco tip."
