install: 
		pip install --upgrade pip &&\
				pip install -r requirements.txt

test: 
		python -m pytest -vv -ra --cov=hello --cov=greeting tests
		python -m pytest --nbval notebook.ipynb

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