
Testcase for this bug: https://code.djangoproject.com/ticket/33582.

To reproduce the issue:

```
# install Poetry
# taken from https://python-poetry.org/docs/#installation, see there if problems
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

poetry install

./manage.py migrate --database default
./manage.py migrate --database other

# This fails - and it should work:
cat books.json | ./manage.py loaddata --database other --format json -

# This works:
cat books.json | ./manage.py loaddata --database default --format json -

# Now, this works (because the data now exist in default):
cat books.json | ./manage.py loaddata --database other --format json -

```