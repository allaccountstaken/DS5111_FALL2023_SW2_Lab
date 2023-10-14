default:
	@cat makefile

env:
	python3 -m venv env
	. env/bin/activate; pip install -r requirements.txt
<<<<<<< HEAD

run:
	@. env/bin/activate; python3 bin/clockdeco_param.py

lint:
	. env/bin/activate; pylint bin/perceptron.py


# your code here so the following task ALWAYS gets called, even though the directory exists >
=======
run:
	@. env/bin/activate; python3 bin/clockdeco_param.py

lint:
	. env/bin/activate; pylint bin/perceptron.py

#< your code here so the following task ALWAYS gets called, even though the directory exists >
>>>>>>> 9db617d3f359c3c3ce7b2c29748d89c7f99be42b
.PHONY: tests
tests:
	. env/bin/activate; pytest -vv tests
