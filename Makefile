setup: requirements.txt
	echo "setup"
	pip install -r requirements.txt

install: setup.py
	echo "install"
	python setup.py install

clean:
	echo "clean"
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

run:
	echo "run"
	python presence.py

