# Enumerations

The enumeration classes from DSS-Python-Backend are reexported as `dss.enums`, and the enums are also imported to the main module `dss` (so you can use `from dss import SolveModes`, for example). Many functions allow using these for better code quality, and some are required to correctly use the extended API. Note that AltDSS-Python includes a lot more enumerations derived from the internal DSS schema.

```{include} ../../dss-extensions/docs/python/enums.md
```
