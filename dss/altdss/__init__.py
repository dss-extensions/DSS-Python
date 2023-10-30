'''
This package exposes base objects for the pythonic Obj and Batch interfaces from DSS C-API.
These interfaces are unique to DSS-Extensions, they are not present in the official OpenDSS.

This is still under development and the final implementation might differ in some aspects.

One recent change, as planned, was to adjust the spelling of many properties; `nconds` became `NConds`, 
`kv` became `kV`, and so on. This is still open to suggestions, since we also considered forcing 
camelCase instead of PascalCase. There is no common naming convention in the OpenDSS properties
across different components and we could not reach a great solution yet changing only the capitalization. 
Note that a plain snake_case convention, forcing all lower-case characters, does not benefit us since it
obfuscates important information, besides deviating too much from the OpenDSS property names in the 
input data.

We also already removed `wdg` and the indirect properties in favour of the array versions.
This will also be tweaked after more usage. `NConds`, for example, may also be removed if we can
develop a mechanism to ensure the dimensions match.
'''

from .enums import *
from .Obj import *
from .common import Edit
from .AltDSS import IAltDSS
