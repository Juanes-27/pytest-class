install: 
		pip install --upgrade pip &&\
				pip install -r requirements.txt

test: 
		python -m pytest -vvv -ra --cov=hello --cov=greeting --cov=smath --cov=web tests

test_web: 
		python -m pytest -v tests/test_web.py # if you just want to test web
test_nb:
		python -m pytest --nbval notebook.ipynb # if you just want to test notebook
debug: 
		python -m pytest -vv --pdb #Debugger is invoked

onetest:
		python -m pytest -vv tests/test_greeting.py::test_my_name4
debugthree: 
		#not working as expected
		python -m pytest -vv --pdb --maxfail=4

format: 
		black *.py

lint: 
		pylint --disable=R,C hello.py

all: install lint test format