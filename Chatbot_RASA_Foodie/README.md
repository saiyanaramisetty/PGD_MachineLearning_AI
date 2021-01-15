# Foodie Restaurant Bot - Saiyana and Sunil

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 

Zomato apis are used for searching the restaurants. https://developers.zomato.com/documentation#/



### Prerequisites

Python 3.7.x(3.7.4)
Visual studio for Python development 
rasa                     1.10.16
rasa-core-sdk            0.14.0
rasa-sdk                 1.10.3
rasa-x                   0.32.2

### Installing ---- How to Run:

## Creating a virtual environment

Create the virtual environment by opening the command prompt and typing the following code:
$ python3 -m venv --system-site-packages ./venv

Activate the virtual environment by typing the following code:
$ source ./venv/bin/activate

## Installing RASA and RASA X

Install both Rasa and Rasa X using the following code:
$ pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

Install Rasa only:
$ pip install rasa 

## Install RASA NLU and Spacy
$ pip install rasa[spacy]
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en

## Training RASA:
$ rasa train

## Running Actions Server:
$ rasa run actions

## Running RASA shell:
$ rasa shell

## For Interactive Learning:
$ rasa interactive
```
Generated stories can be exported to a path and then added to stories.md. Retrain the model and check dialogue flow.
```

## Authors

* **Saiyana Ramisetty**
* **Sunil Indla**

## License

 ---- NA ----------