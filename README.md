These commands will let you build and serve the mkdocs website locally for development

Create a python virtual environment and install the needed packages
```bash
# create a pythong virtual environment
python -m venv venv/

# activate it
source venv/bin/activate

# install the requirements into it
pip install -r requirements.txt
```

To build and serve locally:
```bash
mkdocs serve
```

To deploy on Github:

- Under the repository settings -> pages -> build and deployment -> source: `Deploy from Branch`, branch: `gh-pages` `/root` 


Refer to the documentation for more details:

- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)