from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

from azure.core.credentials import AzureKeyCredential

"""
see page:
https://learn.microsoft.com/zh-cn/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python&preserve-view=true
"""

endpoint = "YOUR_ENDPOINT"
key = "YOUR_KEY"


client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)


def analyze_layout(image_path):

    with open(image_path, "rb") as f:
        data = f.read()


    poller = client.begin_analyze_document(
        model_id="prebuilt-layout",
        body=data
    )

    result = poller.result()

    return result