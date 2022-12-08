

# Some important information

https://github.com/jpadilla/pyjwt/issues/800

cryptography==3.4.8

```
[ERROR] ImportError: /lib64/libc.so.6: version `GLIBC_2.28' not found (required by /var/task/cryptography/hazmat/bindings/_rust.abi3.so)
Traceback (most recent call last):
  File "/var/task/serverless_sdk/__init__.py", line 144, in wrapped_handler
    return user_handler(event, context)
  File "/var/task/s_jobsWorker.py", line 25, in error_handler
    raise e
  File "/var/task/s_jobsWorker.py", line 20, in <module>
    user_handler = serverless_sdk.get_user_handler('handler.consumer')
  File "/var/task/serverless_sdk/__init__.py", line 56, in get_user_handler
    user_module = import_module(user_module_name)
  File "/var/lang/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 843, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/var/task/handler.py", line 2, in <module>
    import snowflake.connector as sc
  File "/var/task/snowflake/connector/__init__.py", line 16, in <module>
    from .connection import SnowflakeConnection
  File "/var/task/snowflake/connector/connection.py", line 26, in <module>
    from .auth import Auth
  File "/var/task/snowflake/connector/auth.py", line 21, in <module>
    from cryptography.hazmat.primitives.serialization import (
  File "/var/task/cryptography/hazmat/primitives/serialization/__init__.py", line 16, in <module>
    from cryptography.hazmat.primitives.serialization.base import (
  File "/var/task/cryptography/hazmat/primitives/serialization/base.py", line 9, in <module>
    from cryptography.hazmat.primitives.asymmetric.types import (
  File "/var/task/cryptography/hazmat/primitives/asymmetric/types.py", line 7, in <module>
    from cryptography.hazmat.primitives.asymmetric import (
  File "/var/task/cryptography/hazmat/primitives/asymmetric/dsa.py", line 10, in <module>
    from cryptography.hazmat.primitives.asymmetric import (
  File "/var/task/cryptography/hazmat/primitives/asymmetric/utils.py", line 6, in <module>
    from cryptography.hazmat.bindings._rust import asn1  
```