# encode = utf-8

question_1_1 = """
# DRAG DROP -
You have 100 chatbots that each has its own Language Understanding model.
Frequently, you must add the same phrases to each model.
You need to programmatically update the Language Understanding models to include the new phrases.
How should you complete the code? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

# Select and Place:
Values:
AddPhraseListAsync
Phraselist
PhraselistCreateObject
Phrases
SavePhraseListAsync
UpdatePhraseListAsync

# Answer Area
var phraselistId = await client.Features.______
(appId, versionId, new ______
{
    EnabledForAllModels = false,
    IsExchangeable = true,
    Name = "PL1",
    Phrases = "item1, item2, item3, item4, item5"

});

# Correct Answer
AddPhraseListAsync, PhraselistCreateObject

Box 1: AddPhraseListAsync -
Example: Add phraselist feature -
var phraselistId = await client.Features.AddPhraseListAsync(appId, versionId, new PhraselistCreateObject
{
EnabledForAllModels = false,
IsExchangeable = true,
Name = "QuantityPhraselist",
Phrases = "few,more,extra"
});
Box 2: PhraselistCreateObject -

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/client-libraries-rest-api
"""

question_1_2 = """
# DRAG DROP -
You plan to use a Language Understanding application named app1 that is deployed to a container.
App1 was developed by using a Language Understanding authoring resource named lu1.
App1 has the versions shown in the following table.
___________________________________________
| Version | Trained date | Published date |
| V1.2    | None         | None           |
| V1.1    | 2020-10-01   | None           |
| V1.0    | 2020-09-01   | 2020-09-15     |
___________________________________________
You need to create a container that uses the latest deployable version of app1.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and
arrange them in the correct order.

# Select and Place:
Actions
Run a container that has version set as an environment variable.
Export the model by using the Export as JSON option.
Select v1.1 of app1.
Run a container and mount the model file.
Select v1.0 of app1.
Export the model by using the Export for containers (GZIP) option.
Select v1.2 of app1.

# Correct Answer
Export the model by using the Export for containers (GZIP) option.
Select v1.1 of app1.
Run a container that has version set as an environment variable.

Step 1: Export the model using the Export for containers (GZIP) option.
Export versioned app's package from LUIS portal
The versioned app's package is available from the Versions list page.
1. Sign on to the LUIS portal.
2. Select the app in the list.
3. Select Manage in the app's navigation bar.
4. Select Versions in the left navigation bar.
5. Select the checkbox to the left of the version name in the list.
6. Select the Export item from the contextual toolbar above the list.
7. Select Export for container (GZIP).
8. The package is downloaded from the browser.
Step 2: Select v1.1 of app1.
A trained or published app packaged as a mounted input to the container with its associated App ID.
Step 3: Run a contain and mount the model le.
Run the container, with the required input mount and billing settings.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-container-howto
"""

question_1_3 = """
# QUESTION
You need to build a chatbot that meets the following requirements:
✑ Supports chit-chat, knowledge base, and multilingual models
✑ Performs sentiment analysis on user messages
✑ Selects the best language model automatically
What should you integrate into the chatbot?
A. QnA Maker, Language Understanding, and Dispatch
B. Translator, Speech, and Dispatch
C. Language Understanding, Text Analytics, and QnA Maker
D. Text Analytics, Translator, and Dispatch

# Correct Answer:
C

Language Understanding: An AI service that allows users to interact with your applications, bots, and IoT devices by using natural language.
QnA Maker is a cloud-based Natural Language Processing (NLP) service that allows you to create a natural conversational layer over your data. It is used to nd the most appropriate answer for any input from your custom knowledge base (KB) of information.
Text Analytics: Mine insights in unstructured text using natural language processing (NLP) no machine learning expertise required. Gain a deeper understanding of customer opinions with sentiment analysis. The Language Detection feature of the Azure Text Analytics REST API evaluates text input
Incorrect Answers:
A, B, D: Dispatch uses sample utterances for each of your bot's different tasks (LUIS, QnA Maker, or custom), and builds a model that can be used to properly route your user's request to the right task, even across multiple bots.

# Reference:
https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/ https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/overview/overview
"""

question_1_4 = """
# QUESTION
Your company wants to reduce how long it takes for employees to log receipts in expense reports. All the receipts are in English.
You need to extract top-level information from the receipts, such as the vendor and the transaction total. The solution must minimize development effort.
Which Azure service should you use?
A. Custom Vision
B. Personalizer
C. Form Recognizer
D. Computer Vision

# Correct Answer:
C
Azure Form Recognizer is a cognitive service that lets you build automated data processing software using machine learning technology.
Identify and extract text, key/value pairs, selection marks, tables, and structure from your documents the service outputs structured data that includes the relationships in the original le, bounding boxes, confidence and more.
Form Recognizer is composed of custom document processing models, prebuilt models for invoices, receipts, IDs and business cards, and the layout model.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer
"""

question_1_5 = """
# HOTSPOT -
You need to create a new resource that will be used to perform sentiment analysis and optical character recognition (OCR). The solution must meet the following requirements:
✑ Use a single key and endpoint to access multiple services.
✑ Consolidate billing for future services that you might use.
✑ Support the use of Computer Vision in the future.
How should you complete the HTTP request to create the new resource? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

# Hot Area:
______(PATCH / POST / PUT) https://management.azure.com/subscriptions/xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/RG1/providers/Microsoft.CognitiveServices/accounts/CS1?api-version=2017-04-18
{
  "location": "West US",
  "kind": "______(CognitiveServices / ComputerVision / TextAnalytics)",
  "sku": {
    "name": "S0"
  },
  "properties": {},
  “identity”: {
    "type": "SystemAssigned"
    
  }
}

# Correct Answer
PUT, CognitiveServices

Box 1: PUT -
Sample Request: PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test-rg/providers/Microsoft.DeviceUpdate/accounts/contoso?api-version=2020-03-01-preview
Incorrect Answers:
PATCH is for updates.
Box 2: CognitiveServices -
Microsoft Azure Cognitive Services provide us to use its pre-trained models for various Business Problems related to Machine Learning.
List of Different Services are:
✑ Decision
✑ Language (includes sentiment analysis)
✑ Speech
✑ Vision (includes OCR)
✑ Web Search

# Reference:
https://docs.microsoft.com/en-us/rest/api/deviceupdate/resourcemanager/accounts/create
https://www.analyticsvidhya.com/blog/2020/12/microsoft-azure-cognitive-services-api-for-ai-development
"""

question_1_6 = """
# QUESTION
You are developing a new sales system that will process the video and text from a public-facing website.
You plan to monitor the sales system to ensure that it provides equitable results regardless of the user's location or background.
Which two responsible AI principles provide guidance to meet the monitoring requirements? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. transparency
B. fairness
C. inclusiveness
D. reliability and safety
E. privacy and security

# Correct Answer:
BD

AI systems should treat all people fairly.
AI systems should perform reliably and safely.

Reference:
https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/responsible-ai
"""

question_1_7 = """
# DRAG DROP -
You plan to use containerized versions of the Anomaly Detector API on local devices for testing and in on-premises datacenters.
You need to ensure that the containerized deployments meet the following requirements:
✑ Prevent billing and API information from being stored in the command-line histories of the devices that run the container.
✑ Control access to the container images by using Azure role-based access control (Azure RBAC).
Which four actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.
NOTE: More than one order of answer choices is correct. You will receive credit for any of the correct orders you select.

# Select and Place:
Create a custom Dockerfile.
Pull the Anomaly Detector container image.
Distribute a docker run script.
Push the image to an Azure container registry.
Build the image.
Push the image to Docker Hub.

# Correct Answer:
Pull the Anomaly Detector container image.
Create a custom Dockerfile.
Push the image to an Azure container registry.
Distribute a docker run script.

Step 1: Pull the Anomaly Detector container image.
Step 2: Create a custom Dockerfile.
Step 3: Push the image to an Azure container registry.
To push an image to an Azure Container registry, you must rst have an image.
Step 4: Distribute the docker run script
Use the docker run command to run the containers.

# Reference:
https://docs.microsoft.com/en-us/azure/container-registry/container-registry-intro
"""

question_1_8 = """
# HOTSPOT -
You plan to deploy a containerized version of an Azure Cognitive Services service that will be used for text analysis.
You configure https://contoso.cognitiveservices.azure.com as the endpoint URI for the service, and you pull the latest version of the Text Analytics Sentiment Analysis container.
You need to run the container on an Azure virtual machine by using Docker.
How should you complete the command? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

# Hot Area:
docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \  
______ \ 
(
http://contoso.blob.core.windows.net
https://contoso.cognitiveservices.azure.com
mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment
)
Eula=accept \ 
Billing= ______ \ 
(
http://contoso.blob.core.windows.net
https://contoso.cognitiveservices.azure.com
mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment
)
apiKey=xxxxxxxxxxxxxxxxxx

# Correct Answer:
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment, https://contoso.cognitiveservices.azure.com

Box 1: mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment
To run the Sentiment Analysis v3 container, execute the following docker run command. docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \ mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment \ Eula=accept \ Billing={ENDPOINT_URI} \ ApiKey={API_KEY} is the endpoint for accessing the Text Analytics API. https://<your-custom-subdomain>.cognitiveservices.azure.com
Box 2: https://contoso.cognitiveservices.azure.com {ENDPOINT_URI} is the endpoint for accessing the Text Analytics API: https://<your-custom-subdomain>.cognitiveservices. The endpoint for accessing the Text Analytics API.azure.com -

Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-install-containers?tabs=sentiment
"""

question_1_9 = """
# QUESTION
You have the following C# method for creating Azure Cognitive Services resources programmatically.
static void create_resource (CognitiveServicesManagementClient client, string resource_name, string kind, string account_tier, string location)
{
  CognitiveServiceAccount parameters = 
    new CognitiveServicesAccount(null, null, kind, location, resource_name, new CognitiveServicesAccountProperties(), new Sku(account_tier));
    var result = client.Accounts.Create(resource_group_name, account_tier, parameters);
}

You need to call the method to create a free Azure resource in the West US Azure region. The resource will be used to generate captions of images automatically.
Which code should you use?
A. create_resource(client, "res1", "ComputerVision", "F0", "westus")
B. create_resource(client, "res1", "CustomVision.Prediction", "F0", "westus")
C. create_resource(client, "res1", "ComputerVision", "S0", "westus")
D. create_resource(client, "res1", "CustomVision.Prediction", "S0", "westus")

# Correct Answer:
B

Many of the Cognitive Services have a free tier you can use to try the service. To use the free tier, use F0 as the SKU for your resource.
There are two tiers of keys for the Custom Vision service. You can sign up for a F0 (free) or S0 (standard) subscription through the Azure portal.
Incorrect Answers:
A: There is no free tier (F0) for ComputerVision.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account-client-library?pivots=programming-language-csharp 
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/limits-and-quotas
"""

question_1_10 = """
# QUESTION 
You successfully run the following HTTP request.
POST https://management.azure.com/subscriptions/18c51a87-3a69-47a8-aedc-a54745f708a1/resourceGroups/RG1/providers/Microsoft.CognitiveServices/accounts/contoso1/regenerateKey?api-version=2017-04-18
Body {"keyName": "Key2"}
What is the result of the request?
A. A key for Azure Cognitive Services was generated in Azure Key Vault.
B. A new query key was generated.
C. The primary subscription key and the secondary subscription key were rotated.
D. The secondary subscription key was reset.

# Correct Answer:
B

Accounts - Regenerate Key regenerates the specified account key for the specified Cognitive Services account.
Syntax:
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/regenerateKey?api-version=2017-04-18

Reference:
https://docs.microsoft.com/en-us/rest/api/cognitiveservices/accountmanagement/accounts/regeneratekey
"""

