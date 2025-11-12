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

question_3_2 = """
# SCENARIO

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You develop an application to identify species of flowers by training a Custom Vision model.
You receive images of new flower species.
You need to add the new images to the classier.
Solution: You add the new images, and then use the Smart Labeler tool.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B

The model need to be extended and retrained.
Note: Smart Labeler to generate suggested tags for images. This lets you label a large number of images more quickly when training a Custom Vision model.
"""

question_3_3 = """
# SCENARIO

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You develop an application to identify species of flowers by training a Custom Vision model.
You receive images of new flowers species.
You need to add the new images to the classier.

Solution: You add the new images and labels to the existing model. You retrain the model, and then publish the model.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
A

The model needs to be extended and retrained.
"""

question_3_4 = """
# SCENARIO

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You develop an application to identify species of flowers by training a Custom Vision model.
You receive images of new flowers species.
You need to add the new images to the classier.

Solution: You create a new model, and then upload the new images and labels.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B

The model needs to be extended and retrained.
"""

question_3_5 = """
# HOTSPOT

You are developing a service that records lectures given in English (United Kingdom).
You have a method named AppendToTranscriptFile that takes translated text and a language identifier.
You need to develop code that will provide transcripts of the lectures to attendees in their respective language. The supported languages are English, French, Spanish, and German.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:
static async Task TranslateSpeechAsync()
{
    var config = SpeechTranslationConfig.FromSubscription("69ccad5cc-0ab3-4704-bdff-afbf4aa07d85", "uksouth");
    var lang = new List<String> ______ ({"en-GB"} / {"fr", "de", "es"} / {"French", "Spanish", "German"} / {languages})
    config.SpeechRecognitionLanguage = "en-GB";
    config.ForEach(config.AddTargetLanguage);
    using var audioConfig = AudioConfig.FromDefaultMicrophoneInput();
    using var recognizer = new ______(IntentRecognizer / SpeakerRecognizer / SpeechSynthesizer / TranslationRecognizer) (config, audioConfig);
    var result = await recognizer.RecognizeOnceAsync();
    if (result.reason == ResultReason.TranslatedSpeech)
}

# Correct Answer:
{"fr", "de", "es"}, TranslationRecognizer

Box 1: {"fr", "de", "es"}
A common task of speech translation is to specify target translation languages, at least one is required but multiples are supported. The
following code snippet sets both French and German as translation language targets. static async Task TranslateSpeechAsync()
{
var translationCong =
SpeechTranslationCong.FromSubscription(SPEECH__SUBSCRIPTION__KEY, SPEECH__SERVICE__REGION);
translationCong.SpeechRecognitionLanguage = "it-IT";
// Translate to languages. See, https://aka.ms/speech/sttt-languages translationCong.AddTargetLanguage("fr");
translationCong.AddTargetLanguage("de");
}

Box 2: TranslationRecognizer -
After you've created a SpeechTranslationCong, the next step is to initialize a TranslationRecognizer.
Example code:
static async Task TranslateSpeechAsync()
{
var translationCong =
SpeechTranslationCong.FromSubscription(SPEECH__SUBSCRIPTION__KEY, SPEECH__SERVICE__REGION); var fromLanguage = "en-US"; 
var toLanguages = new List<string> { "it", "fr", "de" }; translationCong.SpeechRecognitionLanguage = fromLanguage;
toLanguages.ForEach(translationCong.AddTargetLanguage); using var recognizer = new TranslationRecognizer(translationCong);
}
"""

question_3_6 = """
# DRAG DROP

You train a Custom Vision model used in a mobile app.
You receive 1,000 new images that do not have any associated data.
You need to use the images to retrain the model. The solution must minimize how long it takes to retrain the model.
Which three actions should you perform in the Custom Vision portal? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:
Upload the images by category.
Get suggest tags.
Upload all the images.
Group the images locally into category folders.
Review the suggestions and confirm the tags.
Tag the images manually.

# Correct Answer:
Group the images locally into category folders.
Upload the images by category.
Tag the images manually.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classier
"""

question_3_7 = """
# QUESTION

You are building a Conversational Language Understanding model for an e-commerce chatbot. Users can speak or type their billing address when prompted by the chatbot.
You need to construct an entity to capture billing addresses.
Which entity type should you use?
A. machine learned
B. Regex
C. list
D. Pattern.any

# Correct Answer:
B

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-concept-entity-types
"""

question_3_8 = """
# QUESTION

You are building an Azure WebJob that will create knowledge bases from an array of URLs.
You instantiate a QnAMakerClient object that has the relevant API keys and assign the object to a variable named client.
You need to develop a method to create the knowledge bases.
Which two actions should you include in the method? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Create a list of FileDTO objects that represents data from the WebJob.
B. Call the client.Knowledgebase.CreateAsync method.
C. Create a list of QnADTO objects that represents data from the WebJob.
D. Create a CreateKbDTO object.

# Correct Answer:
AC

# Reference:
https://docs.microsoft.com/en-us/rest/api/cognitiveservices-qnamaker/qnamaker4.0/knowledgebase/create
"""

question_3_9 = """
# HOTSPOT
You are developing an application that includes language translation.
The application will translate text retrieved by using a function named getTextToBeTranslated. The text can be in one of many languages. The content of the text must remain within the Americas Azure geography.
You need to develop code to translate the text to a single language.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:
var endpoint = ______ ;
               ("https://api.cognitive.microsofttranslator.com/translate"
                "https://api.cognitive.microsofttranslator.com/transliterate"
                "https://api-apc.cognitive.microsofttranslator.com/detect"
                "https://api-nam.cognitive.microsofttranslator.com/detect"
                "https://api-nam.cognitive.microsofttranslator.com/translate" 
                )
var apikey = "FF956C68883B21B38691ABD200A4C606";
var text = getTextToBeTranslated;
var body = '[{"Text":"' + text + '"}]';
var client = new HttpClient();
client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", apikey);
______
(var uri = endpoint + "?from=en";
 var uri = endpoint + "?suggestedFrom=en";
 var uri = endpoint + "?to=en";
)
HttpResponseMessage response;
var content = new StringContent(body, Encoding.UTF8, "application/json");
var response = await client.PutAsync(uri, content);

# Correct Answer:
"https://api-nam.cognitive.microsofttranslator.com/translate", var uri = endpoint + "?to=en";
"""

question_3_10 = """
# QUESTION

You are building a conversational language understanding model.
You need to enable active learning.
What should you do?
A. Add show-all-intents=true to the prediction endpoint query.
B. Enable speech priming.
C. Add log=true to the prediction endpoint query.
D. Enable sentiment analysis.

# Correct Answer:
C

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-how-to-review-endpoint-utterances#log-user-queries-to-enable-active-learning
"""

question_3_11 = """
# HOTSPOT
You run the following command.
For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Hot Area:
Statements
Going to http://localhost:5000/status will query the Azure endpoint to verify whether the API key used to start the container is valid.
The container logging provider will write log data.
Going to http://localhost:5000/swagger will provide the details to access the documentation for the available endpoints.

# Correct Answer:
Yes, No, Yes

Box 1: Yes -
http://localhost:5000/status : Also requested with GET, this veries if the api-key used to start the container is valid without causing an endpoint query.
Box 2: No -
The command saves container and LUIS logs to output mount at C:\output, located on container host
Box 3: Yes -
http://localhost:5000/swagger : The container provides a full set of documentation for the endpoints and a Try it out feature. With this feature, you can enter your settings into a web-based HTML form and make the query without having to write any code. After the query returns, an example CURL command is provided to demonstrate the HTTP headers and body format that's required.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-container-howto
"""

question_3_12 = """
# QUESTION

You are building a Language Understanding model for an e-commerce platform.
You need to construct an entity to capture billing addresses.
Which entity type should you use for the billing address?
A. machine learned
B. Regex
C. geographyV2
D. Pattern.any
E. list

# Correct Answer:
A

Incorrect Answers:
B:A regular expression entity extracts an entity based on a regular expression pattern you provide. It ignores case and ignores cultural variant. Regular expression is best for structured text or a predened sequence of alphanumeric values that are expected in a certain format. For example:
Entity    Regular expression    Example
Flight Number   flight [A-Z]{2} [0-9]{4}   flight AS 1234
C: The prebuilt geographyV2 entity detects places. Because this entity is already trained, you do not need to add example utterances containing GeographyV2 to the application intents. GeographyV2 entity is supported in English culture.
The geographical locations have subtypes:
Subtype    Purpose
poi     Point of interest
city    name of city
country Region    name of country or region
continent    name of continent
state    name of state or province
D: Pattern.any is a variable-length placeholder used only in a pattern's template utterance to mark where the entity begins and ends.
E: A list entity represents a xed, closed set of related words along with their synonyms. You can use list entities to recognize multiple synonyms or variations and extract a normalized output for them. Use the recommend option to see suggestions for new words based on the current list.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-concept-entity-types
"""

question_3_13 = """
# QUESTION

You need to upload speech samples to a Speech Studio project for use in training.
How should you upload the samples?
A. Combine the speech samples into a single audio le in the .wma format and upload the le.
B. Upload a .zip le that contains a collection of audio les in the .wav format and a corresponding text transcript le.
C. Upload individual audio les in the FLAC format and manually upload a corresponding transcript in Microsoft Word format.
D. Upload individual audio les in the .wma format.

# Correct Answer:
B

To upload your data, navigate to the Speech Studio . From the portal, click Upload data to launch the wizard and create your rst dataset.
You'll be asked to select a speech data type for your dataset, before allowing you to upload your data.
The default audio streaming format is WAV
Use this table to ensure that your audio les are formatted correctly for use with Custom Speech:
Property    Value
File format    RIFF(WAV)
Sample rate    8000 Hz or 16000 Hz
Channels    1(mono)
Maximum length per audio    2 hours
Sample format    PCM, 16-bit
Archive format    .zip
Maximum archive size    2 GB
# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-speech-test-and-train
"""

