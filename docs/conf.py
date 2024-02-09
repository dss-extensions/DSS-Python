import os, sys, shutil

if not os.path.exists('../../dss-extensions'):
    raise RuntimeError('dss-extensions common repo not found. Be sure to clone it side-by-side with OpenDSSDirect.py when building docs.')

if not os.path.exists('../../dss_python_backend'):
    raise RuntimeError('dss_python_backend common repo not found. Be sure to clone it side-by-side with OpenDSSDirect.py when building docs.')

sys.path.append('../../dss-extensions/docs')
from common_conf import *
import dss

project = 'DSS-Python'
copyright = '2018-2024 Paulo Meira, Dheepak Krishnamurthy, DSS-Extensions contributors'
author = 'Paulo Meira, Dheepak Krishnamurthy, DSS-Extensions contributors'
version = dss.__version__
release = dss.__version__

# extensions = [
#     'sphinx.ext.autodoc',
# #    'sphinx.ext.viewcode',
#     'sphinx.ext.githubpages',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.autosectionlabel',
#     'sphinx_autodoc_typehints',
#     'guzzle_sphinx_theme',
#     'nbsphinx',
#     'myst_parser',
# ]

# If we ever need more extensions or change settings, we are free to change it here. e.g.
extensions.append('autodoc2')

autodoc2_packages = [
    {
        "path": "../dss",
        "auto_mode": True,
    },
    {
        "path": "../../dss_python_backend/dss_python_backend",
        "auto_mode": False,
    },
]

autodoc2_docstrings = 'all'
autodoc2_sort_names = True
autodoc2_class_docstring = 'both'
autodoc2_hidden_regexes = [
    r'.*\.__setattr__$',
    r'.*\.__slots__$',
    r'.*\.__all__$',
    r'dss\.UserModels',
]

html_logo = '_static/dss-python.svg'
html_theme_options["logo"] = {
    "image_dark": '_static/dss-python-dark.svg',
}
html_theme_options["show_toc_level"] = 1
html_favicon = '_static/dssx.png'

# autosummary_generate = True

exclude_patterns.append('**electricdss-tst')

source_suffix = ['.md', '.rst', ]

# def try_cleaning(app, docname, source):
#     if os.path.exists('examples/electricdss-tst'):
#         shutil.rmtree('examples/electricdss-tst')

# def setup(app):
#     app.connect('source-read', try_cleaning)


# Ugly patches...

# This one is to make it run at all
patch_autodoc2()

# # This one is related to node_ids being too long with duplicated data
# # 
# import sphinx.domains.python
# add_target_and_index_org = sphinx.domains.python.PyObject.add_target_and_index 
# class PatchPyObject:
#     def add_target_and_index(self, name_cls, sig, signode):
#         if name_cls[0].count('.') > 2:
#             mod_name = self.options.get('module', self.env.ref_context.get('py:module'))
#             assert mod_name == name_cls[0][:len(mod_name)]
#             name_cls = (name_cls[0][1 + len(mod_name):], name_cls[1])
#             parts = name_cls[0].split('.')
#             if len(parts) > 1 and parts[0] == parts[1]:
#                 name_cls = ('.'.join(parts[1:]), name_cls[1])

#         return add_target_and_index_org(self, name_cls, sig, signode)

# sphinx.domains.python.PyObject.add_target_and_index = PatchPyObject.add_target_and_index