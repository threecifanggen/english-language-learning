# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '3GEE English'
copyright = '2022, 3GEE'
author = '3GEE'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    "myst_parser",
    "sphinxcontrib.mermaid",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'press'
html_static_path = ['_static']

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

source_suffix = {
    '.rst': 'restructuredtext',
    # '.txt': 'markdown',
    # '.md': 'markdown',
    '.myst.md': 'markdown',
}

footer_html = """\
<div class="container" id="footer-nav">
<div class="row">
<div class="col">
    <p style="text-align: center"><b>主站其他内容</b></p>
    <ul style="list-style-type: none; text-align: center; padding: 0;">
    <li><a href="https://blog.3gee.me/">我的博客<a></li>
    <li><a href="https://workwiki.3gee.me/">工作(DS/CS)百科<a></li>
    <li><a href="https://philosophia.3gee.me/">哲学百科<a></li>
    <li><a href="https://medicine.3gee.me/">医学百科<a></li>
    </ul>
</div>
<div class="col">
    <p style="text-align: center"><b>社交网络</b></p>
    <ul style="list-style-type: none; text-align: center; padding: 0;">
    <li><a href="https://www.zhihu.com/people/huang-bao-chen">知乎<a></li>
    <li><a href="https://stackoverflow.com/users/5387442/huang-baochen">StackOverflow<a></li>
    <li><a href="https://segmentfault.com/u/sancifanggen">SegmentFault<a></li>
    <li><a href="https://github.com/threecifanggen">GitHub<a></li>
    <ul>
</div>
<div class="col">
    <p style="text-align: center"><b>联系我</b></p>
    <ul style="list-style-type: none; text-align: center; padding: 0;">
    <li><a href="mailto:cube.root.huang+job@gmail.com">招聘<a></li>
    <li><a href="mailto:cube.root.huang+ask@gmail.com">社区求助(任何领域)<a></li>
    <ul>
</div>
</div></div>
"""