question_1_11 = """
# QUESTION 
You build a custom Form Recognizer model.
You receive sample les to use for training the model as shown in the following table.
_________________________
| Name  | Type | Size   |
| File1 | PDF  | 20 MB  |
| File2 | MP4  | 100 MB |
| File3 | JPG  | 20 MB  |
| File4 | PDF  | 100 MB |
| File5 | GIF  | 2 MB   |
| File6 | JPG  | 40 MB  |
-------------------------

Which three les can you use to train the model? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.
A. File1
B. File2
C. File3
D. File4
E. File5
F. File6

# Correct Answer:
ACF

Input requirements -
Form Recognizer works on input documents that meet these requirements:
Format must be JPG, PNG, PDF (text or scanned), or TIFF. Text-embedded PDFs are best because there's no possibility of error in character extraction and location.
File size must be less than 50 MB.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/overview
"""

question_1_12 = """
# QUESTION 
A customer uses Azure Cognitive Search.
The customer plans to enable a server-side encryption and use customer-managed keys (CMK) stored in Azure.
What are three implications of the planned change? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.
A. The index size will increase.
B. Query times will increase.
C. A self-signed X.509 certificate is required.
D. The index size will decrease.
E. Query times will decrease.
F. Azure Key Vault is required.

# Correct Answer:
ABE

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-security-overview
"""

question_1_13 = """
# QUESTION 
You are developing a new sales system that will process the video and text from a public-facing website.
You plan to notify users that their data has been processed by the sales system.
Which responsible AI principle does this help meet?
A. transparency
B. fairness
C. inclusiveness
D. reliability and safety

# Correct Answer:
D

Reference:
https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/responsible-ai
"""

question_1_14 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a web app named app1 that runs on an Azure virtual machine named vm1. Vm1 is on an Azure virtual network named vnet1.
You plan to create a new Azure Cognitive Search service named service1.
You need to ensure that app1 can connect directly to service1 without routing trac over the public internet.

Solution: You deploy service1 and a public endpoint to a new virtual network, and you configure Azure Private Link.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B
The Azure Private Link should use a private endpoint, not a public endpoint.
Private Link service can be accessed from approved private endpoints in any public region.

# Reference:
https://docs.microsoft.com/en-us/azure/private-link/private-link-overview
"""

question_1_15 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a web app named app1 that runs on an Azure virtual machine named vm1. Vm1 is on an Azure virtual network named vnet1.
You plan to create a new Azure Cognitive Search service named service1.
You need to ensure that app1 can connect directly to service1 without routing trac over the public internet.

Solution: You deploy service1 and a public endpoint, and you configure an IP firewall rule.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B
Instead deploy service1 and a private (not public) endpoint to a new virtual network, and you configure Azure Private Link.

# Reference:
https://docs.microsoft.com/en-us/azure/private-link/private-link-overview
"""

question_1_16 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a web app named app1 that runs on an Azure virtual machine named vm1. Vm1 is on an Azure virtual network named vnet1.
You plan to create a new Azure Cognitive Search service named service1.
You need to ensure that app1 can connect directly to service1 without routing trac over the public internet.

Solution: You deploy service1 and a public endpoint, and you configure a network security group (NSG) for vnet1.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B
Instead deploy service1 and a private (not public) endpoint to a new virtual network, and you configure Azure Private Link.

# Reference:
https://docs.microsoft.com/en-us/azure/private-link/private-link-overview
"""

question_1_17 = """
# QUESTION
You plan to perform predictive maintenance.
You collect IoT sensor data from 100 industrial machines for a year. Each machine has 50 different sensors that generate data at one-minute
intervals. In total, you have 5,000 time series datasets.
You need to identify unusual values in each time series to help predict machinery failures.
Which Azure service should you use?
A. Anomaly Detector
B. Cognitive Search
C. Form Recognizer
D. Custom Vision

# Correct Answer:
A
"""

question_1_18 = """
# HOTSPOT -
You are developing a streaming Speech to Text solution that will use the Speech SDK and MP3 encoding.
You need to develop a method to convert speech to text for streaming MP3 data.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

# Hot Area:
var audioFormat = ______ (AudioStreamContainerFormat.MP3);
                  (AudioConfig.SetProperty / AudioStreamFormat.getCompressedFormat / AudioStreamFormat.GetWaveFormatPCM / PullAudioInputStream)
var speechConfig = SpeechConfig.FromSubscription("18c51a87-3a69-47a8-aedc-a54745f708a1", "westus");
var audioConfig = AudioConfig.FromStreamInput(pushStream, audioFormat);
using (var recognizer = new ______ (speechConfig, audioConfig))
                            (KeywordRecognizer / SpeakerRecognizer / SpeechRecognizer / SpeechSynthesizer)
  {
  var result = await recognizer.RecognizeOnceAsync();
  var text = result.Text;
  }
  
# Correct Answer:
AudioStreamFormat.getCompressedFormat, SpeechRecognizer

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-use-codec-compressed-audio-input-streams?tabs=debian&pivots=programming- language-csharp
"""

question_1_19 = """
# HOTSPOT -
You are developing an internet-based training solution for remote learners.
Your company identifies that during the training, some learners leave their desk for long periods or become distracted.
You need to use a video and audio feed from each learner's computer to detect whether the learner is present and paying attention. The solution must minimize development effort and identify each learner. 
Which Azure Cognitive Services service should you use for each requirement? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

# Hot Area:
From a learner's video feed, verify whether the learner is present: ______ (Face / Speech / Text Analytics)
From a learner's facial expression in the video feed, verify whether the learner is paying attention: ______ (Face / Speech / Text Analytics)
From a learner's audio feed, detect whether the learner is talking: ______ (Face / Speech / Text Analytics)

# Correct Answer:
Face, Face, Speech

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/what-are-cognitive-services
"""

question_1_20 = """
# QUESTION
You plan to provision a QnA Maker service in a new resource group named RG1.
In RG1, you create an App Service plan named AP1.
Which two Azure resources are automatically created in RG1 when you provision the QnA Maker service? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Language Understanding
B. Azure SQL Database
C. Azure Storage
D. Azure Cognitive Search
E. Azure App Service

# Correct Answer:
DE

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/how-to/set-up-qnamaker-service-azure?tabs=v1#delete-azure-resources
"""

question_1_21 = """
# QUESTION
You are building a language model by using a Language Understanding (classic) service.
You create a new Language Understanding (classic) resource.
You need to add more contributors.
What should you use?
A. a conditional access policy in Azure Active Directory (Azure AD)
B. the Access control (IAM) page for the authoring resources in the Azure portal
C. the Access control (IAM) page for the prediction resources in the Azure portal

# Correct Answer:
B

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-how-to-collaborate
"""

question_1_22 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Cognitive Search service.
During the past 12 months, query volume steadily increased.
You discover that some search query requests to the Cognitive Search service are being throttled.
You need to reduce the likelihood that search query requests are throttled.

Solution: You migrate to a Cognitive Search service that uses a higher tier.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
A

A simple x to most throttling issues is to throw more resources at the search service (typically replicas for query-based throttling, or partitions for indexing-based throttling). However, increasing replicas or partitions adds cost, which is why it is important to know the reason why throttling is occurring at all.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-performance-analysis
"""

question_1_23 = """
# DRAG DROP -
You need to develop an automated call handling system that can respond to callers in their own language. The system will support only French and English.
Which Azure Cognitive Services service should you use to meet each requirement? To answer, drag the appropriate services to the correct requirements. Each service may be used once, more than once, or not at all. You may need to drag the split bat between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

# Select and Place:
Services
Speaker Recognition
Speech to Text
Text Analytics
Text to Speech
Translator

Answer Area
Detect the incoming language: ______
Respond in the callers' own language: _____

# Correct Answer:
Text Analytics, Translator

Box 1: Text Analytics -
The Language Detection feature of the Azure Text Analytics REST API evaluates text input for each document and returns language identifiers with a score that indicates the strength of the analysis.
Incorrect Answers:
Speaker Recognition which accurately verifies and identifies speakers by their unique voice characteristics.
Box 2: Translator -
Translator is a cloud-based neural machine translation service that is part of the Azure Cognitive Services family of REST APIs. Translator can be used with any operating system and powers many Microsoft products and services used by thousands of businesses worldwide to perform language translation and other language-related operations.

Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-language-detection
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-overview
"""

question_1_24 = """
# QUESTION
You have receipts that are accessible from a URL.
You need to extract data from the receipts by using Form Recognizer and the SDK. The solution must use a prebuilt model.
Which client and method should you use?
A. the FormRecognizerClient client and the StartRecognizeContentFromUri method
B. the FormTrainingClient client and the StartRecognizeContentFromUri method
C. the FormRecognizerClient client and the StartRecognizeReceiptsFromUri method
D. the FormTrainingClient client and the StartRecognizeReceiptsFromUri method

# Correct Answer:
D

To analyze receipts from a URL, use the StartRecognizeReceiptsFromUri method
Example code:
private static async Task AnalyzeReceipt(
FormRecognizerClient recognizerClient, string receiptUri)
{
RecognizedFormCollection receipts = await recognizerClient.StartRecognizeReceiptsFromUri(new
Uri(receiptUrl)).WaitForCompletionAsync();

# Reference:
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/client-library
"""

question_1_25 = """
# QUESTION
You have a collection of 50,000 scanned documents that contain text.
You plan to make the text available through Azure Cognitive Search.
You need to configure an enrichment pipeline to perform optical character recognition (OCR) and text analytics. The solution must minimize costs.
What should you attach to the skillset?
A. a new Computer Vision resource
B. a free (Limited enrichments) Cognitive Services resource
C. an Azure Machine Learning Designer pipeline
D. a new Cognitive Services resource that uses the S0 pricing tier

# Correct Answer:
A

The Computer Vision API uses text recognition APIs to extract and recognize text information from images. Read uses the latest recognition models, and is optimized for large, text-heavy documents and noisy images.

# Reference:
https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/cognitive-search-with-skillsets
"""

question_1_26 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Cognitive Search service.
During the past 12 months, query volume steadily increased.
You discover that some search query requests to the Cognitive Search service are being throttled.
You need to reduce the likelihood that search query requests are throttled.

Solution: You add indexes.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B

Instead, you could migrate to a Cognitive Search service that uses a higher tier.
Note: A simple x to most throttling issues is to throw more resources at the search service (typically replicas for query-based throttling, or partitions for indexing- based throttling). However, increasing replicas or partitions adds cost, which is why it is important to know the reason why throttling is occurring at all.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-performance-analysis
"""

question_1_27 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Cognitive Search service.
During the past 12 months, query volume steadily increased.
You discover that some search query requests to the Cognitive Search service are being throttled.
You need to reduce the likelihood that search query requests are throttled.

Solution: You enable customer-managed key (CMK) encryption.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B

Customer-managed key (CMK) encryption does not affect throttling.
Instead, you could migrate to a Cognitive Search service that uses a higher tier.
Note: A simple x to most throttling issues is to throw more resources at the search service (typically replicas for query-based throttling, or partitions for indexing- based throttling). However, increasing replicas or partitions adds cost, which is why it is important to know the reason why throttling is occurring at all.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-performance-analysis
"""

question_1_28 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a web app named app1 that runs on an Azure virtual machine named vm1. Vm1 is on an Azure virtual network named vnet1.
You plan to create a new Azure Cognitive Search service named service1.
You need to ensure that app1 can connect directly to service1 without routing trac over the public internet.

Solution: You deploy service1 and a private endpoint to vnet1.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
A

A private endpoint is a network interface that uses a private IP address from your virtual network. This network interface connects you privately and securely to a service powered by Azure Private Link. By enabling a private endpoint, you're bringing the service into your virtual network.
The service could be an Azure service such as:
✑ Azure Storage
✑ Azure Cosmos DB
✑ Azure SQL Database
✑ Your own service using a Private Link Service.

