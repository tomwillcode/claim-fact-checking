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
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/abe63700-cc9a-40cc-b7cb-9e10c39f8ccb)
## Usage with OpenAI GPT 3.5
1. replace with your valid openai api key in `fraud_detection_gpt_3_5.py`
2. run `python main_gpt_3_5.py`
## Usage with Google Gemma-2b-it
1. replace with your valid huggingface access token in `fraud_detection_gemma.py`
2. run `python main_gemma.py`
## Architecture
![image](https://github.com/yatshunlee/claim-fact-checking/assets/69416199/a530c314-702e-4729-be1a-3159da2e98e1)
1. Retrieve a statement / query that the user wants to fact-check.
2. Make it a better google search query: sites, keywords, time range.
3. Perform webscrapping to get relevant news content about the query: Google Search, NewsPlease.
4. Utilize text entailment to keep top relevent news by their titles. Then conduct sentence embedding and KNN to get the most relevant sentences in the news.
5. Design the prompt by retrieval augmented generation (RAG).
6. Fit into the GPT 3.5 model to generate a response.
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

