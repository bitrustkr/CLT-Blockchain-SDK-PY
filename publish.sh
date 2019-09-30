# build
echo '======= build ======='
set -x
python3 setup.py bdist_wheel

# upload
echo '======= upload ======='
set -x
twine upload dist/EITRI-1.8-py3-none-any.whl