PYTHON="venv/bin/python"

install:
	@ ${PYTHON} -m pip install -r requirements.txt

compile:
	@ ${PYTHON} -m piptools compile requirements.in
    
sync:
	@ ${PYTHON} -m piptools sync requirements.txt
	@ ${PYTHON} -m pip install -e .

clean_logs:
	@ rm -r logs && mkdir logs && touch logs/.keep