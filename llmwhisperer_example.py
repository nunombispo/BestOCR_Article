from unstract.llmwhisperer.client import LLMWhispererClient

# Initialize the client with your API key
client = LLMWhispererClient(base_url="https://llmwhisperer-api.unstract.com/v1",
                            api_key='<api_key>',
                            api_timeout=300)
# Extract tables from the PDF
result = client.whisper(file_path="bill-of-sale.pdf", output_mode='line-printer')
extracted_text = result["extracted_text"]
print(extracted_text)
