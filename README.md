# Finetuning BioBert for Arthropod gene name Named Entity Recognition

### Project aims to collect a literature corpus as our training and testing data with automated or manual labeled entities, from abstracts in the arthropod sciences. <bt>


### Requirment
`Python3` and `Colab`<br>

### Installation
- seqeval : Used for evaluation (`pip install seqeval`)
- inflect (`pip install inflect`)
- nltk (`pip install nltk`)
- transformers (`pip install transformers`)
- beautifulsoup4 (`pip install beautifulsoup4`)

### Preprocess
`preprocess.py`
- split our data into 10 folds
- convert .xml file to .tsv
- convert .tsv to .txt (with/without text name)
`same_len.py`
- preprocess to same length
- create train_dev.txt, devel.txt, test.txt 

### Finetuning BioBert
# NER