# Reference:
https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview
"""

question_1_29 = """
# QUESTION
You have a Language Understanding resource named lu1.
You build and deploy an Azure bot named bot1 that uses lu1.
You need to ensure that bot1 adheres to the Microsoft responsible AI principle of inclusiveness.
How should you extend bot1?
A. Implement authentication for bot1.
B. Enable active learning for lu1.
C. Host lu1 in a container.
D. Add Direct Line Speech to bot1.

# Correct Answer:
D

Inclusiveness: AI systems should empower everyone and engage people.
Direct Line Speech is a robust, end-to-end solution for creating a flexible, extensible voice assistant. It is powered by the Bot Framework and its Direct Line
Speech channel, that is optimized for voice-in, voice-out interaction with bots.
Incorrect:
Not B: The Active learning suggestions feature allows you to improve the quality of your knowledge base by suggesting alternative questions, based on user submissions, to your question and answer pair. You review those suggestions, either adding them to existing questions or rejecting them.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/direct-line-speech
"""

question_1_30 = """
# HOTSPOT -
You are building an app that will process incoming email and direct messages to either French or English language support teams.
Which Azure Cognitive Services API should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

# Hot Area:
https://______ ______
(api.cognitive.microsofttranslator.com
 eastus.api.cognitive.microsoft.com
 portal.azure.com)
(/text/analytics/v3.1/entities/recognition/general
 /text/analytics/v3.1/languages
 /translator/text/v3.0/translate?to=en
 /translator/text/v3.0/translate?to=fr
)

# Connect Answer:
api.cognitive.microsofttranslator.com, /text/analytics/v3.1/entities/recognition/general

Box 1: api/cognitive.microsofttranslator.com is used for translations.
Incorrect:
eastus.api.cognitive.microsoft.com is used for Face recognition.
Portal.azure.com is the URL of the Azure portal which is a web-based, unified console that provides an alternative to command-line tools.
With the Azure portal, you can manage your Azure subscription using a graphical user interface. You can build, manage, and monitor everything from simple web apps to complex cloud deployments.
Box 2: /text/analytics/v3.1/entities/recognition/general
Named Entity Recognition -
The API returns a list of general named entities in a given document.
Request URL: https://{endpoint}/text/analytics/v3.1/entities/recognition/general[?model-version][&showStats][&loggingOptOut][&stringIndexType]

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate
https://westcentralus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-1/operations/EntitiesRecognitionGenera
"""

question_1_31 = """
# QUESTION
You have an Azure Cognitive Search instance that indexes purchase orders by using Form Recognizer.
You need to analyze the extracted information by using Microsoft Power BI. The solution must minimize development effort.
What should you add to the indexer?
A. a projection group
B. a table projection
C. a le projection
D. an object projection

# Correct Answer:
D

Projections are the physical tables, objects, and les in a knowledge store that accept content from a Cognitive Search AI enrichment pipeline. If you're creating a knowledge store, defining and shaping projections is most of the work.
Objects is used when you need the full JSON representation of your data and enrichments in one JSON document. As with table projections, only valid JSON objects can be projected as objects, and shaping can help you do that.
Note: Form Recognizer analyzes your forms and documents, extracts text and data, maps eld relationships as key-value pairs, and returns a structured JSON output. You quickly get accurate results that are tailored to your specific content without excessive manual intervention or extensive data science expertise.
Incorrect:
Not Tables: Tables is used for data that's best represented as rows and columns, or whenever you need granular representations of your data (for example, as data frames). Table projections allow you to dene a schematized shape, using a Shaper skill or use inline shaping to specify columns and rows.
Not File: File is used when you need to save normalized, binary image les.

# Reference:
https://docs.microsoft.com/en-us/azure/search/knowledge-store-projection-overview
"""

question_1_32 = """
# SCENARIO
Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Cognitive Search service.
During the past 12 months, query volume steadily increased.
You discover that some search query requests to the Cognitive Search service are being throttled.
You need to reduce the likelihood that search query requests are throttled.

Solution: You add replicas.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
A

A simple x to most throttling issues is to throw more resources at the search service (typically replicas for query-based throttling, or
partitions for indexing-based throttling). However, increasing replicas or partitions adds cost, which is why it is important to know the
reason why throttling is occurring at all.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-performance-analysis
"""

question_1_33 = """
# SIMULATION
You need to create a Text Analytics service named Text12345678, and then enable logging for Text12345678. The solution must ensure that any changes to Text12345678 will be stored in a Log Analytics workspace.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Step 1: Sign in to the QnA portal.
Step 2: Create an Azure Cognitive multi-service resource:
Step 3: On the Create page, provide the following information.
Name: Text12345678 -
Step 4: Configure additional settings for your resource as needed, read and accept the conditions (as applicable), and then select Review + create.
Step 5: Navigate to the Azure portal. Then locate and select The Text Analytics service resource Text12345678 (which you created in Step 4).
Step 6: Next, from the left-hand navigation menu, locate Monitoring and select Diagnostic settings. This screen contains all previously created diagnostic settings for this resource.
Step 7: Select + Add diagnostic setting.
Step 8: When prompted to configure, select the storage account and OMS workspace that you'd like to use to store you diagnostic logs.
Note: If you don't have a storage account or OMS workspace, follow the prompts to create one.
Step 9: Select Audit, RequestResponse, and AllMetrics. Then set the retention period for your diagnostic log data. If a retention policy is set to zero, events for that log category are stored indefinitely.
Step 10: Click Save.
It can take up to two hours before logging data is available to query and analyze. So don't worry if you don't see anything right away.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account https://docs.microsoft.com/en-us/azure/cognitive-services/diagnostic-logging
"""

question_1_34 = """
# SIMULATION
You need to create a search service named search12345678 that will index a sample Azure Cosmos DB database named hotels-sample. The solution must ensure that only English language fields are retrievable.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Part 1: Create a search service search12345678
Step 1: Sign in to the QnA portal.
Step 2: Create an Azure Cognitive multi-service resource:
Step 3: On the Create page, provide the following information.
Name: search12345678
Step 4: Click Review + create
Part 2: Start the Import data wizard and create a data source
Step 5: Click Import data on the command bar to create and populate a search index.
Step 6: In the wizard, click Connect to your data > Samples > hotels-sample. This data source is built-in. If you were creating your own data source, you would need to specify a name, type, and connection information. Once created, it becomes an "existing data source" that can be reused in other import operations.
Step 7: Continue to the next page.
Step 8: Skip the "Enrich content" page
Step 9: Configure index.
Make sure English is selected for the fields.
Step 10: Continue and finish the wizard.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account https://docs.microsoft.com/en-us/azure/search/search-get-started-portal
"""

question_1_35 = """
# SIMULATION
You plan to create a solution to generate captions for images that will be read from Azure Blob Storage.
You need to create a service in Azure Cognitive Services for the solution. The service must be named captions12345678 and must use the Free pricing tier.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Part 1: Create a search service captions12345678
Step 1: Sign in to the QnA portal.
Step 2: Create an Azure Cognitive multi-service resource:
Step 3: On the Create page, provide the following information.
Name: captions12345678
Pricing tier: Free 
Step 4: Click Review + create
Step 5: Create a data source
In Connect to your data, choose Azure Blob Storage. Choose an existing connection to the storage account and container you created. Give the data source a name, and use default values for the rest.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-create-service-portal https://docs.microsoft.com/en-us/azure/search/cognitive-search-quickstart-ocr
"""

question_1_36 = """
# SIMULATION
You need to create a Form Recognizer resource named fr12345678.
Use the Form Recognizer sample labeling tool at https://fott-2-1.azurewebsites.net/ to analyze the invoice located in the
C:\Resources\Invoices folder.
Save the results as C:\Resources\Invoices\Results.json.
To complete this task, sign in to the Azure portal and open the Form Recognizer sample labeling tool.

