# Building the Docs

To build and edit the docs, first make sure you've installed Sphinx and the PyData Sphinx theme:

```
pip install sphinx
pip install pydata-sphinx-theme
```

Next, from this directory, run `make.bat` as follows:

```
make html
```

This will generate a directory `build/` containing the documentation. Open `build/html/index.html` in a browser to take a look at the results.