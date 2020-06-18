# -*- coding: utf-8 -*-


# -- Path setup --
import sys
sys.path.append(r"/home/runner/manim_document_zh/manim")
print(sys.path)


# -- Project information --
project = 'manim'
copyright = '- This document has been placed in the public domain.'
# Sphinx写的manim文档编辑者名单,每经过一波大更新，新修正的PR者直接注释掉上一个作者,如果变动比较大，简要声明改动新增内容告知用户即可。
# author = '2019EulerTour'
# author = '2019elteoremadebeethoven'
author = '鹤翔万里 & Tridu33'  # 这个整合版本借鉴了很多已有的网友/群友资料，具体链接文中都已经标识引用。


version = '0.2.5'
release = 'v0.2' #我想把这里标识为文档

# -- General configuration --

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# 后三个是为了ext.autodoc
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.imgmath',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = None
language = 'zh_CN'

# 中文搜索 Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
html_search_language = 'zh'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output --
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = ['assets']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}



html_theme = 'sphinx_rtd_theme'  # 需要pip install sphinx_rtd_theme
html_favicon = 'mk.png'
html_logo = 'assets/image/Logo_black.png'
html_theme_options = {
    'logo_only': True,
}
# html_theme = 'traditional'
# html_theme = 'alabaster'
# https://documentation.help/Sphinx/theming.html
# https://sphinx-themes.org


# -- autoclass --
autoclass_content = 'both'