# Correct Answer:
See explanation below.
Step 1: Sign in to the Azure Portal.
Step 2: Navigate to the Form Recognizer Sample Tool (at https://fott-2-1.azurewebsites.net)
Step 3: On the sample tool home page select Use prebuilt model to get data.
Step 4: Select the Form Type you would like to analyze from the dropdown window.
Step 5: In the Source: URL eld, paste the selected URL and select the Fetch button.
Step 6: In the Choose le for analysis use the le in the C:\Resources\Invoices folder and select the Fetch button.
Step 7: Select Run analysis. The Form Recognizer Sample Labeling tool will call the Analyze Prebuilt API and analyze the document.
Step 8: View the results - see the key-value pairs extracted, line items, highlighted text extracted and tables detected
Step 9: Save the results as C:\Resources\Invoices\Results.json.

# Reference:
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-sample-label-tool
"""

question_1_37 = """
# QUESTION
You have a factory that produces food products.
You need to build a monitoring solution for staff compliance with personal protective equipment (PPE) requirements. The solution must meet the following requirements:
* Identify staff who have removed masks or safety glasses.
* Perform a compliance check every 15 minutes.
* Minimize development effort.
* Minimize costs.

Which service should you use?
A. Face
B. Computer Vision
C. Azure Video Analyzer for Media (formerly Video Indexer)

# Correct Answer:
A

Face API is an AI service that analyzes faces in images.
Embed facial recognition into your apps for a seamless and highly secured user experience. No machine-learning expertise is required.
Features include face detection that perceives facial features and attributes such as a face mask, glasses, or face location in an image, and identification of a person by a match to your private repository or via photo ID.

# Reference:
https://azure.microsoft.com/en-us/services/cognitive-services/face/
"""

question_1_38 = """
# QUESTION
You have an Azure Cognitive Search solution and a collection of blog posts that include a category eld.
You need to index the posts. The solution must meet the following requirements:
* Include the category eld in the search results.
* Ensure that users can search for words in the category eld.
* Ensure that users can perform drill down filtering based on category.

Which index attributes should you configure for the category eld?
A. searchable, sortable, and retrievable
B. searchable, facetable, and retrievable
C. retrievable, filterable, and sortable
D. retrievable, facetable, and key

# Correct Answer:
C

Fields have data types and attributes. The check boxes across the top are index attributes controlling how the eld is used.
* Retrievable means that it shows up in search results list. You can mark individual fields as off limits for search results by clearing this checkbox, for example for fields used only in filter expressions.
* Filterable, Sortable, and Facetable determine whether fields are used in a filter, sort, or faceted navigation structure.
* Searchable means that a eld is included in full text search. Strings are searchable. Numeric fields and Boolean fields are often marked as not searchable.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-get-started-portal
"""

question_1_39 = """
# SIMULATION
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com
Azure Password: XXXXXXXXXXXX
The following information is for technical support purposes only:
Lab Instance: 12345678

Task
You plan to build an API that will identify whether an image includes a Microsoft Surface Pro or Surface Studio.
You need to deploy a service in Azure Cognitive Services for the API. The service must be named AAA12345678 and must be in the East US Azure region. The solution must use the Free pricing tier.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Step 1: In the Azure dashboard, click Create a resource.
Step 2: In the search bar, type "Cognitive Services."
You'll get information about the cognitive services resource and a legal notice. Click Create.
Step 3: You'll need to specify the following details about the cognitive service (refer to the image below for a completed example of this page):
Subscription: choose your paid or trial subscription, depending on how you created your Azure account.
Resource group: click create new to create a new resource group or choose an existing one.
Region: choose the Azure region for your cognitive service. Choose: East US Azure region.
Name: choose a name for your cognitive service. Enter: AAA12345678
Pricing Tier: Select: Free pricing tier
Step 4: Review and create the resource, and wait for deployment to complete. Then go to the deployed resource.
Note: The Computer Vision Image Analysis service can extract a wide variety of visual features from your images. For example, it can determine whether an image contains adult content, nd specific brands or objects, or find human faces.

Tag visual features
Identify and tag visual features in an image, from a set of thousands of recognizable objects, living things, scenery, and actions. When the tags are ambiguous or not common knowledge, the API response provides hints to clarify the context of the tag. Tagging isn't limited to the main subject, such as a person in the foreground, but also includes the setting (indoor or outdoor), furniture, tools, plants, animals, accessories, gadgets, and so on.
Try out the image tagging features quickly and easily in your browser using Vision Studio.

# Reference:
https://docs.microsoft.com/en-us/learn/modules/analyze-images-computer-vision/3-analyze-images
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview-image-analysis
"""

question_1_40 = """
# SIMULATION
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com
Azure Password: XXXXXXXXXXXX
The following information is for technical support purposes only:
Lab Instance: 12345678

Task
You need to build an API that uses the service in Azure Cognitive Services named AAA12345678 to identify whether an image includes a Microsoft Surface Pro or Surface Studio.
To achieve this goal, you must use the sample images in the C:\Resources\Images folder.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Step 1: In the Azure dashboard, click Create a resource.
Step 2: In the search bar, type "Cognitive Services."
You'll get information about the cognitive services resource and a legal notice. Click Create.
Step 3: You'll need to specify the following details about the cognitive service (refer to the image below for a completed example of this page):
Subscription: choose your paid or trial subscription, depending on how you created your Azure account.
Resource group: click create new to create a new resource group or choose an existing one.
Region: choose the Azure region for your cognitive service. Choose: East US Azure region.
Name: choose a name for your cognitive service. Enter: AAA12345678
Pricing Tier: Select: Free pricing tier
Step 4: Review and create the resource, and wait for deployment to complete. Then go to the deployed resource.
Note: The Computer Vision Image Analysis service can extract a wide variety of visual features from your images. For example, it can determine whether an image contains adult content, find specific brands or objects, or nd human faces.

Tag visual features
Identify and tag visual features in an image, from a set of thousands of recognizable objects, living things, scenery, and actions. When the tags are ambiguous or not common knowledge, the API response provides hints to clarify the context of the tag. Tagging isn't limited to the main subject, such as a person in the foreground, but also includes the setting (indoor or outdoor), furniture, tools, plants, animals, accessories, gadgets, and so on.
Try out the image tagging features quickly and easily in your browser using Vision Studio.

# Reference:
https://docs.microsoft.com/en-us/learn/modules/analyze-images-computer-vision/3-analyze-images
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview-image-analysis
"""

question_1_41 = """
# SIMULATION
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com
Azure Password: XXXXXXXXXXXX
The following information is for technical support purposes only:
Lab Instance: 12345678

Task
You need to get insights from a video le located in the C:\Resources\Video\Media.mp4 folder.
Save the insights to the C:\Resources\Video\Insights.json folder.
To complete this task, sign in to the Azure Video Analyzer for Media at https://www.videoindexer.ai/ by using admin@abc.com

# Correct Answer:
See explanation below.
Step 1: Login
Browse to the Azure Video Indexer website and sign in.
URL: https://www.videoindexer.ai/
Login admin@abc.com
Step 2: Create a project from your video
You can create a new project directly from a video in your account.
1. Go to the Library tab of the Azure Video Indexer website.
2. Open the video that you want to use to create your project. On the insights and timeline page, select the Video editor button.
Folder: C:\Resources\Video\Media.mp4
This takes you to the same page that you used to create a new project. Unlike the new project, you see the timestamped insights segments of the video, that you had started editing previously.
Step 3: Save the insights to the C:\Resources\Video\Insights.json folder.

# Reference:
https://docs.microsoft.com/en-us/azure/azure-video-indexer/use-editor-create-project
"""

question_1_42 = """
# SIMULATION
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com
Azure Password: XXXXXXXXXXXX
The following information is for technical support purposes only:
Lab Instance: 12345678

Task
You plan to analyze stock photography and automatically generate captions for the images.
You need to create a service in Azure to analyze the images. The service must be named caption12345678 and must be in the East US Azure
region. The solution must use the Free pricing tier.
In the C:\Resources\Caption\Params.json folder, enter the value for Key 1 and the endpoint for the new service.
To complete this task, sign in to the Azure portal.

# Correct Answer: 
See explanation below.
Step 1: Provision a Cognitive Services resource
If you don't already have one in your subscription, you'll need to provision a Cognitive Services resource.
1. Open the Azure portal at https://portal.azure.com, and sign in using the Microsoft account associated with your Azure subscription.
2. Select the Create a resource button, search for cognitive services, and create a Cognitive Services resource with the following settings:
Subscription: Your Azure subscription
Resource group: Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)
Region: East US Azure region
Name: caption12345678
Pricing tier: Free F0
3. Select the required checkboxes and create the resource.
Wait for deployment to complete, and then view the deployment details.
4. When the resource has been deployed, go to it and view its Keys and Endpoint page. You will need the endpoint and one of the keys from this page in the next procedure.
Step 2: Save Key and Endpoint values in Params.json
Open the configuration file, C:\Resources\Caption\Params.json. and update the configuration values it contains to reflect the endpoint and an authentication key for your cognitive services resource. Save your changes.

# Reference:
https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/15-computer-vision.html
"""

question_1_43 = """
# SIMULATION
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com
Azure Password: XXXXXXXXXXXX
The following information is for technical support purposes only:
Lab Instance: 12345678

Task
You plan to build an application that will use caption12345678. The application will be deployed to a virtual network named VNet1.
You need to ensure that only virtual machines on VNet1 can access caption12345678.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Step 1: Create private endpoint for your web app
1. In the left-hand menu, select All Resources > caption12345678 - the name of your web app.
2. In the web app overview, select Settings > Networking.
3. In Networking, select Private endpoints.
4. Select + Add in the Private Endpoint connections page.
5. Enter or select the following information in the Add Private Endpoint page:
Name: Enter caption12345678.
Subscription Select your Azure subscription.
Virtual network Select VNet1.
Subnet:
Integrate with private DNS zone: Select Yes.
6. Select OK.

# Reference:
https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-webapp-portal
"""

question_1_44 = """
# SIMULATION
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com
Azure Password: XXXXXXXXXXXX
The following information is for technical support purposes only:
Lab Instance: 12345678

Task
You need to ensure that a user named admin@abc.com can regenerate the subscription keys of AAA12345678. The solution must use the principle of least privilege.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Manually rotate subscription keys
1. (Update your application code to reference the secondary key for the Azure account and deploy.)
2. In the Azure portal, navigate to your Azure account.
3. Under Settings, select Authentication.
4. To regenerate the primary key for your Azure account, select the Regenerate button next to the primary key.
5. (Update your application code to reference the new primary key and deploy.)
6. Regenerate the secondary key in the same manner.

Reference:
https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/azure-maps/how-to-manage-authentication.md
"""

question_1_45 = """
# QUESTION
You have an Azure IoT hub that receives sensor data from machinery.
You need to build an app that will perform the following actions:
• Perform anomaly detection across multiple correlated sensors.
• Identify the root cause of process stops.
• Send incident alerts.
The solution must minimize development time.

Which Azure service should you use?
A. Azure Metrics Advisor
B. Form Recognizer
C. Azure Machine Learning
D. Anomaly Detector

# Correct Answer:
D
"""

question_1_46 = """
# QUESTION
You have an app that analyzes images by using the Computer Vision API.
You need to configure the app to provide an output for users who are vision impaired. The solution must provide the output in complete sentences.
Which API call should you perform?
A. readInStreamAsync
B. analyzeImagesByDomainInStreamAsync
C. tagImageInStreamAsync
D. describeImageInStreamAsync

# Correct Answer:
D
"""

question_1_47 = """
# DRAG DROP
You have a Custom Vision service project that performs object detection. The project uses the General domain for classification and contains a trained model.
You need to export the model for use on a network that is disconnected from the internet.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Change the classification type.
Export the model.
Retrain the model.
Change Domains to General (compact).
Create a new classification model.

# Correct Answer:
Change Domains to General (compact).
Retrain the model.
Export the model.
"""

question_1_48 = """
# QUESTION
You are building an AI solution that will use Sentiment Analysis results from surveys to calculate bonuses for customer service staff.
You need to ensure that the solution meets the Microsoft responsible AI principles.
What should you do?
A. Add a human review and approval step before making decisions that affect the staff's financial situation.
B. Include the Sentiment Analysis results when surveys return a low confidence score.
C. Use all the surveys, including surveys by customers who requested that their account be deleted and their data be removed.
D. Publish the raw survey data to a central location and provide the staff with access to the location.

# Correct Answer:
A
"""

question_1_49 = """
# QUESTION
You have an Azure subscription that contains a Language service resource named ta1 and a virtual network named vnet1.
You need to ensure that only resources in vnet1 can access ta1.
What should you configure?
A. a network security group (NSG) for vnet1
B. Azure Firewall for vnet1
C. the virtual network settings for ta1
D. a Language service container for ta1

# Correct Answer:
C
"""

question_1_50 = """
# QUESTION
You are developing a monitoring system that will analyze engine sensor data, such as rotation speed, angle, temperature, and pressure. The
system must generate an alert in response to atypical values.
What should you include in the solution?
A. Application Insights in Azure Monitor
B. metric alerts in Azure Monitor
C. Multivariate Anomaly Detection
D. Univariate Anomaly Detection

# Correct Answer:
C
"""

question_1_51 = """
# QUESTION
You have an app named App1 that uses an Azure Cognitive Services model to identify anomalies in a time series data stream.
You need to run App1 in a location that has limited connectivity. The solution must minimize costs.
What should you use to host the model?
A. Azure Kubernetes Service (AKS)
B. Azure Container Instances
C. a Kubernetes cluster hosted in an Azure Stack Hub integrated system
D. the Docker Engine

# Correct Answer:
C
"""

question_1_52 = """
# HOTSPOT
You have an Azure Cognitive Search resource named Search1 that is used by multiple apps.
You need to secure Search1. The solution must meet the following requirements:
• Prevent access to Search1 from the internet.
• Limit the access of each app to specific queries.
What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point

Answer Area
To prevent access from the internet: ______ (Configure an IP firewall. / Create a private endpoint. / Use Azure roles.)
To limit access to queries: ______ (/ Create a private endpoint. / Use Azure roles. / Use key authorization.)

# Correct Answer:
Create a private endpoint., Use key authorization.
"""

question_1_53 = """
# QUESTION
You are building a solution that will detect anomalies in sensor data from the previous 24 hours.
You need to ensure that the solution scans the entire dataset, at the same time, for anomalies.
Which type of detection should you use?
A. batch
B. streaming
C. change points

# Correct Answer:
A
"""

question_1_54 = """
# DRAG DROP

You are building an app that will scan confidential documents and use the Language service to analyze the contents.
You provision an Azure Cognitive Services resource.
You need to ensure that the app can make requests to the Language service endpoint. The solution must ensure that confidential documents remain on-premises.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Run the container and specify an App ID and Client Secret.
Provision an on-premises Kubernetes cluster that is isolated from the internet.
Pull an image from the Microsoft Container Registry (MCR).
Run the container and specify an API key and the Endpoint URL of the Cognitive Services resource.
Provision an on-premises Kubernetes cluster that has internet connectivity.
Pull an image from Docker Hub.
Provision an Azure Kubernetes Service (AKS) resource.

# Correct Answer:
Pull an image from the Microsoft Container Registry (MCR).
Provision an on-premises Kubernetes cluster that is isolated from the internet.
Run the container and specify an API key and the Endpoint URL of the Cognitive Services resource.
"""

question_1_55 = """
# HOTSPOT

