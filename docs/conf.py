# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html

from nbsite.shared_conf import *


master_doc = "index"
project = "MWE docs"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
nitpicky = True


extensions += [
    "sphinx_copybutton",
    "nbsite.analytics",
]
