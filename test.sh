py test.py
py -m build
twine check dist/*
twine upload --repository testpypi dist/* --verbose

# conda create -y -n py39 python=3.9

conda activate py39
pip install --upgrade -i https://test.pypi.org/simple/ x256numpy
py demo.py

twine upload dist/* --verbose