You have an Azure subscription that has the following configurations:
• Subscription ID: 8d3591aa-96b8-4737-ad09-00f9b1ed35ad
• Tenant ID: 3edfe572-cb54-3ced-ae12-c5c177f39a12
You plan to create a resource that will perform sentiment analysis and optical character recognition (OCR).
You need to use an HTTP request to create the resource in the subscription. The solution must use a single key and endpoint.
How should you complete the request? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
https://management.azure.com/______/resourceGroups/OCRProject/providers/______/accounts/CS1?api-version=2021-10-01
(subscriptions/3edfe572-cb54-3ced-ae12-c5c177f39a12
 subscriptions/8d3591aa-96b8-4737-ad09-00f9b1ed35ad
 tenant/3edfe572-cb54-3ced-ae12-c5c177f39a12
 tenant/8d3591aa-96b8-4737-ad09-00f9b1ed35ad)
(Microsoft.ApiManagement
 Microsoft.CognitiveServices
 Microsoft.ContainerService
 Microsoft.KeyVault
)

# Correct Answer:
subscriptions/8d3591aa-96b8-4737-ad09-00f9b1ed35ad, Microsoft.CognitiveServices
"""

question_1_56 = """
# QUESTION
You have an Azure subscription that contains an Anomaly Detector resource.
You deploy a Docker host server named Server1 to the on-premises network.
You need to host an instance of the Anomaly Detector service on Server1.
Which parameter should you include in the docker run command?
A. Fluentd
B. Billing
C. Http Proxy
D. Mounts

# Correct Answer:
B
"""

question_1_57 = """
# QUESTION
You are building an app that will use the Speech service.
You need to ensure that the app can authenticate to the service by using a Microsoft Azure Active Directory (Azure AD), part of Microsoft Entra, token.
Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Enable a virtual network service endpoint.
B. Configure a custom subdomain.
C. Request an X.509 certificate.
D. Create a private endpoint.
E. Create a Conditional Access policy.

# Correct Answer:
CE
"""

question_1_58 = """
# HOTSPOT

