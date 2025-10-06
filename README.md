redisbayes
=========

Forked from [jart/redisbayes](https://github.com/jart/redisbayes)

Table Of Contents
-----------------

- [redisbayes](#redisbayes)
  - [Table Of Contents](#table-of-contents)
  - [What Is This?](#what-is-this)
  - [What's New](#whats-new)
    - [Python Packaging Enhancements](#python-packaging-enhancements)
    - [Improved Logging](#improved-logging)
  - [Installation](#installation)
  - [Building \& Packaging](#building--packaging)
  - [Testing The Build](#testing-the-build)
  - [Basic Usage](#basic-usage)

What Is This?
-----------------

It's a Naïve Bayesian Text Classifier on Redis (aka spam filter.) I wrote this to filter spammy comments from a high traffic forum website and it worked pretty well.  It can work for you too :) It's not tied to any particular format like email, it just deals with the raw text.

This is probably the only spam filtering library you'll find for Python that's simple (170 lines of code), works (30 lines of test code), and doesn't suck.

What's New
-----------------

### Python Packaging Enhancements

- `pyproject.toml`: Earlier settings.py was being used to build the package from repo, now pyproject.toml will be used.

### Improved Logging

- Used python's logging module and updated old python 2 style strings to python 3 style f-strings

Installation
-----------------

From folder:

    sudo python setup.py install

From cheeseshop:

    sudo pip install redisbayes

From git:

    sudo pip install git+git://github.com/jart/redisbayes.git

Building & Packaging
-----------------

We use [PEP 517/518](https://peps.python.org/pep-0518/) with `pyproject.toml`.
All modern build tools work, but the recommended one is [`build`](https://pypi.org/project/build/).

    # Cleaning old builds
    rm -rf dist build *.egg-info

    # Installing build, setuptools, wheel
    python -m pip install --upgrade build setuptools wheel

    # Building wheel + source distribution
    python -m build

    # Checking the distribution contents
    ls dist/

Testing The Build
-----------------

Installing into a fresh virtual environment to verify:

    python -m venv .venv-test
    source .venv-test/bin/activate

    pip install dist/redisbayes-*.whl

    python -c "from importlib.metadata import version; print('Installed version:', version('redisbayes'))"

    deactivate

Basic Usage
-----------------

    import redis, redisbayes
    rb = redisbayes.RedisBayes(redis=redis.Redis())

    rb.train('good', 'sunshine God love sex lobster sloth')
    rb.train('bad', 'fear death horror government zombie')

    assert rb.classify('sloths are so cute i love them') == 'good'
    assert rb.classify('i am a zombie and love the government') == 'bad'

    print rb.score('i fear God and hate the government')

    rb.untrain('good', 'sunshine God love sex lobster sloth')
    rb.untrain('bad', 'fear death horror government zombie')
