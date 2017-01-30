.PHONY: init_venv deps freeze clean_venv

all: init_venv deps
	PYTHONPATH=venv ; . venv/bin/activate

init_venv:
	if [ ! -e "venv/bin/activate_this.py" ] ; then PYTHONPATH=venv ; virtualenv --clear venv ; fi

deps:
	PYTHONPATH=venv ; . venv/bin/activate && venv/bin/pip install -U -r requirements.txt && if [ "$(ls requirements)" ] ; then venv/bin/pip install -U -r requirements/* ; fi

freeze:
	. venv/bin/activate && venv/bin/pip freeze > requirements.txt

clean_venv:
	rm -rf venv
