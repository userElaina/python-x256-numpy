# cd gen
# py gen.py
# cd ..

py test.py
py -m build
twine check dist/*
twine upload --repository testpypi dist/* --verbose

# conda create -y -n py39 python=3.9
# pip install --upgrade x256offline

conda activate py39
pip install --upgrade -i https://test.pypi.org/simple/ x256numpy
py demo.py

conda deactivate
twine upload dist/* --verbose
