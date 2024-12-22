Notes:
- All special methods are called _dunder methods_. `__getitem__`: dunder-getitem
- `collections.namedtuple`: Since Python 2.6, namedtuple can be used to build classes of objects that are just bundles of attributes with no custom methods, like a database record.
- You can use special methods to leverage the Python data model, like `__len__` and `__getitem__`, to give standard operations instead of having tp memorize arbitary method names "How to get the number of items? Is it `.size()`, `.length()`, or what?"
- For built-in types like list, str, bytearray, and so on, the interpreter takes a short‐ cut: the CPython implementation of len() actually returns the value of the ob_size field in the PyVarObject C struct that represents any variable-sized built-in object in memory. This is much faster than calling a method.
- 

---

Questions & to learn:
- implicit call vs. explicit
- composition
- encapsulation
- 
