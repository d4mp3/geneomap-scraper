# geneomap

## Run virtual env and install dependencies

```
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Get batch links

```
python3 get_batch_links.py

```

## Run scrapper

```
python scraper/scraper.py --first 0 --last 10 -l -v --num_of_threads 0

```

## Run unit tests

```
python -m unittest discover -s scraper/ -p 'test_*.py'
```

## Run unit tests with coverage

```
coverage run --branch -m unittest discover -s scraper/ -p 'test_*.py'
coverage report
```
    
