default:
    @cat makefile

env:
    python3 -m venv env
    source ~/bin/activate; pip install -r requirements.txt

run:
    python bin/clockdeco_param.py

< your code here so the following task ALWAYS gets called, even though the directory exists >
tests:
    pytest -vv tests
