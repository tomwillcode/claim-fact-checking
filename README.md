# claim-fact-checking
A cli, python based application to fact check a statement by comparing to relevant and recent news.
## Installation
### Local Environment with Conda
```
git clone https://github.com/yatshunlee/claim-fact-checking.git
conda env create -f env/environment.yml
conda activate claim-fact-check
```
### Colab Environment
```
!pip install -U -q transformers
!pip install -U -q accelerate
!pip install -q news-please
!pip install -q google
!pip install -U -q sentence-transformers
!pip install nltk
!pip install requests-html
```
One way to go is to upload the .py files you will need into the folder for the colab you are using as seen in the picture below, but you can also pull this github repository to your google drive as a new folder in your google drive and you can change the colabs working directory to the FactChecker folder.
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/abe63700-cc9a-40cc-b7cb-9e10c39f8ccb)

you will definitely want to use the best GPU you can through colab if you are using Gemma-2b locally. At least some GPU resources are available for free. Be sure to adjust the run-time as needed. 

## Usage with OpenAI GPT 3.5
1. replace with your valid openai api key in `fraud_detection_gpt_3_5.py`
2. run `python main_gpt_3_5.py`
## Usage with Google Gemma-2b-it
1. replace with your valid huggingface access token in `fraud_detection_gemma.py`
2. run `python main_gemma.py`
## Architecture

1. Retrieve a statement / query that the user wants to fact-check.
2. Retrieve up to 10 regular results, and 10 news results with the Google Search API.
3. Perform webscrapping to get relevant content from the results using NewsPlease and requests-html.
4. Find the top 5 sentences that are most similar to the original query (on topic) based on cosine-similarity.
5. Design the prompt by retrieval augmented generation (RAG) based on the top 5 sentences as context.
6. Feed the context and query to LLM.
7. LLM determines if the claim is fraud or not.
## Fact Checker
### Check statement: Joe Biden told people not to vote
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/87ceed02-dafc-4d07-bec7-bb404efc0a3d)
#### GPT 3.5
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/ae35abcf-0955-4743-b743-753ec157887a)
#### Gemma-2b-it
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/eb70817f-4dd9-46c7-bde2-76a452960681)
### Check statement: Taylor Swift Promoting Le Creuset Cookware
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/b1cd6117-3410-4fd8-8f5a-2af6e04bed98)
#### GPT 3.5
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/78646f09-0061-41ea-84bc-b45eb7bc1aaf)
#### Gemma-2b-it
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/55bf5b27-dc0c-40c4-b683-96b75f051a0b)

