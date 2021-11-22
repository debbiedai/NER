# Finetuning BioBert for arthropod gene name Named Entity Recognition

Project aims to collect a literature corpus as our training and testing data with automated or manual labeled entities, from abstracts in the arthropod sciences. We finetuned the [BioBert](https://github.com/dmis-lab/biobert-pytorch) to perform named-entity recognition (NER) for arthropod gene name.


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
