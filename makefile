default:
    @cat makefile

env:
    python3 -m venv env
    . env/bin/activate; pip install -r requirements.txt
run:
    . env/bin/activate; python3 bin/clockdeco_param.py

#< your code here so the following task ALWAYS gets called, even though the directory exists >
tests:
    . env/bin/activate; pytest -vv tests