question_3_14 = """
# QUESTION

You are developing a method for an application that uses the Translator API.
The method will receive the content of a webpage, and then translate the content into Greek (el). The result will also contain a transliteration that uses the Roman alphabet.
You need to create the URI for the call to the Translator API.
You have the following URI.
https://api.cognitive.microsofttranslator.com/translate?api-version=3.0
Which three additional query parameters should you include in the URI? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. toScript=Cyrl
B. from=el
C. textType=html
D. to=el
E. textType=plain
F. toScript=Latn

# Correct Answer:
CDF
C: textType is an optional parameter. It denes whether the text being translated is plain text or HTML text (used for web pages).
D: to is a required parameter. It species the language of the output text. The target language must be one of the supported languages included in the translation scope.
F: toScript is an optional parameter. It species the script of the translated text.
We use Latin (Roman alphabet) script.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate
"""

question_3_15 = """
# QUESTION

You have a chatbot that was built by using the Microsoft Bot Framework.
You need to debug the chatbot endpoint remotely.
Which two tools should you install on a local computer? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Fiddler
B. Bot Framework Composer
C. Bot Framework Emulator
D. Bot Framework CLI
E. ngrok
F. nginx

# Correct Answer:
CE

Bot Framework Emulator is a desktop application that allows bot developers to test and debug bots, either locally or remotely. ngrok is a cross-platform application that "allows you to expose a web server running on your local machine to the internet." Essentially, what we'll be doing is using ngrok to forward messages from external channels on the web directly to our local machine to allow debugging, as opposed to the standard messaging endpoint congured in the Azure portal.

# Reference:
https://docs.microsoft.com/en-us/azure/bot-service/bot-service-debug-emulator
"""

question_3_16 = """
# DRAG DROP

You are building a retail chatbot that will use a QnA Maker service.
You upload an internal support document to train the model. The document contains the following question: "What is your warranty period?"
Users report that the chatbot returns the default QnA Maker answer when they ask the following question: "How long is the warranty coverage?"
The chatbot returns the correct answer when the users ask the following question: 'What is your warranty period?"
Both questions should return the same answer.
You need to increase the accuracy of the chatbot responses.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.
Select and Place:

Actions
Add a new question and answer (QnA) pair.
Retrain the model.
Add additional questions to the document.
Republish the model.
Add alternative phrasing to the question and answer (QnA) pair.

# Correct Answer:
Add alternative phrasing to the question and answer (QnA) pair.
Retrain the model.
Republish the model.

Step 1: Add alternative phrasing to the question and answer (QnA) pair.
Add alternate questions to an existing QnA pair to improve the likelihood of a match to a user query.
Step 2: Retrain the model.
Periodically select Save and train after making edits to avoid losing changes.
Step 3: Republish the model -
Note: A knowledge base consists of question and answer (QnA) pairs. Each pair has one answer and a pair contains all the information associated with that answer.

Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/how-to/edit-knowledge-base
"""

question_3_17 = """
# Scenario

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You build a language model by using a Language Understanding service. The language model is used to search for information on a contact list by using an intent named FindContact.
A conversational expert provides you with the following list of phrases to use for training.
✑ Find contacts in London.
✑ Who do I know in Seattle?
✑ Search for contacts in Ukraine.
You need to implement the phrase list in Language Understanding.

Solution: You create a new intent for location.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
A

An intent represents a task or action the user wants to perform. It is a purpose or goal expressed in a user's utterance. Define a set of intents that corresponds to actions users want to take in your application.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-concept-intent
"""

question_3_18 = """
# Scenario

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You build a language model by using a Language Understanding service. The language model is used to search for information on a contact list by using an intent named FindContact.
A conversational expert provides you with the following list of phrases to use for training.
✑ Find contacts in London.
✑ Who do I know in Seattle?
✑ Search for contacts in Ukraine.
You need to implement the phrase list in Language Understanding.

Solution: You create a new entity for the domain.
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

question_3_19 = """
# QUESTION

You are training a Language Understanding model for a user support system.
You create the rst intent named GetContactDetails and add 200 examples.
You need to decrease the likelihood of a false positive.
What should you do?
A. Enable active learning.
B. Add a machine learned entity.
C. Add additional examples to the GetContactDetails intent.
D. Add examples to the None intent.

# Correct Answer:
D

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/conversational-language-understanding/concepts/none-intent#adding-examples-to-the-none-intent
"""

question_3_20 = """
# DRAG DROP
You are building a Language Understanding model for purchasing tickets.
You have the following utterance for an intent named PurchaseAndSendTickets.
Purchase [2 audit business] tickets to [Paris] [next Monday] and send tickets to [email@domain.com]
You need to select the entity types. The solution must use built-in entity types to minimize training data whenever possible.
Which entity type should you use for each label? To answer, drag the appropriate entity types to the correct labels. Each entity type may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.

Select and Place:
Entity Types
Email
List
Regex
GeographyV2
Machine learned

Answer Area
Paris:______
email@domain.com:______
2 audit business:______

# Correct Answer:
GeographyV2， Email， Machine learned

Box 1: GeographyV2 -
The prebuilt geographyV2 entity detects places. Because this entity is already trained, you do not need to add example utterances containing GeographyV2 to the application intents.
Box 2: Email -
Email prebuilt entity for a LUIS app: Email extraction includes the entire email address from an utterance. Because this entity is already trained, you do not need to add example utterances containing email to the application intents.
Box 3: Machine learned -
The machine-learning entity is the preferred entity for building LUIS applications.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-reference-prebuilt-geographyv2 
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-reference-prebuilt-email 
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/reference-entity-machine-learned-entity
"""

question_3_21 = """
# QUESTION

You have the following C# method.

static void create_resource(string resource_name, string kind, string account_tier, string location)
{
    CognitiveServicesAccount parameters = 
        new CognitiveServicesAccount(null, null, kind, location, resource_name, new CognitiveServicesAccountProperties(), new Sku(account_tier));
    var result = cog_sve_client.Accounts.Create(resource_group_name, account_tier, parameters);
}

You need to deploy an Azure resource to the East US Azure region. The resource will be used to perform sentiment analysis.
How should you call the method?
A. create_resource("res1", "ContentModerator", "S0", "eastus")
B. create_resource("res1", "TextAnalytics", "S0", "eastus")
C. create_resource("res1", "ContentModerator", "Standard", "East US")
D. create_resource("res1", "TextAnalytics", "Standard", "East US")

# Correct Answer:
B

To perform sentiment analysis, we specify TextAnalytics, not ContentModerator.
Possible SKU names include: 'F0','F1','S0','S1','S2','S3','S4','S5','S6','S7','S8'
Possible location names include: westus, eastus

# Reference:
https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/new-azcognitiveservicesaccoun
"""

question_3_22 = """
# QUESTION

You build a Conversational Language Understanding model by using the Language Services portal.
You export the model as a JSON file as shown in the following sample.
{
  "text": "average amount of rain by month at chicago last year",
  "intent": "Weather.CheckWeatherValue",
  "entities": [
    {
      "entity": "Weather.weatherRange",
      "startPos": 0,
      "endPos": 6,
      "children": []
    },
    {
      "entity": "Weather.weatherCondition",
      "startPos": 16,
      "endPos": 21,
      "children": []
    },
    {
      "entity": "Weather.Historic",
      "startPos": 23,
      "endPos": 30,
      "children": []
    },
  ]
}

To what does the Weather.Historic entity correspond in the utterance?
A. by month
B. chicago
C. rain
D. location

# Correct Answer:
A
"""

question_3_23 = """
# QUESTION

You are examining the Text Analytics output of an application.
The text analyzed is: `Our tour guide took us up the Space Needle during our trip to Seattle last week.`
The response contains the data shown in the following table.

Text    Category    ConfidenceScore
Tour guide    PersonType    0.45
Space Needle    Location    0.38
Trip     Event    0.78
Seattle    Location    0.78
last week    Time    0.80

Which Text Analytics API is used to analyze the text?
A. Entity Linking
B. Named Entity Recognition
C. Sentiment Analysis
D. Key Phrase Extraction

# Correct Answer:
B

Named Entity Recognition (NER) is one of the features offered by Azure Cognitive Service for Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. The NER feature can identify and categorize entities in unstructured text. For example: people, places, organizations, and quantities.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/overview
"""

question_3_24 = """
# SIMULATION

You need to configure and publish bot12345678 to support task management. The intent must be named TaskReminder. The LUDown for the intent is in the C:
\Resources\LU folder.
To complete this task, use the Microsoft Bot Framework Composer.

# Correct Answer:
See explanation below.
Step 1: Open Microsoft Bot Framework Composer
Step 2: Select the bot bot12345678
Step 3: Select Import existing resources. Read the instructions on the right side of the screen and select Next.
Step 4: Browse to the C:\Resources\LU folder and select the available .lu file
Step 5: In the pop-up window Importing existing resources, modify the JSON le content based on your resources information: Name the intent TaskReminder
Step 6: Select Publish from the Composer menu. In the Publish your bots pane, select the bot to publish (bot12345678), then select a publish profile from the Publish target drop-down list.

# Reference:
https://docs.microsoft.com/en-us/composer/how-to-publish-bot
"""

question_3_25 = """
# QUESTION

You need to configure bot12345678 support the French (FR-FR) language.
Export the bot to C:\Resources\Bot\Bot1.zip.
To complete this task, use the Microsoft Bot Framework Composer.

# Correct Answer:
See explanation below.
Step 1: Open Microsoft Bot Framework Composer
Step 2: Select the bot bot12345678
Step 3: Select Configure.
Step 4: Select the Azure Language Understanding tab
Step 5: Select the Set up Language Understanding button. The Set up Language Understanding window will appear, shown below:
Step 6: Select Use existing resources and then select Next at the bottom of the window.
Step 7: Now select the Azure directory, Azure subscription, and Language Understanding resource name (French).
Step 8: Select Next on the bottom. Your Key and Region will appear on the next on the next window, shown below
Step 9. Select Done.

# Reference:
https://docs.microsoft.com/en-us/composer/concept-language-understanding https://docs.microsoft.com/en-us/composer/how-to-add-luis
"""

question_3_26 = """
# SIMULATION

You need to configure and publish bot12345678 to answer questions by using the frequently asked questions (FAQ) located at 
https://docs.microsoft.com/en-us/azure/bot-service/bot-service-resources-bot-framework-faq. 
The solution must use bot%@lab.LabInstance.Id-qna-qna%.
To complete this task, use the Microsoft Bot Framework Composer.

