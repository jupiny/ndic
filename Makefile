upload:
	- python setup.py sdist
	- twine upload dist/*
testupload:
	- twine upload --repository testpypi dist/*
