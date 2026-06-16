import boto3, json, os
from dotenv import load_dotenv

load_dotenv()
bedrock = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
MODEL_ID = os.getenv("MODEL_ID")

def invoke_model(messages):
    # Lógica de formato Llama 3
    system_prompt = open("prompts/system_prompt.txt", "r").read()
    prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>{system_prompt}<|eot_id|>"
    for msg in messages:
        role = "user" if msg["role"] == "user" else "assistant"
        prompt += f"<|start_header_id|>{role}<|end_header_id|>\n\n{msg['content']}<|eot_id|>"
    prompt += "<|start_header_id|>assistant<|end_header_id|>"

    body = json.dumps({"prompt": prompt, "max_gen_len": 1024, "temperature": 0.1})
    response = bedrock.invoke_model(modelId=MODEL_ID, body=body)
    return json.loads(response["body"].read())["generation"]