# Correct Answer:
See explanation below.
Step 1: Open Microsoft Bot Framework Composer
Step 2: Select the bot bot12345678
Step 3: Open the configure page in Composer. Then select the Development resources, and scroll down to Azure QnA Maker.
Step 4: To access the Connect to QnA Knowledgebase action, you need to select + under the node you want to add the QnA knowledge base and then select Connect to QnAKnowledgeBase from the Access external resources action menu.
Step 5: Review the QnA Maker settings panel after selecting the QnA Maker dialog.
Use:
Instance: bot%@lab.LabInstance.Id-qna-qna%

# Reference:
https://docs.microsoft.com/en-us/composer/how-to-create-qna-kb https://docs.microsoft.com/en-us/composer/how-to-add-qna-to-bot
"""

question_3_27 = """
You need to measure the public perception of your brand on social media by using natural language processing.
Which Azure service should you use?
A. Language service
B. Content Moderator
C. Computer Vision
D. Form Recognizer

# Correct Answer:
A

Azure Cognitive Service for Language is a cloud-based service that provides Natural Language Processing (NLP) features for understanding and analyzing text.
Use this service to help build intelligent applications using the web-based Language Studio, REST APIs, and client libraries.
Note: Natural language processing (NLP) has many uses: sentiment analysis, topic detection, language detection, key phrase extraction, and document categorization.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/overview
"""

question_3_28 = """
# HOTSPOT

You are developing an application that includes language translation.
The application will translate text retrieved by using a function named get_text_to_be_translated. The text can be in one of many languages.
The content of the text must remain within the Americas Azure geography.
You need to develop code to translate the text to a single language.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Hot Area:

api_key = "FF956C68B83B21B38691ABD200A4C606",
text = get_text_to_be_translated()
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': api_key
    }
body = {
    'Text': text
    }
conn = httplib.HTTPSConnection______
                              ("api.cognitive.microsofttranslator.com")
                              ("api-apc.cognitive.microsofttranslator.com")
                              ("api-nam.cognitive.microsofttranslator.com")
conn.request("POST", ______, str(body), headers)
                     ("/translate?from=en"
                      "/translate?suggestedFrom=en"
                      "/translate?to=en"
                      "/detect?to=en"
                      "/detect?from=en"
                     )
response = conn.getresponse()
response_data = response.read()

# Correct Answer:
("api-nam.cognitive.microsofttranslator.com"), "/translate?to=en"

Box 1: ("api-nam.cognitive.microsofttranslator.com")
Geography USA: api-nam.cognitive.microsofttranslator.com
Datacenters: East US, South Central US, West Central US, and West US 2
Box 2: "/translate?to=en"
Must specify the language which it is being translated to. The 'to' parameter is required

Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-reference
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate
"""

question_3_29 = """
# QUESTION

You have the following data sources:
✑ Finance: On-premises Microsoft SQL Server database
✑ Sales: Azure Cosmos DB using the Core (SQL) API
✑ Logs: Azure Table storage
✑ HR: Azure SQL database
You need to ensure that you can search all the data by using the Azure Cognitive Search REST API.
What should you do?
A. Migrate the data in HR to Azure Blob storage.
B. Migrate the data in HR to the on-premises SQL server.
C. Export the data in Finance to Azure Data Lake Storage.
D. Ingest the data in Logs into Azure Sentinel.

# Correct Answer:
C

In Azure Cognitive Search, a data source is used with indexers, providing the connection information for ad hoc or scheduled data refresh of a target index, pulling data from supported Azure data sources.
Note: Supported data sources -
Indexers crawl data stores on Azure and outside of Azure.
Amazon Redshift (in preview)
Azure Blob Storage -
Azure Cosmos DB -
Azure Data Lake Storage Gen2 -
Azure MySQL (in preview)
Azure SQL Database -
Azure Table Storage -
Elasticsearch (in preview)
PostgreSQL (in preview)
Salesforce Objects (in preview)
Salesforce Reports (in preview)
Smartsheet (in preview)
Snowflake (in preview)
Azure SQL Managed Instance -
SQL Server on Azure Virtual Machines
Azure Files (in preview)

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-indexer-overview#supported-data-sources
"""

question_3_30 = """
# SIMULATION

Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com -
Azure Password: XXXXXXXXXXXX -
The following information is for technical support purposes only:
Lab Instance: 12345678 -
Task -
You need to create and publish a Language Understanding (classic) model named 1u12345678. The model will contain an intent of Travel that has an utterance of Boat.
To complete this task, sign in to the Language Understanding portal at https://www.luis-ai/.

# Correct Answer:
See explanation below.
Create your LUIS model -
1. You should navigate to your LUIS.ai management portal and create a new application. In the portal create a model.
Model name: 1u12345678 -
2. Dene one intent as Travel and add an example utterances of Boat.
3. Publish the model
In order to use your model, you have to publish it. This is as easy as hitting the Publish tab, selecting between the production or staging environments, and hitting Publish. As you can see from this page, you can also choose to enable sentiment analysis, speech priming to improve speech recognition, or the spell checker.
For now, you can leave those unchecked.

# Reference:
https://docs.microsoft.com/en-us/azure/health-bot/language_model_howto
https://www.codemag.com/article/1809021/Natural-Language-Understanding-with-LUIS
"""

question_3_31 = """
# SIMULATION

Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com -
Azure Password: XXXXXXXXXXXX -
The following information is for technical support purposes only:
Lab Instance: 12345678 -
Task -
You need to create a version of the 1u12345678 Language Understanding (classic) model. The new version must have a version name of 1.0
and must be active.
To complete this task, sign in to the Language Understanding portal at https://www.luis.ai/.

# Correct Answer:
See explanation below.
Step 1: Clone a version -
1. Select the version you want to clone (1u12345678) then select Clone from the toolbar.
2. In the Clone version dialog box, type a name for the new version. Type 1.0
Step 2: Set active version -
Select a version from the list, then select Activate from the toolbar.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-how-to-manage-versions
"""

question_3_32 = """
# QUESTION

You have a Language service resource that performs the following:
• Sentiment analysis
• Named Entity Recognition (NER)
• Personally Identifiable Information (PII) identification
You need to prevent the resource from persisting input data once the data is analyzed.

Which query parameter in the Language service API should you congure?
A. model-version
B. piiCategories
C. showStats
D. loggingOptOut

# Correct Answer:
D
"""

question_3_33 = """
# QUESTION

You have an Azure Cognitive Services model named Model1 that identifies the intent of text input.
You develop an app in C# named App1.
You need to configure App1 to use Model1.

Which package should you add to App1?
A. Universal.Microsoft.CognitiveServices.Speech
B. SpeechServicesToolkit
C. Azure.AI.Language.Conversations
D. Xamarin.Cognitive.Speech

# Correct Answer:
A
"""

question_3_34 = """
# HOTSPOT

You are building content for a video training solution.
You need to create narration to accompany the video content. The solution must use Custom Neural Voice.
What should you use to create a custom neural voice, and which service should you use to generate the narration? To answer, select the appropriate options in the answer area.
NOTE: Each correct answer is worth one point.

Answer Area
Custom neural voice: ______ (Microsoft Bot Framework Composer / The Azure portal / The Language Understanding portal / The Speech Studio portal)
Narration: ______ (Language Understanding / Speaker Recognition / Speech-to-text / Text-to-speech)

# Correct Answer
The Speech Studio portal, Text-to-speech
"""

question_3_35 = """
# HOTSPOT

You are building a call handling system that will receive calls from French-speaking and German-speaking callers. The system must perform the following tasks:
• Capture inbound voice messages as text.
• Replay messages in English on demand.
Which Azure Cognitive Services services should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
To capture messages: ______ (Speaker Recognition / Speech-to-text / Text-to-speech / Translator)
To replay messages: ______ (Speech-to-text only / Speech-to-text and Language / Speaker Recognition and Language / Text-to-speech and Language / Text-to-speech and Translator)

# Correct Answer:
Speech-to-text, Text-to-speech and Translator
"""

question_3_36 = """
# QUESTION

You are building a social media extension that will convert text to speech. The solution must meet the following requirements:
• Support messages of up to 400 characters.
• Provide users with multiple voice options.
• Minimize costs.
You create an Azure Cognitive Services resource.

Which Speech API endpoint provides users with the available voice options?
A. https://uksouth.api.cognitive.microsoft.com/speechtotext/v3.0/models/base
B. https://uksouth.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/voices
C. https://uksouth.tts.speech.microsoft.com/cognitiveservices/voices/list
D. https://uksouth.voice.speech.microsoft.com/cognitiveservices/v1?deploymentId={deploymentId}

# Correct Answer:
D
"""

question_3_37 = """
# QUESTION

You develop a custom question answering project in Azure Cognitive Service for Language. The project will be used by a chatbot.
You need to configure the project to engage in multi-turn conversations.
What should you do?
A. Add follow-up prompts.
B. Enable active learning.
C. Add alternate questions.
D. Enable chit-chat.

# Correct Answer:
A
"""

question_3_38 = """
# HOTSPOT

You are building a solution that students will use to nd references for essays.
You use the following code to start building the solution.

using Azure;
using System;
using Azure.AI.TextAnalytics;

private static readonly AzureKeyCredential credentials = new AzureKeyCredential("<key>");
private static readonly Uri endpoint = new Uri("<endpoint>");

static void EntityLinker(TextAnalyticsClient client)
{
    var response = client.RecognizeLinkedEntities(
        "Our tour guide took us up the Space Needle during our trip to Seattle lask week.");
}

For each of the following statements, select Yes is the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Answer Area
Statements
The Code will detect the language of documents.
The url attribute returned for each linked entity will be a Bing search link.
The matches attribute returned for each linked entity will provide the location in a document where the entity is referenced.

# Correct Answer
No, Yes, Yes
"""

question_3_39 = """
# QUESTION

You train a Conversational Language Understanding model to understand the natural language input of users.
You need to evaluate the accuracy of the model before deploying it.
What are two methods you can use? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.
A. From the language authoring REST endpoint, retrieve the model evaluation summary.
B. From Language Studio, enable Active Learning, and then validate the utterances logged for review.
C. From Language Studio, select Model performance.
D. From the Azure portal, enable log collection in Log Analytics, and then analyze the logs.

# Correct Answer:
AC
"""

question_3_40 = """
# DRAG DROP

You develop an app in C# named App1 that performs speech-to-speech translation.
You need to configure App1 to translate English to German.
How should you complete the SpeechTranslationCong object? To answer, drag the appropriate values to the correct targets. Each value may
be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

