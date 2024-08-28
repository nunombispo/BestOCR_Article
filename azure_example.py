from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
endpoint = "https://ocr-article.cognitiveservices.azure.com/"
key = "f5b45e2b2b3e4b24b3fc49010e50bce0"


def analyze_invoice():
    # Create a Document Intelligence client
    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Read PDF to bytes
    with open("bill-of-sale.pdf", "rb") as f:
        # Analyze the document
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-invoice", analyze_request=f, content_type="application/pdf"
        )
        invoices = poller.result()

        print(invoices.content)


if __name__ == "__main__":
    analyze_invoice()
