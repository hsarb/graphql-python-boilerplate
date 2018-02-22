## GraphQl Python Boilerplate

A [GraphQL](http://graphql.org/) and [Python](https://www.python.org/) boilerplate using [Graphene](http://graphene-python.org/), [Flask](http://flask.pocoo.org/), and [SQLAlchemy](https://www.sqlalchemy.org/)

## Getting started

Make sure you have [Python](https://www.python.org/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/index.html) before attempting the following steps.

1. Clone the repo

```
  $ git clone git@github.com:hsarb/graphql-python-boilerplate.git yourAppName
  $ cd yourAppName
```

2. Run setup

```
  $ mkvirtualenv --python=/usr/local/bin/python3 boilerplate
  $ workon boilerplate
  $ PYTHONPATH=. python setup.py install
```

3. Start the server

```
  $ python run.py
```