Values
addTargetLanguage
speechSynthesisLanguage
speechRecognitionLanguage
voiceName

Answer Area
var translationConfig = SpeechTranslationConfig.FromSubscription(SPEECH__SUBSCRIPTION__KEY, SPEECH__SERVICE__REGION);
     translationConfig.______ = "en-US";
     translationConfig.______ = ("de");
     
# Correct Answer
speechRecognitionLanguage, speechSynthesisLanguage
"""

question_3_41 = """
# QUESTION

You have an Azure subscription that contains an Azure Cognitive Service for Language resource.
You need to identify the URL of the REST interface for the Language service.
Which blade should you use in the Azure portal?
A. Identity
B. Keys and Endpoint
C. Networking
D. Properties

# Correct Answer:
B
"""

question_3_42 = """
# DRAG DROP

You are building a transcription service for technical podcasts.
Testing reveals that the service fails to transcribe technical terms accurately.
You need to improve the accuracy of the service.
Which ve actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Deploy the model.
Create a Custom Speech project.
Upload training datasets.
Create a speech-to-text model.
Create a Speaker Recognition model.
Train the model.
Create a Conversational Language Understanding model.

# Correct Answer:
Create a Custom Speech project.
Create a speech-to-text model.
Upload training datasets.
Train the model.
Deploy the model.
"""

question_3_43 = """
You are building a retail kiosk system that will use a custom neural voice.
You acquire audio samples and consent from the voice talent.
You need to create a voice talent profile.
What should you upload to the profile?
A. a .zip file that contains 10-second .wav files and the associated transcripts as .txt files
B. a five-minute .ac audio file and the associated transcript as a .txt file
C. a .wav or .mp3 file of the voice talent consenting to the creation of a synthetic version of their voice
D. a five-minute .wav or .mp3 file of the voice talent describing the kiosk system

Correct Answer:
C
"""

question_3_44 = """
# DRAG DROP

You have a Language Understanding solution that runs in a Docker container.
You download the Language Understanding container image from the Microsoft Container Registry (MCR).
You need to deploy the container image to a host computer.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
From the host computer, move the package file to the Docker input directory.
From the Language Understanding portal, export the solution as a package file.
From the host computer, build the container and specify the output directory.
From the host computer, run the container and specify the input directory.
From the language Understanding portal, retrain the model.

# Correct Answer:
From the Language Understanding portal, export the solution as a package file.
From the host computer, move the package file to the Docker input directory.
From the host computer, run the container and specify the input directory.
"""

question_3_45 = """
# HOTSPOT

You are building a text-to-speech app that will use a custom neural voice.
You need to create an SSML le for the app. The solution must ensure that the voice prole meets the following requirements:
• Expresses a calm tone
• Imitates the voice of a young adult female
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
```
  <mstts:express-as ______(role / style / styledegree / type / voice) ="YoungAdultFemale" ______(role / style / styledegree / type / voice)="gentle">
  How can I assist you?
  </mstts:express-as>
```

# Correct Answer:
role, style
"""

question_3_46 = """
# HOTSPOT

You have a collection of press releases stored as PDF les.
You need to extract text from the files and perform sentiment analysis.
Which service should you use for each task? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
Extract text: ______ (Azure Cognitive Search / Computer Vision / Form Recognizer)
Perform sentiment analysis: ______ (Azure Cognitive Search / Computer Vision / Form Recognizer / Language)

# Correct Answer:
Form Recognizer, Language
"""

question_3_47 = """
# QUESTION
You have a text-based chatbot.
You need to enable content moderation by using the Text Moderation API of Content Moderator.
Which two service responses should you use? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. personal data
B. the adult classification score
C. text classification
D. optical character recognition (OCR)
E. the racy classification score

# Correct Answer:
AC
"""

question_3_48 = """
# HOTSPOT

You are developing a text processing solution.
You have the function shown below.

static void GetKeyWords(TextAnalyticsClient textAnalyticsClient, string text)
{
    var response = textAnalyticsClient.RecognizeEntities (text);
    Console.WriteLine("Key words:");
    
    foreach (CategorizedEntity entity in response.Value)
    {
        Console.WriteLine($"\t{entity.Text}");
    }
}

For the second argument, you call the function and specify the following string.
Our tour of Paris included a visit to the Eiffel Tower
For each of the following statements, select Yes if the statement is true. Otherwise, select No.

Answer Area
Statements
The output will include the following words: our and included.
The output will include the following words: Paris, Eiffel, and Tower.
The function will output all the key phrases from the input string to the console.

# Correct Answer:
No, Yes, Yes
"""

question_3_49 = """
# HOTSPOT

You are building an Azure web app named App1 that will translate text from English to Spanish.
You need to use the Text Translation REST API to perform the translation. The solution must ensure that you have data sovereignty in the United States.
How should you complete the URI? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area

https://______/______?api-verision=3.0&to=es
(api.cognitive.microsofttranslator.com / api-nam.cognitive.microsofttranslator.com / api-nam.cognitiveservices.azure.com / eastus.api.cognitive.microsoft.com)
(detext / languages / text-to-speech / translate)

# Correct Answer:
api-nam.cognitive.microsofttranslator.com, translate
"""

question_3_50 = """
# DRAG DROP

You have a Docker host named Host1 that contains a container base image.
You have an Azure subscription that contains a custom speech-to-text model named model1.
You need to run model1 on Host1.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Retrain the model.
Request approval to run the container.
Export model1 to host1.
Run the container.
Configure disk logging.

# Correct Answer:
Request approval to run the container.
Retrain the model.
Run the container.
"""

question_3_51 = """
# SCENARIO

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.
After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You build a language model by using a Conversational Language Understanding. The language model is used to search for information on a contact list by using an intent named FindContact.
A conversational expert provides you with the following list of phrases to use for training.
• Find contacts in London.
• Who do I know in Seattle?
• Search for contacts in Ukraine.
You need to implement the phrase list in Conversational Language Understanding.

Solution: You create a new utterance for each phrase in the FindContact intent.
Does this meet the goal?
A. Yes
B. No

# Correct Answer:
B
"""

question_3_52 = """
# DRAG DROP

You have a question answering project in Azure Cognitive Service for Language.
You need to move the project to a Language service instance in a different Azure region.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
From the new Language service instance, train and publish the project.
From the new Language service instance, import the project file.
From the new Language service instance, enable custom text classification.
From the original Language service instance, export the existing project.
From the new Language service instance, regenerate the keys.
From the original Language service instance, tran and publish the model.

# Correct Answer:
From the original Language service instance, export the existing project.
From the new Language service instance, import the project file.
From the new Language service instance, train and publish the project.
"""

question_3_53 = """
# DRAG DROP
-
You are building a customer support chatbot.
You need to configure the bot to identify the following:
• Code names for internal product development
• Messages that include credit card numbers
The solution must minimize development effort.
Which Azure Cognitive Service for Language feature should you use for each requirement? To answer, drag the appropriate features to the correct requirements. Each feature may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

Features
Custom named entity recognition (NER)
Key phrase extraction
Language detection
Named Entity Recognition (NER)
Personally Identifiable information (PII) detection
Sentiment analysis

Answer Area
Identify code names for internal product development: ______
Identify messages that include credit card numbers: ______

# Correct Answer:
Custom named entity recognition (NER), Personally Identifiable information (PII) detection
"""

question_3_54 = """
# HOTSPOT

You are building an app by using the Speech SDK. The app will translate speech from French to German by using natural language processing.
You need to dene the source language and the output language.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
var speechTranslationConfig = 
SpeechTranslationConfig.FromSubscription(speechKey, speechRegion);
speechTranslationConfig.______(AddTargetLanguage / SpeechRecognitionLanguage / SpeechSynthesisLanguage / TargetLanguages / VoiceName)="fr"
speech_translation_config.______(AddTargetLanguage / SpeechRecognitionLanguage / SpeechSynthesisLanguage / TargetLanguages / VoiceName)="fr"

# Correct Answer:
SpeechRecognitionLanguage, AddTargetLanguage
"""

question_3_55 = """
# DRAG DROP

You have a collection of Microsoft Word documents and PowerPoint presentations in German.
You need to create a solution to translate the files to French. The solution must meet the following requirements:
• Preserve the original formatting of the files.
• Support the use of a custom glossary.
You create a blob container for German files and a blob container for French files. You upload the original files to the container for German files.
Which three actions should you perform in sequence to complete the solution? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Perform an asynchronous translation by using the list of files to be translated.
Perform an asynchronous translation by using the document translation specification.
Generate a list of files to be translated.
Upload a glossary file to the container for German files.
Upload a glossary file to the container for French files.
Define a document translation specification that has French target.

# Correct Answer:
Upload a glossary file to the container for German files.
Define a document translation specification that has French target.
Perform an asynchronous translation by using the document translation specification.
"""

question_3_56 = """
# QUESTION

You have the following C# function.

static void MyFunction(TextAnalyticsClient textAnalyticsClient, string text)
{
    var response = textAnalyticsClient.ExtractKeyPhrases(text);
    Console.WriteLine("Key phrases:");
    
    foreach (string keyphrase in response.Value)
    {
        Console.WriteLine($"{keyphrase}");
    }
}

You call the function by using the following code.

MyFunction(textAnalyticsClient, "the quick brown fox jumps over the lazy dog");

Which output will you receive?
A. The quick
The lazy
B. the quick brown fox jumps over the lazy dog
C. jumps over the
D. quick brown fox
lazy dog

# Correct Answer:
D
"""

question_3_57 = """
# QUESTION

You have the following Python method.

def create_resource (resource_name, kind, account_tier, location):
    parameters = CognitiveServiceAccount(sku=Sku(name=account_tier), kind=kind, location=location, properties={})
    result = cogSveClient.accounts.create(resource_group_name, resource_name, parameters)

You need to deploy an Azure resource to the East US Azure region. The resource will be used to perform sentiment analysis.
How should you call the method?
A. create_resource("res1", "TextAnalytics", "Standard", "East US")
B. create_resource("res1", "ContentModerator", "S0", "eastus")
C. create_resource("res1", "ContentModerator", "Standard", "East US")
D. create_resource("res1", "TextAnalytics", "S0", "eastus")

# Correct Answer:
D
"""

question_3_58 = """
# DRAG DROP

