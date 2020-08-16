I decided to use `poetry`. It [seems like](https://news.ycombinator.com/item?id=21510597) people are more excited about it right now.

```bash
# Install according to https://python-poetry.org/docs/#installation
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Enable it in my current bash session
source $HOME/.poetry/env

# Install autocompletion
poetry completions bash | sudo tee /etc/bash_completion.d/poetry.bash-completion
```

Note that the last statement uses `sudo tee` even though it's not mentioned in the Poetry [install docs](https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh). This is needed to modify files in `/etc/`, which is owned by `root`.

I create a new project with

```bash
poetry new nia
```

I also decided to use this opportunity to check out the latest Django, so I run:

```bash
poetry install django
```

Then in my `nia/pyproject.toml` file I change `django = "^3.0.1"` to `django = "~3.0"`, because the minor version is more like a major version in Django versioning, so this should keep the version in the 3.0.x range.