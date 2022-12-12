activate fea_model
python -m pytest tests/ --cov-report term-missing --cov='.'  -k "test_orcaflex_model"