You develop a Python app named App1 that performs speech-to-speech translation.
You need to configure App1 to translate English to German.
How should you complete the SpeechTranslationCong object? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once or not at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

Values
add_target_language
speech_synthesis_language
speech_recognition_language
voice_name

Answer Area
def translate_speech_to_text():
    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)
    translation_config.______ = "en-US"
    translation_config.______ = "de"
    
# Correct Answer:
speech_recognition_language, add_target_language
"""

question_3_59 = """
# HOTSPOT

You are developing a streaming Speech to Text solution that will use the Speech SDK and MP3 encoding.
You need to develop a method to convert speech to text for streaming MP3 data.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area

audio_format = speechsdk.audio.______(compressed_stream_format=speechsdk.AudioStreamContainerFormat.MP3)
                               (AudioConfig.SetProperty / AudioStreamFormat / GetWaveFormatPCM / PullAudioinputStream)
stream = speechsdk.audio.PullAudioInputStream(stream_format=audio_format, pull_stream_callback=callback)
speech_config = speechsdk.SpeechConfig("18c51a87-3a69-47a8-aedc-a54745f708a1", "westus")
audio_config = speechsdk.audio.AudioConfig(stream=stream)
recognizer = speechsdk.______(speech_config=speech_config, audio_config=audio_config)
                       (KeywordRecognizer / SpeakerRecognizer / SpeechRecognizer / SpeechSynthesizer)
result = recognizer.recognize_once()
text = result.text

Correct Answer:
AudioStreamFormat, SpeechRecognizer
"""

question_3_60 = """
# HOTSPOT

You are building a chatbot.
You need to use the Content Moderator API to identify aggressive and sexually explicit language.
Which three settings should you configure? To answer, select the appropriate settings in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area

Content Moderator - Moderate
Text - Screen
The operation detects profanity in more than 100 languages and match against custom and shared blacklists.
Host
  Name
  Resource Name
Query parameters
  autocorrect
  PII
  listId
  classify
  language
Headers
  Content-Type
  Ocp-Apim-Subscription-Key
  
# Correct Answer:
autocorrect, classify, Ocp-Apim-Subscription-Key
"""

question_3_61 = """
# QUESTION

You are developing an app that will use the Decision and Language APIs.
You need to provision resources for the app. The solution must ensure that each service is accessed by using a single endpoint and credential.
Which type of resource should you create?
A. Language
B. Speech
C. Azure Cognitive Services
D. Content Moderator

# Correct Answer:
C
"""

question_3_62 = """
# QUESTION

You are building a chatbot.
You need to ensure that the bot will recognize the names of your company’s products and codenames. The solution must minimize development effort.
Which Azure Cognitive Service for Language service should you include in the solution?
A. custom text classification
B. entity linking
C. custom Named Entity Recognition (NER)
D. key phrase extraction

# Correct Answer:
C
"""

question_3_63 = """
# QUESTION

You have an Azure subscription that contains an Azure App Service app named App1.
You provision a multi-service Azure Cognitive Services resource named CSAccount1.
You need to configure App1 to access CSAccount1. The solution must minimize administrative effort.
What should you use to configure App1?
A. a system-assigned managed identity and an X.509 certificate
B. the endpoint URI and an OAuth token
C. the endpoint URI and a shared access signature (SAS) token
D. the endpoint URI and subscription key

# Correct Answer:
D
"""

question_3_64 = """
# QUESTION

You have an Azure subscription that contains a multi-service Azure Cognitive Services Translator resource named Translator1.
You are building an app that will translate text and documents by using Translator1.
You need to create the REST API request for the app.
Which headers should you include in the request?
A. the access control request, the content type, and the content length
B. the subscription key and the client trace ID
C. the resource ID and the content language
D. the subscription key, the subscription region, and the content type

# Correct Answer:
D
"""

question_3_65 = """
# QUESTION

You have a file share that contains 5,000 images of scanned invoices.
You need to analyze the images. The solution must extract the following data:
• Invoice items
• Sales amounts
• Customer details
What should you use?
A. Custom Vision
B. Azure AI Computer Vision
C. Azure AI Immersive Reader
D. Azure AI Document Intelligence

# Correct Answer:
D
"""

question_3_66 = """
# HOTSPOT

You are developing a text processing solution.
You have the function shown below.

def get_key_words(textAnalyticClient, text):
    response = textAnalyticClient.recognize_entities(documents = [text])[0]
    print("Key Words:")
    for entity in response.entities:
        print("\t\t", entity.text)

For the second argument, you call the function and specify the following string.
Our tour of Paris included a visit to the Eiffel Tower
For each of the following statements, select Yes if the statement is true. Otherwise, select No.

Answer Area
Statements
The output will include the following words: our and included.
The output will include the following words: Paris, Eiffel, and Tower.
The function will output all the key phrases from the input string to the console.

# Correct Answer:
No, Yes, Yes
"""

question_3_67 = """
# HOTSPOT

You are developing a text processing solution.
You develop the following method.

def get_key_phrases(text_analytics_client, text):
    response = text_analytics_client.extract_key_phrases(text, language="en")
    print('Key phrases:')
    for keyphrase in response.key_phrases:
        print(f'\t{keyphrase}')

You call the method by using the following code.

get_key_phrases(text_analytics_client, "the cat sat on the mat")

For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Answer Area
Statements
The call will output key phrases from the input string to the console.
The output will contain the following words: the, cat, sat, on and mat.
The output will contain the confidence level for key phrases.

# Correct Answer:
Yes, No, No
"""

question_3_68 = """
# HOTSPOT

You are developing a service that records lectures given in English (United Kingdom).
You have a method named append_to_transcript_le that takes translated text and a language identifier.
You need to develop code that will provide transcripts of the lectures to attendees in their respective language. The supported languages are English, French, Spanish, and German.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point

Answer Area

