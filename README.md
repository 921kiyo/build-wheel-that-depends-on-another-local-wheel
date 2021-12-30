# Python packaging edge cases

This is a code example to demonstrate an edge case written in [my blog post](https://921kiyo.com/python-packaging-edge-cases/).

>> TL;DR: You cannot package a Python module that depends on local wheel dependencies.

First, make sure you are using the latest `setuptools`
```bash
pip install setuptools -U
```

Build a package using direct references as follows:

```bash
cd build-wheel-that-depends-on-another-local-wheel
python setup.py sdist bdist_wheel
```

Now try to build it using the relative path, which should give you an error

```bash
cd build-wheel-that-depends-on-another-local-wheel
python setup_modified.py sdist bdist_wheel
```
