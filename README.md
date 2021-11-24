# Finetuning BioBert for arthropod gene name Named Entity Recognition

Project aims to collect a literature corpus as our training and testing data with automated or manual labeled entities, from abstracts in the arthropod sciences. We finetuned the [BioBert](https://github.com/dmis-lab/biobert-pytorch) to perform named-entity recognition (NER) for arthropod gene name.


### Requirment
`Python3` and `Colab`<br>
The introduction of [Colab](https://colab.research.google.com/?utm_source=scs-index#scrollTo=5fCEDCU_qrC0).

### Installation
- seqeval : Used for evaluation (`pip install seqeval`)
- inflect (`pip install inflect`)
- nltk (`pip install nltk`)
- transformers (`pip install transformers`)
- beautifulsoup4 (`pip install beautifulsoup4`)

### Preprocess
Before training, please run `preprocess.py` and `same_len.py` to process the dataset.

`preprocess.py`
- split our data into 10 folds (10 folds cross validation)
- convert .xml file to .tsv
- convert .tsv to .txt (generate with/without text name .txt file)

`same_len.py` (run `same_len.py` on with/without text name .txt file)
- preprocess to same length
- create train_dev.txt, devel.txt, test.txt and labels.txt

### Finetuning BioBert

Put the dataset (The directory contain train_dev.txt, devel.txt, test.txt and labels.txt) and `args.json`, `run_ner.ipynb` and `utils_ner.ipynb` on Colab.
The `args.json` stores the setting argument when training. (Remind: "max_seq_length" is the same as "max_len" in same_len.py) Because of 10 folds cross validation, please change the setting of args when you train the next fold.

### The result of 10 folds cross validation

| Test Fold      |    Test Precision (%)   |    Test Recall (%)   |    Test F1 (%)   |
|----------------|:-----------------------:|:--------------------:|:----------------:|
| fold_0         |          76.96          |         78.50        |       77.72      |
| fold_1         |          73.86          |         87.24        |       79.99      |
| fold_2         |          76.17          |         81.58        |       78.78      |
| fold_3         |          81.08          |         91.25        |       85.67      |
| fold_4         |          81.20          |         84.19        |       82.67      |
| fold_5         |          82.40          |         98.09        |       89.56      |
| fold_6         |          87.54          |         82.28        |       84.83      |
| fold_7         |          84.07          |         85.34        |       84.70      |
| fold_8         |          90.11          |         86.01        |       88.01      |
| fold_9         |          85.77          |         87.40        |       86.58      |

### Postprocess

After training, the test prediction of each fold would be saved in output directory. 
In `postprocess.py`, you can add text name in the test prediction and postprocess to the output format we want.