You plan to deploy an Azure OpenAI resource by using an Azure Resource Manager (ARM) template.
You need to ensure that the resource can respond to 600 requests per minute.
How should you complete the template? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
{
  "type": "Microsoft.CognitiveServices/accounts/deployments",
  "apiVersion": "2023-05-01",
  "name": "arm-aoai-sample-resource/arm-je-std-deployment",
  "dependsOn": [
    "[resourceId('Microsoft.CognitiveServices/accounts', 'arm-aoai-sample-resource')]"
  ],
  "sku": {
    "name": "Standard",
    ______("capacity" / "count" / "maxValue" / "size"): ______ (1 / 60 / 100 / 600)
  },
  "properties": {
    "model": {
      "format": "OpenAI",
}

# Correct Answer:
"capacity", 100
"""

question_1_59 = """
# DRAG DROP

You have an app that manages feedback.
You need to ensure that the app can detect negative comments by using the Sentiment Analysis API in Azure AI Language. The solution must ensure that the managed feedback remains on your company’s internal network.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.
NOTE: More than one order of answer choices is correct. You will receive credit for any of the correct orders you select.

Actions
Identify the Language service endpoint URL and query the prediction endpoint.
Provision the Language service resource in Azure.
Run the container and query the prediction endpoint.
Deploy a Docker container to an on-premises server.
Deploy a Docker container to an Azure container instance.

# Correct Answer:
Deploy a Docker container to an on-premises server.
Provision the Language service resource in Azure.
Run the container and query the prediction endpoint.
"""

question_1_60 = """
# HOTSPOT

You have an Azure OpenAI resource named AI1 that hosts three deployments of the GPT 3.5 model. Each deployment is optimized for a unique workload.
You plan to deploy three apps. Each app will access AI1 by using the REST API and will use the deployment that was optimized for the app's intended workload.
You need to provide each app with access to AI1 and the appropriate deployment. The solution must ensure that only the apps can access AI1.
What should you use to provide access to AI1, and what should each app use to connect to its appropriate deployment? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area 
Provide Access to AI1 by using: ______ (An API key / A bearer token / A shared access signature (SAS) token)
Connect to the deployment by using: ______ (An API key / A deployment endpoint / a deployment name / A deployment type)

# Correct Answer:
A bearer token, A deployment endpoint
"""

question_1_61 = """
# QUESTION
You build a bot by using the Microsoft Bot Framework SDK.
You start the bot on a local computer.
You need to validate the functionality of the bot.
What should you do before you connect to the bot?
A. Run the Bot Framework Emulator.
B. Run the Bot Framework Composer.
C. Register the bot with Azure Bot Service.
D. Run Windows Terminal.

# Correct Answer:
A
"""

question_1_62 = """
# QUESTION
You have an Azure OpenAI model named AI1.
You are building a web app named App1 by using the Azure OpenAI SDK.
You need to configure App1 to connect to AI1.
What information must you provide?
A. the endpoint, key, and model name
B. the deployment name, key, and model name
C. the deployment name, endpoint, and key
D. the endpoint, key, and model type

# Correct Answer:
C
"""

question_1_63 = """
# QUESTION
You are building a solution in Azure that will use Azure Cognitive Service for Language to process sensitive customer data.
You need to ensure that only specific Azure processes can access the Language service. The solution must minimize administrative effort.
What should you include in the solution?
A. IPsec rules
B. Azure Application Gateway
C. a virtual network gateway
D. virtual network rules

# Correct Answer:
D
"""

question_1_64 = """
# QUESTION
You plan to perform predictive maintenance.
You collect IoT sensor data from 100 industrial machines for a year. Each machine has 50 different sensors that generate data at one-minute intervals. In total, you have 5,000 time series datasets.
You need to identify unusual values in each time series to help predict machinery failures.
Which Azure service should you use?
A. Azure AI Computer Vision
B. Cognitive Search
C. Azure AI Document Intelligence
D. Azure AI Anomaly Detector

# Correct Answer:
D
"""

question_1_65 = """
# HOTSPOT

You plan to deploy a containerized version of an Azure Cognitive Services service that will be used for sentiment analysis.
You configure https://contoso.cognitiveservices.azure.com as the endpoint URI for the service.
You need to run the container on an Azure virtual machine by using Docker.
How should you complete the command? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area 
docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \  
______ \ 
(
http://contoso.blob.core.windows.net
https://contoso.cognitiveservices.azure.com
mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment
)
Eula=accept \ 
Billing= ______ \ 
(
http://contoso.blob.core.windows.net
https://contoso.cognitiveservices.azure.com
mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment
)
apiKey=xxxxxxxxxxxxxxxxxx

# Correct Answer:
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment, https://contoso.cognitiveservices.azure.com
"""

question_1_66 = """
# QUESTION
You are developing a system that will monitor temperature data from a data stream. The system must generate an alert in response to a typical values. The solution must minimize development effort.
What should you include in the solution?
A. Multivariate Anomaly Detection
B. Azure Stream Analytics
C. metric alerts in Azure Monitor
D. Univariate Anomaly Detection

# Correct Answer:
D
"""

question_1_67 = """
# QUESTION
You have a Microsoft OneDrive folder that contains a 20-GB video le named File1.avi.
You need to index File1.avi by using the Azure Video Indexer website.
What should you do?
A. Upload File1.avi to the www.youtube.com webpage, and then copy the URL of the video to the Azure AI Video Indexer website.
B. Download File1.avi to a local computer, and then upload the le to the Azure AI Video Indexer website.
C. From OneDrive, create a download link, and then copy the link to the Azure AI Video Indexer website.
D. From OneDrive, create a sharing link for File1.avi, and then copy the link to the Azure AI Video Indexer website.

# Correct Answer:
C
"""

question_1_68 = """
# QUESTION
You have an Azure subscription that contains an Azure AI Service resource named CSAccount1 and a virtual network named VNet1.
CSAaccount1 is connected to VNet1.
You need to ensure that only specific resources can access CSAccount1. The solution must meet the following requirements:
• Prevent external access to CSAccount1.
• Minimize administrative effort.
Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct answer is worth one point.
A. In VNet1, enable a service endpoint for CSAccount1.
B. In CSAccount1, configure the Access control (IAM) settings.
C. In VNet1, modify the virtual network settings.
D. In VNet1, create a virtual subnet.
E. In CSAccount1, modify the virtual network settings.

# Correct Answer:
AD
"""

question_1_69 = """
# QUESTION
You are building an internet-based training solution. The solution requires that a user's camera and microphone remain enabled.
You need to monitor a video stream of the user and detect when the user asks an instructor a question. The solution must minimize development effort.
What should you include in the solution?
A. speech-to-text in the Azure AI Speech service
B. language detection in Azure AI Language Service
C. the Face service in Azure AI Vision
D. object detection in Azure AI Custom Vision

# Correct Answer:
A
"""

question_1_70 = """
# QUESTION
You have an Azure DevOps pipeline named Pipeline1 that is used to deploy an app. Pipeline1 includes a step that will create an Azure AI
services account.
You need to add a step to Pipeline1 that will identify the created Azure AI services account. The solution must minimize development effort.
Which Azure Command-Line Interface (CLI) command should you run?
A. az resource link
B. az cognitiveservices account network-rule
C. az cognitiveservices account show
D. az account list

# Correct Answer:
C
"""

question_1_71 = """
# HOTSPOT
You have 1,000 scanned images of hand-written survey responses. The surveys do NOT have a consistent layout.
You have an Azure subscription that contains an Azure AI Document Intelligence resource named AIdoc1.
You open Document Intelligence Studio and create a new project.
You need to extract data from the survey responses. The solution must minimize development effort.
To where should you upload the images, and which type of model should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area 
Upload to: ______ (An Azure Cosmos DB account / An Azure Files share / An Azure Storage account)
Model type: ______ (Custom neural / Custom template / Identity document (ID))

# Correct Answer:
An Azure Storage account, Custom neural
"""

question_2_1 = """
# HOTSPOT

You are developing an application that will use the Computer Vision client library. The application has the following cod

public async TaskAnalyzeImage(ComputerVisionClient client, string localImage)
{
    List<VisualFeatureTypes> features = new List<VisualFeatureTypes>()
        {
            VisualFeatureTypes.Description,
            VisualFeatureTypes.Tags,
        };
    using (Stream imageStream = File.OpenRead(localImage))
    {
        try
        {
            imageAnalysis results = await client.AnalyzeImageInStreamAsync(imageStream, features);
            foreach (var caption in results.Description.Captions)
            {
                Console.WriteLine($"(caption.Text) with confidence (caption.Confidence)");
            }
            foreach (var tag in results.Tags)
            {
                Console.WriteLine($"{tag.Name} {tag.Confidence}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}

For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Hot Area
Statements
The code will perform face recognition.
The code will list tags and their associate confidence.
The code will read a file from the local file system.

# Correct Answer:
No, Yes, No

Box 1: No -
Box 2: Yes -
The ComputerVision.analyzeImageInStreamAsync operation extracts a rich set of visual features based on the image content.
Box 3: No -
Images will be read from a stream.

# Reference:
https://docs.microsoft.com/en-us/java/api/com.microsoft.azure.cognitiveservices.vision.computervision.computervision.analyzeimageinstreamasync
"""

question_2_2 = """
# QUESTION

You are developing a method that uses the Computer Vision client library. The method will perform optical character recognition (OCR) in images. The method has the following code.

public static async Task ReadFileUrl(ComputerVisionClient client, string urlFile)
{
    const int numberOfcharsInOperationId = 36;
    
    var txtHeaders = await client.ReadAsync(urlFile, language: "en");
    
    string opLocation = textHeaders.OperationLocation;
    string operationId = opLocation.Substring(opLocation.Length - numberOfcharsInOperationId);
    
    ReadOperationResult results;
    
    results = await client.GetReadResultAsync(Guid.Parse(operationId));
    
    var textUrlFileResults = results.AnalyzeResult.ReadResults;
    foreach (ReadResult page in textUrlFileResults)
    {
        foreach (Line line in page.Lines)
        {
            Console.WriteLine(line.Text);
        }
    }
}

During testing, you discover that the call to the GetReadResultAsync method occurs before the read operation is complete.
You need to prevent the GetReadResultAsync method from proceeding until the read operation is complete.
Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Remove the Guid.Parse(operationId) parameter.
B. Add code to verify the results.Status value.
C. Add code to verify the status of the txtHeaders.Status value.
D. Wrap the call to GetReadResultAsync within a loop that contains a delay.

# Correct Answer:
BD

Example code :
do
{
results = await client.GetReadResultAsync(Guid.Parse(operationId));
}
while ((results.Status == OperationStatusCodes.Running || results.Status == OperationStatusCodes.NotStarted));

Reference:
https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/dotnet/ComputerVision/ComputerVisionQuickstart.cs
"""

question_2_3 = """
# HOTSPOT
You have a Computer Vision resource named contoso1 that is hosted in the West US Azure region.
You need to use contoso1 to make a different size of a product photo by using the smart cropping feature.
How should you complete the API URL? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:
curl -H "Ocp-Apim-Subscription-Key: xxx" -o "sample.png" -H "Content-Type: application/json" ______/vision/v3.1/______?width=100&height=100&smartCropping=true" -d "{\"url\":\"https://upload.litwareinc.org/litware/bicycle.jpg\"}"
("https:api.projectoxford.ai / "https://contoso1.cognitiveservices.azure.com / "https://westus.api.cognitive.microsoft.com)
(areaOfinterest / detect / generateThumbnail)

# Correct Answer:
"https://westus.api.cognitive.microsoft.com , generateThumbnail

# Reference:
https://westus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f21b
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/concept-generating-thumbnails#examples
"""

question_2_4 = """
# DRAG DROP
You are developing a webpage that will use the Azure Video Analyzer for Media (previously Video Indexer) service to display videos of internal company meetings.
You embed the Player widget and the Cognitive Insights widget into the page.
You need to configure the widgets to meet the following requirements:
✑ Ensure that users can search for keywords.
✑ Display the names and faces of people in the video.
✑ Show captions in the video in English (United States).
How should you complete the URL for each widget? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

Select and Place:
Values
en-US
false
people,keywords
people,search
search
true

Answer Area
Cognitive insights widget
https://www.videoindexer.ai/embed/insights/<accountId>/<videoId>/?widgets=______controls=______
Player Widget
https://www.videoindexer.ai/embed/player/<accountId>/<videoId>/?showcaptions=______captions=______

# Correct Answer
people,keywords, search, true, en-US

# Reference:
https://docs.microsoft.com/en-us/azure/azure-video-analyzer/video-analyzer-for-media-docs/video-indexer-embed-widgets
"""

question_2_5 = """
# DRAG DROP
You train a Custom Vision model to identify a company's products by using the Retail domain.
You plan to deploy the model as part of an app for Android phones.
You need to prepare the model for deployment.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:
Change the model domain.
Retrain the model.
Test the model.
Export the model.

# Correct Answer
Change the model domain.
Retrain the model.
Test the model.
Export the model.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-your-model
"""

question_2_6 = """
# HOTSPOT
You are developing an application to recognize employees' faces by using the Face Recognition API. Images of the faces will be accessible from a URI endpoint.
The application has the following code.

def add_face(subscription_key, person_group_id, person_id, image_uri):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
        }
    body = {
        'url': image_uri
        }
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", F"/face/v1.0/persongroups/{person_group_id}/persons/{person_id}', f'{body}', headers)')
    response = conn.getresponse()
    response_data = response.read()
    
For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Hot Area:
Statements
The code will add a face image to a person object in a person group.
The code will work for up to 10000 people.
add_face can be called multiple times to add multiple face images to a person object.

# Correct Answer:
Yes, No, Yes

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/use-persondirectory
"""

question_2_7 = """
# DRAG DROP

You have a Custom Vision resource named acvdev in a development environment.
You have a Custom Vision resource named acvprod in a production environment.
In acvdev, you build an object detection model named obj1 in a project named proj1.
You need to move obj1 to acvprod.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and
arrange them in the correct order.

Select and Place:
Actions
Use the ExportProject endpoint on acvdev.
Use the GetProjects endpoint on acvdev.
Use the ImportProject endpoint on acvprod.
Use the ExportIteration endpoint on acvdev.
Use the GetIterations endpoint on acvdev.
Use the UpdateProject endpoint on acvprod.

# Correct Answer:
Use the GetProjects endpoint on acvdev.
Use the ExportProject endpoint on acvdev.
Use the ImportProject endpoint on acvprod.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/copy-move-projects
"""

question_2_8 = """
# DRAG DROP

You are developing an application that will recognize faults in components produced on a factory production line. The components are specific to your business.
You need to use the Custom Vision API to help detect common faults.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:
Actions
Train the classifier model.
Upload and tag images.
Initialize the training dataset.
Train the object detection model.
Create a Project.

# Correct Answer
Create a Project.
Upload and tag images.
Train the classifier model.

Step 1: Create a project
Create a new project.
Step 2: Upload and tag the images
Choose training images. Then upload and tag the images.
Step 3: Train the classier model.
Train the classier

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classier
"""

question_2_9 = """
# HOTSPOT
You are building a model that will be used in an iOS app.
You have images of cats and dogs. Each image contains either a cat or a dog.
You need to use the Custom Vision service to detect whether the images is of a cat or a dog.
How should you configure the project in the Custom Vision portal? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:
Project Types: ______ (Classification / Object Detection)
Classification Types: ______ (Multiclass (Single tag per image) / Multilabel (Multiple tags per image))
Domains: ______ (Audit / Food / General / General(compact) / Landmarks / Landmarks(compact) / Retail / Retail(compact))

# Correct Answer
Classification / Multiclass (Single tag per image) / General

Box 1: Classification
Incorrect Answers:
An object detection project is for detecting which objects, if any, from a set of candidates are present in an image.
Box 2: Multiclass
A multiclass Classification project is for classifying images into a set of tags, or target labels. An image can be assigned to one tag only.
Incorrect Answers:
A multilabel Classification project is similar, but each image can have multiple tags assigned to it.
Box 3: General -
General: Optimized for a broad range of image Classification tasks. If none of the other specific domains are appropriate, or if you're unsure of which domain to choose, select one of the General domains.

Reference:
https://cran.r-project.org/web/packages/AzureVision/vignettes/customvision.html
"""

question_2_10 = """
# QUESTION
You have an Azure Video Analyzer for Media (previously Video Indexer) service that is used to provide a search interface over company videos on your company's website.
You need to be able to search for videos based on who is present in the video.
What should you do?
A. Create a person model and associate the model to the videos.
B. Create person objects and provide face images for each object.
C. Invite the entire staff of the company to Video Indexer.
D. Edit the faces in the videos.
E. Upload names to a language model.

Correct Answer:
A

Video Indexer supports multiple Person models per account. Once a model is created, you can use it by providing the model ID of a specific Person model when uploading/indexing or reindexing a video. Training a new face for a video updates the specific custom model that the video was associated with.
Note: Video Indexer supports face detection and celebrity recognition for video content. The celebrity recognition feature covers about one million faces based on commonly requested data source such as IMDB, Wikipedia, and top LinkedIn influencers. Faces that aren't recognized by the celebrity recognition feature are detected but left unnamed. Once you label a face with a name, the face and name get added to your account's Person model. Video Indexer will then recognize this face in your future videos and past videos.

Reference:
https://docs.microsoft.com/en-us/azure/media-services/video-indexer/customize-person-model-with-api
"""

question_2_11 = """
# QUESTION 
You use the Custom Vision service to build a classier.
After training is complete, you need to evaluate the classier.
Which two metrics are available for review? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.
A. recall
B. F-score
C. weighted accuracy
D. precision
E. area under the curve (AUC)

Correct Answer:
AD

Custom Vision provides three metrics regarding the performance of your model: precision, recall, and AP.

Reference:
https://www.tallan.com/blog/2020/05/19/azure-custom-vision/
"""

question_2_12 = """
# DRAG DROP
You are developing a call to the Face API. The call must nd similar faces from an existing list named employeefaces. The employeefaces list contains 60,000 images.
How should you complete the body of the HTTP request? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

Select and Place:
Values
"faceListId"
"LargeFaceListId"
"matchFace"
"matchPerson"

Answer Area
{
"faceId": "18c51a87-3a69-47a8-aedc-a547745f708a1",
______: "employeefaces"
"maxNumOfCandidatesReturned": 1,
"mode": ______
}

# Correct Answer
"LargeFaceListId", "matchFace"

Box 1: LargeFaceListID -
LargeFaceList: Add a face to a specified large face list, up to 1,000,000 faces.
Note: Given query face's faceId, to search the similar-looking faces from a faceId array, a face list or a large face list. A "faceListId" is
created by FaceList - Create containing persistedFaceIds that will not expire. And a "largeFaceListId" is created by LargeFaceList - Create
containing persistedFaceIds that will also not expire.
Incorrect Answers:
Not "faceListId": Add a face to a specified face list, up to 1,000 faces.
Box 2: matchFace -
Find similar has two working modes, "matchPerson" and "matchFace". "matchPerson" is the default mode that it tries to nd faces of the
same person as possible by using internal same-person thresholds. It is useful to nd a known person's other photos. Note that an empty
list will be returned if no faces pass the internal thresholds. "matchFace" mode ignores same-person thresholds and returns ranked similar
faces anyway, even the similarity is low. It can be used in the cases like searching celebrity-looking faces.

Reference:
https://docs.microsoft.com/en-us/rest/api/faceapi/face/findsimilar
"""

question_2_13 = """
# DRAG DROP
You are developing a photo application that will nd photos of a person based on a sample image by using the Face API.
You need to create a POST request to nd the photos.
How should you complete the request? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

Select and Place:
Values
detect
findsimilars
group
identify
matchFace
matchPerson
verify

Answer Area
POST {Endpoint}/face/v1.0/______
Request Body
{
  "faceId": "c5c24a82-6845-4031-9d5d-989df9175426",
  "largeFaceListId": "sample_list",
  "maxNumOfCandidatesReturned": 10,
  "mode": "______"
}

# Correct Answer
detect, matchPerson

Box 1: detect
Face - Detect With Url: Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks, and attributes.
POST {Endpoint}/face/v1.0/detect
Box 2: matchPerson
Find similar has two working modes, "matchPerson" and "matchFace". "matchPerson" is the default mode that it tries to nd faces of the same person as possible by using internal same-person thresholds. It is useful to nd a known person's other photos. Note that an empty list will be returned if no faces pass the internal thresholds. "matchFace" mode ignores same-person thresholds and returns ranked similar faces anyway, even the similarity is low. It can be used in the cases like searching celebrity-looking faces.

# Reference:
https://docs.microsoft.com/en-us/rest/api/faceapi/face/detectwithurl 
https://docs.microsoft.com/en-us/rest/api/faceapi/face/ndsimilar
"""

question_2_14 = """
# HOTSPOT
You develop a test method to verify the results retrieved from a call to the Computer Vision API. The call is used to analyze the existence of company logos in images. The call returns a collection of brands named brands.
You have the following code segment.

for brand in image_analysis.brands:
    if brand_confidence >= 0.75:
         print(f"\nLogo of {brand_name} between {brand.rectangle_x}, {brand.rectangle_y} and {brand.rectangle_w}, {brand.rectangle_h}")

For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Hot Area:
Statements
The code will return the name of each detected brand with a confidence equal to or higher than 75 persent.
The code will return coordinates for the top-left corner of the rectangle that contains the brand logo of the displayed brands.
The code will return coordinates for the bottom-right corner of the rectangle that contains the brand logo of the displayed brands.

# Correct Answer
Yes, Yes, No

Box 1: Yes
Box 2: Yes
Coordinates of a rectangle in the API refer to the top left corner.
Box 3: No

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/concept-brand-detection
"""

question_2_15 = """
# HOTSPOT
You develop an application that uses the Face API.
You need to add multiple images to a person group.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:
Parallel.For(0, PersonCount, async i =>
{
    Guid personId = persons[i].PersonId;
    string personImageDir = $"/path/to/person/{i}/images";
    foreach (string image in Directory.GetFiles(personImageDir, "*.jpg"))
    {
        using (______(File / Stream / Uri / Url) t = File.OpenRead(imagePath))
        {
            await faceClient.PersonGroupPerson.______(AddFaceFromStreamAsync / AddFaceFromUrlAsync / CreateAsync / GetAsync)(personGroupId, personId, t);
        }
    }
});

# Correct Answer
Stream, AddFaceFromUrlAsync

Box 1: Stream -
The File.OpenRead(String) method opens an existing le for reading.
Example: Open the stream and read it back.
using (FileStream fs = File.OpenRead(path))

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/how-to-add-faces
"""

question_2_16 = """
# QUESTION
Your company uses an Azure Cognitive Services solution to detect faces in uploaded images. The method to detect the faces uses the following code.

static async Task DetectFaces(string imageFilePath)
{
  HttpClient client = new HttpClient();
  DefaultRequestHeaders.add("Ocp-Apim-Subscription-Key", subscriptionKey);
  string requestParameter = "detectionModel=detection_01&returnFace=true&returnFaceLandmarks=false";
  string uri = endpoint + "/face/v1.0/detect?" + requestParameters;
  HttpResponseMessage response;
  byte[] byteData = GetImagesAsByteArray(imageFilePath);
  using (ByteArrayContent content = new ByteArrayContent(byteData))
  {
    Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
    response = await PostAsync(uri, content);
    string contentString = await Content.ReadAsStringAsync();
    ProcessDetection(contentString);
  }
}

You discover that the solution frequently fails to detect faces in blurred images and in images that contain sideways faces.
You need to increase the likelihood that the solution can detect faces in blurred images and images that contain sideways faces.
What should you do?
A. Use a different version of the Face API.
B. Use the Computer Vision service instead of the Face service.
C. Use the Identify method instead of the Detect method.
D. Change the detection model.

# Correct Answer:
D

Evaluate different models.
The best way to compare the performances of the detection models is to use them on a sample dataset. We recommend calling the Face Detect API on a variety of images, especially images of many faces or of faces that are difficult to see, using each detection model. Pay attention to the number of faces that each model returns.
The different face detection models are optimized for different tasks. See the following table for an overview of the differences

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/face/face-api-how-to-topics/specify-detection-mode
"""

question_2_17 = """
# QUESTION
You have the following Python function for creating Azure Cognitive Services resources programmatically. 
def create_resource(resource_name, kind, account_tier, location) : parameters = CognitiveServicesAccount(sku=Sku(name=account_tier), kind=kind, location=location, properties={}) result = client.accounts.create(resource_group_name, resource_name, parameters)
You need to call the function to create a free Azure resource in the West US Azure region. The resource will be used to generate captions of images automatically.
Which code should you use?
A. create_resource("res1", "ComputerVision", "F0", "westus")
B. create_resource("res1", "CustomVision.Prediction", "F0", "westus")
C. create_resource("res1", "ComputerVision", "S0", "westus")
D. create_resource("res1", "CustomVision.Prediction", "S0", "westus")

Correct Answer:
B

F0 is the free tier.
Custom Vision Service Upload images to train and customize a computer vision model for your specific use case. Once the model is trained, you can use the API to tag images using the model and evaluate the results to improve your classier.
Incorrect:
Not C, not D: S0 is the standard tier, which isn't free.
Not A, not C: The Computer Vision service provides developers with access to advanced algorithms for processing images and returning information.
Computer Vision Returns information about visual content found in an image:
Use tagging, descriptions, and domain-specific models to identify content and label it with confidence.
Apply adult/racy settings to enable automated restriction of adult content.
Identify image types and color schemes in pictures.

Reference:
https://docs.microsoft.com/en-us/python/api/overview/azure/cognitive-services?view=azure-python
"""

question_2_18 = """
# QUESTION
You are developing a method that uses the Computer Vision client library. The method will perform optical character recognition (OCR) in images. The method has the following code.
During testing, you discover that the call to the GetReadResultAsync method occurs before the read operation is complete.
You need to prevent the GetReadResultAsync method from proceeding until the read operation is complete.
Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Remove the operation_id parameter.
B. Add code to verify the read_results.status value.
C. Add code to verify the status of the read_operation_location value.
D. Wrap the call to get_read_result within a loop that contains a delay.

Correct Answer:
BD
"""

question_2_19 = """
# HOTSPOT
You are building an app that will enable users to upload images. The solution must meet the following requirements:
* Automatically suggest alt text for the images.
* Detect inappropriate images and block them.
* Minimize development effort.
You need to recommend a computer vision endpoint for each requirement.
What should you recommend? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:
Generate alt text:
https://westus.api.cognitive.microsoft.com/contentmoderator/moderate/v1.0/ProcessImage/Evaluate
https://westus.api.cognitive.microsoft.com/customvision/v3.1/prediction/projectId/classify/iterations/publishedName/image
https://westus.api.cognitive.microsoft.com/vision/v3.2/analyze/?visualFeatures=Adult,Descnption

Detect inappropriate content:
https://westus.api.cognitive.microsoft.com/contentmoderator/moderate/v1.0/ProcessImage/Evaluate
https://westus.api.cognitive.microsoft.com/customvision/v3.1/prediction/projectId/classify/iterations/publishedName/image
https://westus.api.cognitive.microsoft.com/vision/v3.2/analyze/?visualFeatures=Adult,Descnption
https://westus.api.cognitive.microsoft.com/vision/v3.2/describe?maxCandidates=1

# Correct Answer:
https://westus.api.cognitive.microsoft.com/customvision/v3.1/prediction/projectId/classify/iterations/publishedName/image
https://westus.api.cognitive.microsoft.com/vision/v3.2/analyze/?visualFeatures=Adult,Descnption

Box 1: https://westus.api.cognitive.microsoft.com/customvision/v3.1/prediction/projectid/classify/iterations/publishName/image
Box 2: https://westus.api.cognitive.microsoft.com/vision/v3.2/analyze/?visualFeatures=Adult,Description
Computer Vision can detect adult material in images so that developers can restrict the display of these images in their software. Content flags are applied with a score between zero and one so developers can interpret the results according to their own preferences.
You can detect adult content with the Analyze Image API. When you add the value of Adult to the visualFeatures query parameter
Incorrect:
Use the Image Moderation API in Azure Content Moderator to scan image content. The moderation job scans your content for profanity, and compares it against custom and shared blocklists.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/concept-detecting-adult-content https://docs.microsoft.com/en-us/azure/cognitive-services/content-moderator/try-image-api 
https://docs.microsoft.com/en-us/legal/cognitive-services/custom-vision/custom-vision-cvs-transparency-note
"""

question_2_20 = """
# QUESTION
You need to build a solution that will use optical character recognition (OCR) to scan sensitive documents by using the Computer Vision API.
The solution must NOT be deployed to the public cloud.
What should you do?
A. Build an on-premises web app to query the Computer Vision endpoint.
B. Host the Computer Vision endpoint in a container on an on-premises server.
C. Host an exported Open Neural Network Exchange (ONNX) model on an on-premises server.
D. Build an Azure web app to query the Computer Vision endpoint.

# Correct Answer:
B

One option to manage your Computer Vision containers on-premises is to use Kubernetes and Helm.
Three primary parameters for all Cognitive Services containers are required. The Microsoft Software License Terms must be present with a value of accept. An Endpoint URI and API key are also needed.
Incorrect:
Not D: This Computer Vision endpoint would be available for the public, unless it is secured.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/deploy-computer-vision-on-premises
"""

question_2_21 = """
# QUESTION
You have an Azure Cognitive Search solution and a collection of handwritten letters stored as JPEG les.
You plan to index the collection. The solution must ensure that queries can be performed on the contents of the letters.
You need to create an indexer that has a skillset.
Which skill should you include?
A. image analysis
B. optical character recognition (OCR)
C. key phrase extraction
D. document extraction

# Correct Answer:
B
"""

question_2_22 = """
# HOTSPOT

You have a library that contains thousands of images.
You need to tag the images as photographs, drawings, or clipart.
Which service endpoint and response property should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area:

Service endpoint: ______ (Computer Vision analyze images / Computer Vision object detection / Custom Vision image classification / Custom Vision object detection)
Property: ______ (categories / description / imageType / metadata / objects)

# Correct Answer:
Computer Vision analyze images, imageType
"""

question_2_23 = """
# QUESTION
You have an app that captures live video of exam candidates.
You need to use the Face service to validate that the subjects of the videos are real people.
What should you do?
A. Call the face detection API and retrieve the face rectangle by using the FaceRectangle attribute.
B. Call the face detection API repeatedly and check for changes to the FaceAttributes.HeadPose attribute.
C. Call the face detection API and use the FaceLandmarks attribute to calculate the distance between pupils.
D. Call the face detection API repeatedly and check for changes to the FaceAttributes.Accessories attribute.

# Correct Answer:
A
"""

question_2_24 = """
# HOTSPOT

You make an API request and receive the results shown in the following exhibits.

HTTP request
POST https://facetesting.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&returnFaceAttributes=qualityforrecognition&recognitionModel=recognition_04&returnRecognitionModel=false&detectionModel=detection_03&faceIdTimeToLive=86400 HTTP/1.1
Hots: facetesting.cognitiveservices.azure.com
Content-Type: application/json
Ocp-Apim-Subscription-key: *******************************

{
    "url": "https://news.microsoft.com/wp-content-uploads/prod/sites/68/2021/11/EDU19_HigherEdStudentsOnCampus_002-1536*1024.jpg"
}

Response status
200 OK
Response content

  x-envoy-upstream-service-time: 1292
  apim-request-id: 8a3aa72f-5bad-45d0-b8a4-584312258f06
  Strict-Transport-Security: max-age=35136000; includeSubDomains; preload
  x-content-type-options: nosniff
  CSP-Billing-Usage: CognitiveServices.Face.Transaction=1
  Date: Sat, 04 Dec 2021 11:15:33 GMT
  Content-Length: 655
  Content-Type: application/json; charset=utf-8
  
  [{
    "faceId": "d14d131c-76ba-43e9-9e3d-dcf646e5022",
    "faceRectangle": {
      "top": 201,
      "left": 797,
      "width": 121,
      "height": 160,
    }，
    “faceAttributes”: {
      "qualityForRecognition": "high"
    }
  }, {
    "faceId": "a3a0f2ff-b015-464c-b87c-0dd09d0698da",
    "faceRectangle": {
      "top": 249,
      "left": 1167,
      "width": 103,
      "height": 159,
    }，
    “faceAttributes”: {
      "qualityForRecognition": "medium"
    }
  }, {
    "faceId": "45481ce8-dcc4-4564-a21c-3c15cd9c4fa",
    "faceRectangle": {
      "top": 191,
      "left": 497,
      "width": 85,
      "height": 178,
    }，
    “faceAttributes”: {
      "qualityForRecognition": "low"
    }
  }, {
    "faceId": "eac17649-effd-42c9-9093-4dd60fd4cfc7",
    "faceRectangle": {
      "top": 754,
      "left": 118,
      "width": 30,
      "height": 44,
    }，
    “faceAttributes”: {
      "qualityForRecognition": "low"
    }
  }]
  
Use the drop-down menus to select the answer choice that completes each statement based on the information presented in the graphic.
NOTE: Each correct selection is worth one point

Answer Area

The API [answer choice] faces. (detects / finds similar /recognizes/ verifies)
A face that can be used in person enrollment is at position [answer choice] within the photo (118, 754 / 497, 191 / 797, 201 / 1167, 249)

# Correct Answer:
detects, (797, 201)
"""

question_2_25 = """
# QUESTION
You have an Azure subscription that contains an AI enrichment pipeline in Azure Cognitive Search and an Azure Storage account that has 10 GB of scanned documents and images.
You need to index the documents and images in the storage account. The solution must minimize how long it takes to build the index.
What should you do?
A. From the Azure portal, configure parallel indexing.
B. From the Azure portal, configure scheduled indexing.
C. configure field mappings by using the REST API.
D. Create a text-based indexer by using the REST API.

# Correct Answer:
A
"""

question_2_26 = """
# DRAG DROP

You need to analyze video content to identify any mentions of specific company names.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Add the specific company names to the exclude list.
Add the specific company names to the include list.
From Content model customization, select Language.
Sign in to the Custom Vision website.
Sign in to the Azure Video Analyzer for Media website.
From Content model customization, select Brands.

# Correct Answer
Sign in to the Azure Video Analyzer for Media website.
From Content model customization, select Brands.
Add the specific company names to the include list.
"""

question_2_27 = """
# QUESTION

You have a mobile app that manages printed forms.
You need the app to send images of the forms directly to Forms Recognizer to extract relevant information. For compliance reasons, the image les must not be stored in the cloud.
In which format should you send the images to the Form Recognizer API endpoint?
A. raw image binary
B. form URL encoded
C. JSON

# Correct Answer:
A
"""

question_2_28 = """
# QUESTION

You plan to build an app that will generate a list of tags for uploaded images. The app must meet the following requirements:
• Generate tags in a user's preferred language.
• Support English, French, and Spanish.
• Minimize development effort.
You need to build a function that will generate the tags for the app.

Which Azure service endpoint should you use?
A. Content Moderator Image Moderation
B. Custom Vision image classification
C. Computer Vision Image Analysis
D. Custom Translator

# Correct Answer:
B
"""

question_2_29 = """
# HOTSPOT

You develop a test method to verify the results retrieved from a call to the Computer Vision API. The call is used to analyze the existence of company logos in images. The call returns a collection of brands named brands.
You have the following code segment.

foreach (var brand in brands)
{
    if (brand.Confidence >= .75)
        Console.WriteLine($"Logo of {brand_name} between {brand.rectangle.X}, {brand.rectangle.Y} and {brand.rectangle.W}, {brand.rectangle.H}")
}

For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point

Answer Area
Statements
The code will display the name of each detected brand with a confidence equal to or higher than 75 percent.
The code will display coordinates for the top-left corner of the rectangle that contains the brand logo of the displayed brands.
The code will display coordinates for the bottom-right corner of the rectangle that contains the brand logo of the displayed brands.

# Correct Answer
Yes, Yes, No
"""

question_2_30 = """
# DRAG DROP

You have a factory that produces cardboard packaging for food products. The factory has intermittent internet connectivity.
The packages are required to include four samples of each product.
You need to build a Custom Vision model that will identify defects in packaging and provide the location of the defects to an operator. The model must ensure that each package contains the four products.
Which project type and domain should you use? To answer, drag the appropriate options to the correct targets. Each option may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point

Options
Food
General
General(compact)
Image classification
Logo
Object detection

Answer Area
Project type: ______
Domain: ______

# Correct Answer:
Object detection, General(compact)
"""

question_2_31 = """
# HOTSPOT

You are building a model to detect objects in images.
The performance of the model based on training data is shown in the following exhibit.

Iteration 1
Finished training on 18/02/2022, 17:08:38 using General domain
Iteration id: eedf9f1a-1a9f-4d98-bf2c-ffc28bd8cae1
Precision 100.0%  Recall 25.0% mAP 77.2%

Use the drop-down menus to select the answer choice that completes each statement based on the information presented in the graphic.
NOTE: Each correct selection is worth one point

Answer Area
The Percentage of false positive is [answer choice]. (0 / 25 / 30 / 50 /100)
The value for the number of true positives divided by the total number of true positives and false negatives is [answer choice]. (0 / 25 / 30 / 50 /100)

# Correct Answer:
0, 25
"""

question_2_32 = """
# QUESTION
You are building an app that will include one million scanned magazine articles. Each article will be stored as an image le.
You need to configure the app to extract text from the images. The solution must minimize development effort.
What should you include in the solution?
A. Computer Vision Image Analysis
B. the Read API in Computer Vision
C. Form Recognizer
D. Azure Cognitive Service for Language

# Correct Answer:
A
"""

question_2_33 = """
# QUESTION
You have a 20-GB video le named File1.avi that is stored on a local drive.
You need to index File1.avi by using the Azure Video Indexer website.
What should you do rst?
A. Upload File1.avi to an Azure Storage queue.
B. Upload File1.avi to the Azure Video Indexer website.
C. Upload File1.avi to Microsoft OneDrive.
D. Upload File1.avi to the www.youtube.com webpage.

Correct Answer:
B
"""

question_2_34 = """
# HOTSPOT
You are building an app that will share user images.
You need to configure the app to meet the following requirements:
• Uploaded images must be scanned and any text must be extracted from the images.
• Extracted text must be analyzed for the presence of profane language.
• The solution must minimize development effort.
What should you use for each requirement? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point

Answer Area
Text extraction: (Azure AI Language / Azure AI Computer Vision / Content Moderator / Azure AI Custom Vision / Azure AI Document Intelligence)
Profane language detection: (Azure AI Language / Azure AI Computer Vision / Content Moderator / Azure AI Custom Vision / Azure AI Document Intelligence)

# Correct Answer:
Azure AI Document Intelligence, Content Moderator
"""

question_2_35 = """
# QUESTION

You are building an app that will share user images.
You need to configure the app to perform the following actions when a user uploads an image:
• Categorize the image as either a photograph or a drawing.
• Generate a caption for the image.
The solution must minimize development effort.
Which two services should you include in the solution? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

A. object detection in Azure AI Computer Vision
B. content tags in Azure AI Computer Vision
C. image descriptions in Azure AI Computer Vision
D. image type detection in Azure AI Computer Vision
E. image classification in Azure AI Custom Vision

# Correct Answer:
CE
"""

question_2_36 = """
# QUESTION

You are building an app that will use the Azure AI Video Indexer service.
You plan to train a language model to recognize industry-specic terms.
You need to upload a le that contains the industry-specic terms.
Which le format should you use?
A. XML
B. TXT
C. XLS
D. PDF

# Correct Answer:
B
"""

question_2_37 = """
# DRAG DROP

You have an app that uses Azure AI and a custom trained classier to identify products in images.
You need to add new products to the classier. The solution must meet the following requirements:
• Minimize how long it takes to add the products.
• Minimize development effort.
Which five actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions 
Label the sample images.
From Vision Studio, open the project.
Publish the model.
From the Custom Vision portal, open the project.
Retrain the model.
Upload sample images of the new product.
From the Azure Machine Learning studio, open the workspace.

# Correct Answer:
From Vision Studio, open the project.
Upload sample images of the new product.
Label the sample images.
Retrain the model.
Publish the model.
"""

question_2_38 = """
# HOTSPOT

You are developing an application that will use the Azure AI Vision client library. The application has the following code.

def analyze_image(local_image):
  with open(local_image, "rb") as image_stream:
  image_analysis = client.analyze_image_in_stream(
    image=image_stream,
    visual_features=[
      VisualFeatureTypes.tags,
      VisualFeatureTypes.description
    ]
  )
  for caption in image_analysis.description.captions:
    print(f"\n{caption.text} with confidence {caption.confidence}")
  for tag in image_analysis.tags:
    print(f"\n{tag.name} with confidence {tag.confidence}")  

For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Answer Area
Statements
The code will perform face recognition.
The code will list tags and their associated confidence.
The code will read an image file from the local file system.

# Correct Answer
No, Yes, Yes
"""

question_2_39 = """
# QUESTION
You are developing a method that uses the Azure AI Vision client library. The method will perform optical character recognition (OCR) in images. The method has the following code.

def read_file_url(computervision_client, url_file):
    read_response = computervision_client.read(url_file, raw=True)
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location_split("/")[-1]
    read_result = computervision_client.get_read_result(operation_id)
    
    for page in read_result.analyze_result.read_results:
        for line in page.lines:
            print(line.text)

During testing, you discover that the call to the get_read_result method occurs before the read operation is complete.
You need to prevent the get_read_result method from proceeding until the read operation is complete.
Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Remove the operation_id parameter.
B. Add code to verify the read_results.status value.
C. Add code to verify the status of the read_operation_location value.
D. Wrap the call to get_read_result within a loop that contains a delay.

Correct Answer:
BD
"""

question_2_40 = """
# HOTSPOT
You are developing an app that will use the Azure AI Vision API to analyze an image.
You need configure the request that will be used by the app to identify whether an image is clipart or a line drawing.
How should you complete the request? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
______ (GET / PATCH / POST)
"https://*.cognitiveservices.azure.com/vision/v3.2/analyze?visualFeatures=______(description / imageType / objects / tags)&details={string}&language=en-US"

# Correct Answer
POST, imageType
"""

question_2_41 = """
# HOTSPOT

You have an Azure subscription that contains an Azure AI Video Indexer account.
You need to add a custom brand and logo to the indexer and configure an exclusion for the custom brand.
How should you complete the REST API call? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
{
  "referenceUrl": "https://www.contoso.com/Contoso",
  "id": 97974,
  "name": "Contoso",
  "accountId": "ContosoAccountId",
  "lastModifierUserName": "SampleUserName",
  "created": "2023-04-25T14:59:52.7433333",
  "lastModified": "2023-04-25T14:59:52.7433333",
  ______("enabled" / "state" / "tags"/ "useBuiltin"): ______(["Excluded"] / ["included"] / false / true)
}

# Correct Answer
"enabled", false
"""

question_2_42 = """
# QUESTION

You have a local folder that contains the les shown in the following table.
___________________________________________
| Name  | Format | Length(mins) | Size(MB) |
| File1 | WMV    |          34  |     400  |
| File2 | AVI    |          90  |    1200  |
| File3 | MOV    |         300  |     980  |
| File4 | MP4    |          80  |    1800  |
--------------------------------------------

You need to analyze the les by using Azure AI Video Indexer.
Which files can you upload to the Video Indexer website?
A. File1 and File3 only
B. File1, File2, File3 and File4
C. File1, File2, and File3 only
D. File1 and File2 only
E. File1, File2, and File4 only

# Correct Answer:
B
"""

question_3_1 = """
# SCENARIO

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You build a language model by using a Language Understanding service. The language model is used to search for information on a contact list by using an intent named FindContact.
A conversational expert provides you with the following list of phrases to use for training.
✑ Find contacts in London.
✑ Who do I know in Seattle?
✑ Search for contacts in Ukraine.
You need to implement the phrase list in Language Understanding.

Solution: You create a new pattern in the FindContact intent.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B

Instead use a new intent for location.
Note: An intent represents a task or action the user wants to perform. It is a purpose or goal expressed in a user's utterance.
Dene a set of intents that corresponds to actions users want to take in your application.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-concept-intent
"""

