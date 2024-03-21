# bento-meta-poc
simple proof-of-concept and usage of bento-meta


## Instructions

### get code
```
git clone https://github.com/CBIIT/bento-mdf.git
git clone https://github.com/CBIIT/bento-meta.git
git clone https://github.com/CBIIT/c3dc-model
```

get data 
```
mkdir data
cp c3dc-model/model-desc/* data/
```

Setup venv
```
python3 -m venv venv
source venv/bin/activate
```

install modules
```shell
cd bento-meta/python/
pip3 install .
cd ../../
```

```
cd bento-mdf/drivers/python
pip3 install .
cd ../../../
```

```shell
pip3 install -r requirements.txt
```

run code

```
python3 ./poc.py
```

then you should see some warnings (safe to ignore for now), followed by the following six lines:
```
...
diagnosis
participant
sample
study
survival
reference_file
```

