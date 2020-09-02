.PHONY: test
test:
	bash -c "source ./venv/bin/activate && nosetests -v --with-coverage test/"