speech_key = os.environ['SPEECH__SUBSCRIPTION__KEY']
service region = os.environ['SPEECH_SERVICE_REGION']
def translate_speech():
    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)
    translation_config.speech_recognition_language = "en-GB"
    languages = ______ ((['en-GB']) / (['fr', 'de', 'es']) / (['French', 'Spanish', 'German']) / (['languages']))
    for language in languages: translation_config.add_target_language(language)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.translation.______(IntentRecognizer( / SpeakerRecognizer( / SpeechSynthesizer( / TranslationRecognizer( ) translation_config=translation_config, audio_config=audio_config)
    result = recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        append_to_transcript_file(result.text, "en")
        for language in result.translations:
            append_to_transcript_file(result.translations[language], language)
            
# Correct Answer:
(['fr', 'de', 'es']), TranslationRecognizer(
"""

question_3_69 = """
# QUESTION

You are developing an app that will use the text-to-speech capability of the Azure AI Speech service. The app will be used in motor vehicles.
You need to optimize the quality of the synthesized voice output.
Which Speech Synthesis Markup Language (SSML) attribute should you congure?
A. the style attribute of the mstts:express-as element
B. the effect attribute of the voice element
C. the pitch attribute of the prosody element
D. the level attribute of the emphasis element

# Correct Answer:
B
"""

question_3_70 = """
# QUESTION

You are designing a content management system.
You need to ensure that the reading experience is optimized for users who have reduced comprehension and learning differences, such as dyslexia. The solution must minimize development effort.
Which Azure service should you include in the solution?
A. Azure AI Immersive Reader
B. Azure AI Translator
C. Azure AI Document Intelligence
D. Azure AI Language

# Correct Answer:
A
"""

question_3_71 = """
# HOTSPOT

You are building an app that will answer customer calls about the status of an order. The app will query a database for the order details and provide the customers with a spoken response.
You need to identify which Azure AI service APIs to use. The solution must minimize development effort.
Which object should you use for each requirement? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
Convert customer calls into text queries: ______ (SpeechRecognizer / SpeechSynthesizer / TranslationRecognizer / VoiceProfileClient)
Provide customers with the order details: ______ (SpeechRecognizer / SpeechSynthesizer / TranslationRecognizer / VoiceProfileClient)

# Correct Answer:
TranslationRecognizer, SpeechSynthesizer
"""

question_3_72 = """
# QUESTION

You have an Azure AI service model named Model1 that identifies the intent of text input.
You develop a Python app named App1.
You need to configure App1 to use Model1.
Which package should you add to App1?
A. azure-cognitiveservices-language-textanalytics
B. azure-ai-language-conversations
C. azure-mgmt-cognitiveservices
D. azure-cognitiveservices-speech

# Correct Answer:
D
"""

question_3_73 = """
# HOTSPOT

You are building an app that will automatically translate speech from English to French, German, and Spanish by using Azure AI service.
You need to dene the output languages and configure the Azure AI Speech service.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area

speech_key, service_region = os.environ['SPEECH__SERVICE__KEY'], os.environ['SPEECH_SERVICE_REGION']
languages = ______ (['en-GB'] / ['en', 'fr', 'de', 'es'] / ['fr', 'de', 'es'] / ["French", "Spanish", "German"])
def translate_speech_to_text():
  translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)
  for lang in languages:
    translation_config.add_target_language(lang)
      for lang in languages:
        translation_config.add_language(lang)
    recognizer = speechsdk.translation.______ (intentRecognizer / SpeakerRecognizer / SpeechSynthesizer / TranslationRecognizer) (translation_config=translation_config)
    
# Correct Answer:
['fr', 'de', 'es'], TranslationRecognizer
"""

question_3_74 = """
# DRAG DROP

You plan to implement an Azure AI Search resource that will use custom skill based on sentiment analysis.
You need to create a custom model and configure Azure AI Search use the model.
Which ve actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Actions
Create an endpoint for the model.
Rerun the indexer to enrich the index.
Create an Azure Machine Learning workspace.
Create and train the model in the Azure Machine Learning studio.
Provision an Azure AI Services resource and obtain the endpoint.
Connect the custom skill the endpoint.

# Correct Answer:
Create an Azure Machine Learning workspace.
Provision an Azure AI Services resource and obtain the endpoint.
Connect the custom skill the endpoint.
Create and train the model in the Azure Machine Learning studio.
Rerun the indexer to enrich the index.
"""

question_3_75 = """
# HOTSPOT

You have a collection of press releases stored as PDF les.
You need to extract text from the les and perform sentiment analysis.
Which service should you use for each task? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
Extract text:______ (Azure AI Search / Azure AI Vision / Azure AI Document Intelligence)
Perform sentiment analysis:______ (Azure Cognitive Search / Azure AI Computer Vision / Azure AI Document Intelligence / Azure AI Language)

# Correct Answer:
Azure AI Document Intelligence, Azure AI Language
"""

question_3_76 = """
# QUESTION

You are building an internet-based training solution. The solution requires that a user's camera and microphone remain enabled.
You need to monitor a video stream of the user and verify that the user is alone and is not collaborating with another user. The solution must minimize development effort.
What should you include in the solution?
A. speech-to-text in the Azure AI Speech service
B. object detection in Azure AI Custom Vision
C. Spatial Analysis in Azure AI Vision
D. object detection in Azure AI Custom Vision

# Correct Answer:
A
"""

question_3_77 = """
# QUESTION

You are developing an app that will use the Speech and Language APIs.
You need to provision resources for the app. The solution must ensure that each service is accessed by using a single endpoint and credential.
Which type of resource should you create?
A. Azure AI Language
B. Azure AI Speech
C. Azure AI Services
D. Azure AI Content Safety

# Correct Answer:
C
"""

question_3_78 = """
# HOTSPOT

You are building an app that will automatically translate speech from English to French, German, and Spanish by using Azure AI service.
You need to dene the output languages and configure the Azure AI Speech service.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area

static async Task TranslateSpeechAsync()
{
  var config = SpeechTranslationConfig.FromSubscription(SPEECH__SUBSCRIPTION__KEY, SPEECH__SERVICE__REGION);
  var languages = new List<string>______; (["en-GB"] / ["en", "fr", "de", "es"] / ["fr", "de", "es"] / ["French", "German", "Spanish"])
  languages.ForEach(config.AddTargetLanguage);
  usingvar recognizer = new ______; (IntentRecognizer / SpeakerRecognizer / SpeechSynthesizer / TranslationRecognizer)
}

# Correct Answer:
["fr", "de", "es"], TranslationRecognizer
"""

question_3_79 = """
# QUESTION

You are developing a text processing solution.
You have the following function.

static void GetKeyWords(TextAnalyticsClient textAnalyticsClient, string text)
{
    var response = textAnalyticsClient.RecognizeEntities(text);
    Console.WriteLine("Key words:");
    
    foreach (CategorizedEntity entity in response.Value)
    {
        Console.WriteLine($"\t{entity.Text}");
    }
}

You call the function and use the following string as the second argument.

Our tour of London included a visit to Buckingham Palace

What will the function return?
A. London and Buckingham Palace only
B. Tour and visit only
C. London and Tour only
D. Our tour of London included visit to Buckingham Palace

# Correct Answer:
A
"""

question_3_80 = """
# QUESTION

You have the following Python function.

def my_function(textAnalyticsClient, text):
    response = textAnalyticsClient.extract_key_phrases(documents = [text])[0]
    print("Key Phrases:")
    for phrase in response.key_phrases:
        print(phrase)

You call the function by using the following code.

my_function(text_analytics_client, "the quick brown fox jumps over the lazy dog")

Following 'Key phrases', what output will you receive?
A. The quick
The lazy
B. jumps over the
C. quick brown fox
lazy dog
D. the quick brown fox jumps over the lazy dog

# Correct Answer:
C
"""

question_3_81 = """
# QUESTION

You have an Azure subscription.
You need to deploy an Azure AI Search resource that will recognize geographic locations.
Which built-in skill should you include in the skillset for the resource?
A. AzureOpenAIEmbeddingSkill
B. DocumentExtractionSkill
C. EntityRecognitionSkill
D. EntityLinkingSkill

# Correct Answer:
C
"""

question_4_1 = """
HOTSPOT

You are developing a text processing solution.
You develop the following method.

static void GetKeyPhrases(TextAnalyticsClient textAnalyticsClient, string text)
{
    var response = textAnalyticsClient.ExtractKeyPhrases(text);
    Console.WriteLine("Key phrases:");
    
    foreach (string keyphrase in response.Value)
    {
        Console.WriteLine($"\t{keyphrase}");
    }
}

You call the method by using the following code.
GetKeyPhrases(textAnalyticsClient, "the cat sat on the mat");
For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.

Hot Area:
Statements
The call will output key phrases from the input string to the console.
The output will contain the following words: the cat, sat, on and mat.
The output will contain the confidence level for key phrases.

Correct Answer:
Yes, No, No

Box 1: Yes -
The Key Phrase Extraction API evaluates unstructured text, and for each JSON document, returns a list of key phrases.
Box 2: No -
'the' is not a key phrase.
This capability is useful if you need to quickly identify the main points in a collection of documents. For example, given input text "The food was delicious and there were wonderful staff", the service returns the main talking points: "food" and "wonderful staff".
Box 3: No -
Key phrase extraction does not have confidence levels.

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-keyword-extraction
"""

question_4_2 = """
# QUESTION

You deploy a web app that is used as a management portal for indexing in Azure Cognitive Search. The app is configured to use the primary admin key.
During a security review, you discover unauthorized changes to the search index. You suspect that the primary access key is compromised.
You need to prevent unauthorized access to the index management endpoint. The solution must minimize downtime.
What should you do next?
A. Regenerate the primary admin key, change the app to use the secondary admin key, and then regenerate the secondary admin key.
B. Change the app to use a query key, and then regenerate the primary admin key and the secondary admin key.
C. Regenerate the secondary admin key, change the app to use the secondary admin key, and then regenerate the primary key.
D. Add a new query key, change the app to use the new query key, and then delete all the unused query keys.

# Correct Answer:
A

Regenerate admin keys.
Two admin keys are created for each service so that you can rotate a primary key, using the secondary key for business continuity.
1. In the Settings >Keys page, copy the secondary key.
2. For all applications, update the API key settings to use the secondary key.
3. Regenerate the primary key.
4. Update all applications to use the new primary key.
Note: Two admin api-keys, referred to as primary and secondary keys in the portal, are automatically generated when the service is created and can be individually regenerated on demand. Having two keys allows you to roll over one key while using the second key for continued access to the service.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-security-api-keys#regenerate-admin-keys
"""

question_4_3 = """
# QUESTION

You have an existing Azure Cognitive Search service.
You have an Azure Blob storage account that contains millions of scanned documents stored as images and PDFs.
You need to make the scanned documents available to search as quickly as possible.
What should you do?
A. Split the data into multiple blob containers. Create a Cognitive Search service for each container. Within each indexer definition, schedule the same runtime execution pattern.
B. Split the data into multiple blob containers. Create an indexer for each container. Increase the search units. Within each indexer definition, schedule a sequential execution pattern.
C. Create a Cognitive Search service for each type of document.
D. Split the data into multiple virtual folders. Create an indexer for each folder. Increase the search units. Within each indexer definition, schedule the same runtime execution pattern.

# Correct Answer:
D

Incorrect Answers:
A: Need more search units to process the data in parallel.
B: Run them in parallel, not sequentially.
C: Need a blob indexer.
Note: A blob indexer is used for ingesting content from Azure Blob storage into a Cognitive Search index.
Index large datasets
Indexing blobs can be a time-consuming process. In cases where you have millions of blobs to index, you can speed up indexing by partitioning your data and using multiple indexers to process the data in parallel. Here's how you can set this up:
✑ Partition your data into multiple blob containers or virtual folders
✑ Set up several data sources, one per container or folder.
✑ Create a corresponding indexer for each data source. All of the indexers should point to the same target search index.
✑ One search unit in your service can run one indexer at any given time. Creating multiple indexers as described above is only useful if they actually run in parallel.

Reference:
https://docs.microsoft.com/en-us/azure/search/search-howto-indexing-azure-blob-storage
"""

question_4_4 = """
# QUESTION

You need to implement a table projection to generate a physical expression of an Azure Cognitive Search index.
Which three properties should you specify in the skillset definition JSON configuration table node? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. tableName
B. generatedKeyName
C. dataSource
D. dataSourceConnection
E. source

# Correct Answer:
ABE

Defining a table projection.
Each table requires three properties:
✑ tableName: The name of the table in Azure Storage.
✑ generatedKeyName: The column name for the key that uniquely identifies this row.
✑ source: The node from the enrichment tree you are sourcing your enrichments from. This node is usually the output of a shaper, but could be the output of any of the skills.

# Reference:
https://docs.microsoft.com/en-us/azure/search/knowledge-store-projection-overview
"""

question_4_5 = """
# HOTSPOT
You are creating an enrichment pipeline that will use Azure Cognitive Search. The knowledge store contains unstructured JSON data and scanned PDF documents that contain text.
Which projection type should you use for each data type? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:
JSON data: ______ (File projection / Object projection / Table projection)
Scanned data: ______ (File projection / Object projection / Table projection)

# Correct Answer:
Object projection, File projection

Box 1: Object projection -
Object projections are JSON representations of the enrichment tree that can be sourced from any node.
Box 2: File projection -
File projections are similar to object projections and only act on the normalized_images collection.

# Reference:
https://docs.microsoft.com/en-us/azure/search/knowledge-store-projection-overview
"""

question_4_6 = """
HOTSPOT -
You are building an Azure Cognitive Search custom skill.
You have the following custom skill schema definition.

{
  "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
  "description": "My custom skill description",
  "uri": "https//contoso-webskill.azurewebsites.net/api/process",
  "context": "/document/organizations/*",
  "inputs": [
    {
      "name": "companyName",
      "source": "/document/organizations/*"
    }
  ],
  "outputs": [
    {
      "name": "companyDescription",
    }
  ]
}

For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.
Hot Area:

Statements
CompanyDescription is available for indexing.
The definition calls a web API as part of the enrichment process.
The enrichment step is called only for the first organization under "/document/organizations".

# Correct Answer:
Yes, Yes, No

Box 1: Yes -
Once you have defined a skillset, you must map the output fields of any skill that directly contributes values to a given eld in your search index.
Box 2: Yes -
The definition is a custom skill that calls a web API as part of the enrichment process.
Box 3: No -
For each organization identified by entity recognition, this skill calls a web API to nd the description of that organization.

# Reference:
https://docs.microsoft.com/en-us/azure/search/cognitive-search-output-field-mapping
"""

question_4_7 = """
# QUESTION

You have the following data sources:
✑ Finance: On-premises Microsoft SQL Server database
✑ Sales: Azure Cosmos DB using the Core (SQL) API
✑ Logs: Azure Table storage
HR: Azure SQL database -
You need to ensure that you can search all the data by using the Azure Cognitive Search REST API.
What should you do?
A. Configure multiple read replicas for the data in Sales.
B. Mirror Finance to an Azure SQL database.
C. Ingest the data in Logs into Azure Data Explorer.
D. Ingest the data in Logs into Azure Sentinel.

# Correct Answer:
B

On-premises Microsoft SQL Server database cannot be used as an index data source.
Note: Indexer in Azure Cognitive Search: : Automate aspects of an indexing operation by configuring a data source and an indexer that you can schedule or run on demand. This feature is supported for a limited number of data source types on Azure.
Indexers crawl data stores on Azure.
✑ Azure Blob Storage
✑ Azure Data Lake Storage Gen2 (in preview)
✑ Azure Table Storage
✑ Azure Cosmos DB
✑ Azure SQL Database
✑ SQL Managed Instance
✑ SQL Server on Azure Virtual Machines

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-indexer-overview#supported-data-sources
"""

question_4_8 = """
# QUESTION

You are developing a solution to generate a word cloud based on the reviews of a company's products.
Which Text Analytics REST API endpoint should you use?
A. keyPhrases
B. sentiment
C. languages
D. entities/recognition/general

# Correct Answer:
A

# Reference:
https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview
"""

question_4_9 = """
# DRAG DROP
You have a web app that uses Azure Cognitive Search.
When reviewing billing for the app, you discover much higher than expected charges. You suspect that the query key is compromised.
You need to prevent unauthorized access to the search endpoint and ensure that users only have read only access to the documents collection. The solution must minimize app downtime.
Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:
Actions
Add a new query key.
Regenerate the secondary admin key.
Change the app to use the secondary admin key.
Change the app to use the new key.
Regenerate the primary admin key.
Delete the compromised key.

# Correct Answer:
Add a new query key.
Change the app to use the new key.
Delete the compromised key.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-security-api-keys
"""

question_4_10 = """
# QUESTION

You are developing an application that will use Azure Cognitive Search for internal documents.
You need to implement document-level filtering for Azure Cognitive Search.
Which three actions should you include in the solution? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. Send Azure AD access tokens with the search request.
B. Retrieve all the groups.
C. Retrieve the group memberships of the user.
D. Add allowed groups to each index entry.
E. Create one index per group.
F. Supply the groups as a filter for the search requests.

# Correct Answer:
CDF

Your documents must include a eld specifying which groups have access. This information becomes the filter criteria against which documents are selected or rejected from the result set returned to the issuer.
D: A query request targets the documents collection of a single index on a search service.
CF: In order to trim documents based on group_ids access, you should issue a search query with a group_ids/any(g:search.in(g, 'group_id1,
group_id2,...')) filter, where 'group_id1, group_id2,...' are the groups to which the search request issuer belongs.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search
"""

question_4_11 = """
# QUESTION

You have an Azure Cognitive Search solution and an enrichment pipeline that performs Sentiment Analysis on social media posts.
You need to dene a knowledge store that will include the social media posts and the Sentiment Analysis results.
Which two fields should you include in the definition? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.
A. storageContainer
B. storageConnectionString
C. files
D. tables
E. objects

# Correct Answer:
BE
Knowledge store definition -
A knowledge store is defined inside a skillset definition and it has two components:
A connection string to Azure Storage Projections that determine whether the knowledge store consists of tables, objects or files.
The projections element is an array. You can create multiple sets of table-object-file combinations within one knowledge store.
"knowledgeStore": {
"storageConnectionString":"<YOUR-AZURE-STORAGE-ACCOUNT-CONNECTION-STRING>",
"projections":[
{
"tables":[ ],
"objects":[ ],
"files":[ ]
}
}
The type of projection you specify in this structure determines the type of storage used by knowledge store.
Objects - project JSON document into Blob storage. The physical representation of an object is a hierarchical JSON structure that represents an enriched document.
Tables - project enriched content into Table Storage. Dene a table projection when you need tabular reporting structures for inputs to analytical tools or export as data frames to other data stores. You can specify multiple tables within the same projection group to get a subset or cross section of enriched documents. Within the same projection group, table relationships are preserved so that you can work with all of them.
Projected content is not aggregated or normalized. The following screenshot shows a table, sorted by key phrase, with the parent document indicated in the adjacent column. In contrast with data ingestion during indexing, there is no linguistic analysis or aggregation of content.
Plural forms and differences in casing are considered unique instances.
Incorrect:
Not C: files - project image les into Blob storage. A file is an image extracted from a document, transferred intact to Blob storage.
Although it is named "files", it shows up in Blob Storage, not file storage.
"""

question_4_12 = """
# SIMULATION -
Use the following login credentials as needed:
To enter your username, place your cursor in the Sign in box and click on the username below.
To enter your password, place your cursor in the Enter password box and click on the password below.
Azure Username: admin@abc.com -
Azure Password: XXXXXXXXXXXX -
The following information is for technical support purposes only:
Lab Instance: 12345678

Task -
You need to create an Azure resource named solution12345678 that will index a sample database named realestate-us-sample. The solution must ensure that users can search the index in English for people, organizations, and locations.
To complete this task, sign in to the Azure portal.

# Correct Answer:
See explanation below.
Step 1 - Start the Import data wizard and create a data source
1. Sign in to the Azure portal with your Azure account.
2. Find your search service and on the Overview page, click Import data on the command bar to create and populate a search index.
3. In the wizard, click Connect to your data, and select the sample database named realestate-us-sample
Step 2 - Skip the "Enrich content" page
The wizard supports the creation of an AI enrichment pipeline for incorporating the Cognitive Services AI algorithms into indexing.
We'll skip this step for now, and move directly on to Customize target index.
Step 3 - Configure index -
The solution must ensure that users can search the index in English for people, organizations, and locations.
Configure Searchable for the fields people, organizations, and locations.

# Reference:
https://docs.microsoft.com/en-us/azure/search/search-get-started-portal
"""

question_4_13 = """
# HOTSPOT

You create a knowledge store for Azure Cognitive Search by using the following JSON.

"knowledgeStore": {
    ”storageConnectionString“: "DefaultEndpointsProtocol=https;AccountName=<Acct Name>;AccountKey=<Acct Key>;",
    "projections": [
        {
            "tables": [
                {
                    "tableName": "unrelatedDocument",
                    "generatedKeyName": "Documentid",
                    "source": "/document/pbiShape"
                },
                {
                    "tableName": "unrelatedKeyPhrases",
                    "generatedKeyName": "KeyPhraseid",
                    "source": "/document/pbiShape/keyPhrases"
                }
            ],
            "objects": [
            
            ],
            "files": []
        },
        {
            "tables": [],
            "objects": [
                {
                    "storageContainer": "unrelatedocrtext,
                    "source": null,
                    "sourceContext": "/document/normalized_images/*/text",
                    "inputs": [
                        {
                            "name": "ocrText",
                            "source": "/document/normalized_images/*/text"
                        }
                    ]
                },
                {
                    "storageContainer": "unrelatedocrlayout",
                    "source": null,
                    "sourceContext": "/document/normalized_images/*/layoutText",
                    "inputs": [
                        {
                            "name": "ocrLayoutText",
                            "source": "/document/normalized_images/*/layoutText"
                        }
                    ]
                }
            ],
            "files": []
        }    
    ]
}

Use the drop-down menus to select the answer choice that completes each statement based on the information presented in the graphic.
NOTE: Each correct selection is worth one point.

Answer Area
There will be ______. (no projection groups / one projection groups / two projection groups / four projection groups)
Normalized images will ______. (not be projected / be projected to Azure Blob storage / be projected to Azure File storage / be saved to an Azure Table storage)

# Correct Answer:
two projection groups, be projected to Azure Blob storage
"""

question_4_14 = """
# QUESTION

You plan create an index for an Azure Cognitive Search service by using the Azure portal. The Cognitive Search service will connect to an Azure SQL database.
The Azure SQL database contains a table named UserMessages. Each row in UserMessages has a eld named MessageCopy that contains the text of social media messages sent by a user.
Users will perform full text searches against the MessageCopy eld, and the values of the eld will be shown to the users.
You need to configure the properties of the index for the MessageCopy eld to support the solution.
Which attributes should you enable for the eld?
A. Sortable and Retrievable
B. Filterable and Retrievable
C. Searchable and Facetable
D. Searchable and Retrievable

# Correct Answer:
D
"""

question_4_15 = """
# QUESTION

You have the following data sources:
• Finance: On-premises Microsoft SQL Server database
• Sales: Azure Cosmos DB using the Core (SQL) API
• Logs: Azure Table storage
• HR: Azure SQL database
You need to ensure that you can search all the data by using the Azure Cognitive Search REST API.

What should you do?
A. Export the data in Finance to Azure Data Lake Storage.
B. Configure multiple read replicas for the data in Sales.
C. Ingest the data in Logs into Azure Data Explorer.
D. Migrate the data in HR to Azure Blob storage.

# Correct Answer:
A
"""

question_4_16 = """
# HOTSPOT

You plan to provision Azure Cognitive Services resources by using the following method.
You need to create a Standard tier resource that will convert scanned receipts into text.

static void provision_resource(CognitiveServicesManagementClient client, string name, string kind, string tier, string location)
{
  CognitiveServicesAccount parameters = 
    new CognitiveServicesAccount(null, null, kind, location, name, new CognitiveServicesAccountProperties(), new Sku(tier));
  result = client.Accounts.Create(resource_group_name, tier, parameters);
}

How should you call the method? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area

provision_resource("res1", ______ ______
                           (ComputerVision / CustomVision.Prediction / CustomVision.Training / FormRecognizer)
                           ("eastus", "S1") / "useast", "S1") / "S0", "eastus") / "S0", "useast"))
                           
# Correct Answer:
FormRecognizer, "S0", "eastus")

The current name for Form Recognizer (as of May 2024) is Document Intelligence.
https://azure.microsoft.com/en-us/pricing/details/ai-document-intelligence/
"""

question_4_17 = """
# HOTSPOT

You have an app named App1 that uses Azure AI Document Intelligence to analyze medical records and provide pharmaceutical dosage recommendations for patients.
You send a request to App1 and receive the following response.

{
  "status": "succeeded",
  "createdDateTime": "2023-09-14T21:01:02Z",
  "lastUpdateDateTime": "2023-09-14T21:01:03Z",
  "analyzeResult": {
    "apiVersion": "2023-07-31",
    "modelId": "prebuilt-healthInsuranceCard.us",
    "stringIndexType": "utf16CodeUnit",
    "content": "Blood Pressure 118/72",
    "pages": [
      {
        ...
        "words": [
          {
            "content": "Blood",
            "polygon": [ ... ],
            "confidence": 0.766,
            "span": [ ... ]
          },
          {
            "content": "Pressure",
            "polygon": [ ... ],
            "confidence": 0.716,
            "span": [ ... ]
          },
          {
            "content": "118/72",
            "polygon": [ ... ],
            "confidence": 0.761,
            "span": [ ... ]
          }
        ],
        ...
      "documents": [
        {
          "docType": "healthInsuranceCard.us",
          "boundingRegions": [ ... ]
        }
      ],
      "fields": {},
      "confidence": 1,
      "spans": [ ... ]
      }
    ]
  }
}

For each of the following statements, select Yes if the statement is true. Otherwise, select No
NOTE: Each correct selection is worth one point.

Answer Area
Statements
The chosen model is suitable for the intended use case.
The text content was recognized with greater than 70 percent confidence.
The form elements were recognized with greater than 70 percent confidence.

# Correct Answer:
No, Yes, Yes
"""

question_4_18 = """
# HOTSPOT

You have an Azure subscription that contains an Azure AI Document Intelligence resource named DI1.
You build an app named App1 that analyzes PDF les for handwritten content by using DI1.
You need to ensure that App1 will recognize the handwritten content.
How should you complete the code? To answer, select the appropriate options in the answer area.

Answer Area

Uri fileUri = new Uri("<fileUri>");
AnalyzeDocumentOperation operation = await client.AnalyzeDocumentFromUriAsync(WaitUtil.Completed, ______("prebuilt-document", / "prebuilt-contract", / "prebuilt-read",) fileUri);
AnalyzeResult result = operation.Value;
foreach (DocumentStyle style in result.Styles)
{
  bool isHandwritten = style.IsHandwritten.HasValue && style.IsHandwritten == true;
  if (isHandwritten && style.Confidence > ______(0.1 / 0.75 / 1.0))
    {
      Console.WriteLine($"Handwritten content found:");
      foreach (DocumentSpan span in style.Spans)
      
# Correct Answer:
"prebuilt-document", , 0.75
"""

question_4_19 = """
# QUESTION

You have an app named App1 that uses a custom Azure AI Document Intelligence model to recognize contract documents.
You need to ensure that the model supports an additional contract format. The solution must minimize development effort.
What should you do?
A. Lower the confidence score threshold of App1.
B. Create a new training set and add the additional contract format to the new training set. Create and train a new custom model.
C. Add the additional contract format to the existing training set. Retrain the model.
D. Lower the accuracy threshold of App1.

# Correct Answer:
C
"""

question_4_20 = """
# HOTSPOT

You have an Azure subscription.
You need to deploy an Azure AI Document Intelligence resource.
How should you complete the Azure Resource Manager (ARM) template? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point

Answer Area
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {},
  "variables": {},
  "resources": [
    {
      "type": "______ (Microsoft.CognitiveSearch / Microsoft.CognitiveServices / Microsoft.MachineLearning / Microsoft.MachineLearningServices) /accounts",
      "apiVersion": "2023-05-01",
      "name": "DocumentIntelligenceDemo",
      "location": "westeurope",
      "sku": {
        "name": "F0"
      },
      "kind": ______ ("AiBuilder", / "CognitiveSearch", / "FormRecognizer", / "OpenAI")
    }
  ]
}

# Correct Answer:
Microsoft.CognitiveServices, "FormRecognizer",
"""

question_4_21 = """
# QUESTION

You are building an app named App1 that will use Azure AI Document Intelligence to extract the following data from scanned documents:
• Shipping address
• Billing address
• Customer ID
• Amount due
• Due date
• Total tax
• Subtotal
You need to identify which model to use for App1. The solution must minimize development effort.
Which model should you use?
A. custom extraction model
B. contract
C. invoice
D. general document

# Correct Answer:
C
"""

question_4_22 = """
# QUESTION

You have the following data sources:
• Finance: On-premises Microsoft SQL Server database
• Sales: Azure Cosmos DB using the Core (SQL) API
• Logs: Azure Table storage
• HR: Azure SQL database
You need to ensure that you can search all the data by using the Azure AI Search REST API.
What should you do?
A. Migrate the data in HR to Azure Blob storage.
B. Migrate the data in HR to the on-premises SQL server.
C. Export the data in Finance to Azure Data Lake Storage.
D. Migrate the data in Sales to the MongoDB API.

# Correct Answer:
C
"""

question_4_23 = """
# QUESTION

You are building an app that will process scanned expense claims and extract and label the following data:
• Merchant information
• Time of transaction
• Date of transaction
• Taxes paid
• Total cost
You need to recommend an Azure AI Document Intelligence model for the app. The solution must minimize development effort.
What should you use?
A. the prebuilt Read model
B. a custom template model
C. a custom neural model
D. the prebuilt receipt model

# Correct Answer:
D
"""

question_4_24 = """
# HOTSPOT

You are building a language learning solution.
You need to recommend which Azure services can be used to perform the following tasks:
• Analyze lesson plans submitted by teachers and extract key fields, such as lesson times and required texts.
• Analyze learning content and provide students with pictures that represent commonly used words or phrases in the text.
The solution must minimize development effort.
Which Azure service should you recommend for each task? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
Analyze lesson plans: ______ (Azure Cognitive Search / Azure AI Custom Vision / Azure AI Document Intelligence / Immersive Reader)
Analyze learning content: ______ (Azure Cognitive Search / Azure AI Custom Vision / Azure AI Document Intelligence / Immersive Reader)

# Correct Answer
Azure AI Document Intelligence, Immersive Reader
"""

question_4_25 = """
# HOTSPOT

You have an Azure subscription.
You plan to build a solution that will analyze scanned documents and export relevant fields to a database.
You need to recommend which Azure AI service to deploy for the following types of documents:
• Internal expenditure request authorization forms
• Supplier invoices
The solution must minimize development effort.
What should you recommend for each document type? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
Internal expenditure request authorization forms: ______ (An Azure AI Document Intelligence custom model / An Azure AI Document Intelligence pre-built model / Azure AI Custom Vision / Azure AI Immersive Reader / Azure AI Vision)
Supplier invoices: ______ (An Azure AI Document Intelligence custom model / An Azure AI Document Intelligence pre-built model / Azure AI Custom Vision / Azure AI Immersive Reader / Azure AI Vision)

# Correct Answer:
An Azure AI Document Intelligence custom model,  An Azure AI Document Intelligence pre-built model
"""

question_4_26 = """
# QUESTION

You have an Azure AI Search resource named Search1.
You have an app named App1 that uses Search1 to index content.
You need to add a custom skill to App1 to ensure that the app can recognize and retrieve properties from invoices by using Search1.
What should you include in the solution?
A. Azure AI Immersive Reader
B. Azure OpenAI
C. Azure AI Document Intelligence
D. Azure AI Custom Vision

# Correct Answer:
C
"""

question_4_27 = """
# HOTSPOT

You have an Azure subscription.
You plan to build a solution that will analyze scanned documents and export relevant fields to a database.
You need to recommend an Azure AI Document Intelligence model for the following types of documents:
• Expenditure request authorization forms
• Structured and unstructured survey forms
• Structured employment application forms
The solution must minimize development effort and costs.
Which type of model should you recommend for each document type? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area:
Expenditure request authorization forms: ______ (Custom neural / Custom template / Prebuilt contract / Prebuilt invoice / Prebuilt layout)
Structured employment application forms: ______ (Custom neural / Custom template / Prebuilt contract / Prebuilt invoice / Prebuilt layout)
Structured and unstructured survey forms:  ______ (Custom neural / Custom template / Prebuilt contract / Prebuilt invoice / Prebuilt layout)

# Correct Answer:
Custom template, Prebuilt contract, Custom neural
"""

question_4_28 = """
# QUESTION

You have an Azure subscription that contains an Azure AI Document Intelligence resource named AIdoc1 in the S0 tier.
You have the les shown in the following table.

Name Format Password-locked Size(MB)
File1 JPG N/A 400
File2 PDF No  250
File3 PNG N/A 600
File4 XLSX No 900
File5 PDF Yes 160

You need to train a custom extraction model by using AIdoc1.
Which les can you upload to Document Intelligence Studio?
A. File1, File2, and File4 only
B. File2, and File5 only
C. File2, File4, and File5 only
D. File1, File2, File3, File4, and File5
E. File1 and File2 only

# Correct Answer:
E
"""

question_4_29 = """
# QUESTION

You have an Azure subscription that contains an Azure AI Document Intelligence resource named DI1. DI1 uses the Standard S0 pricing tier.
You have the les shown in the following table.

Name Size Description
File1.pdf 800MB Contains scanned images
File2.jpg 1KB An image that has 25 x 25 pixels
File3.tiff 5MB An image that has 5000 x 5000 pixels

Which files can you analyze by using DI1?
A. File1.pdf only
B. File2.jpg only
C. File3.tiff only
D. File2.jpg and File3.tiff only
E. File1.pdf, File2.jpg, and File3.tiff
Correct Answer:
B
"""

question_4_30 = """
HOTSPOT

You have an Azure subscription that contains an Azure AI Document Intelligence resource named DI1.
You build an app named App1 that analyzes PDF les for handwritten content by using DI1.
You need to ensure that App1 will recognize the handwritten content.
How should you complete the code? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

Answer Area
document_analysis_client = DocumentAnalysisClient(
  endpoint=endpoint, credential=AzureKeyCredential(key)
)
with open(<filePath>, "rb") as f:
  poller = document_analysis_client.begin_analyze_document(
    ______ ("prebuilt-document", / "prebuilt-contract", / "prebuilt-read") document=f
  )
result = poller.result()
for style in result.styles:
  if style.ishandwritten and style.confidence > ______ (0.1 / 0.75 / 1.0)
    print("Document contains handwritten content: ")
    print(",".join([result.content[span.offset:span.offset + span.length] for span in style.spans]))
    
# Correct Answer:
"prebuilt-document", , 0.75
"""

# 489