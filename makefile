setup:
	python3 -m venv .venv;
	source .venv/bin/activate;
	pip install -r requirements.txt;

run-local:
	uvicorn main:app --reload
