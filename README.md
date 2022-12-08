<!--
title: 'AWS Python Example'
description: 'This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework.'
layout: Doc
framework: v3
platform: AWS
language: python
priority: 2
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->

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
# Serverless Framework AWS Python Example

This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework. The deployed function does not include any event definitions as well as any kind of persistence (database). For more advanced configurations check out the [examples repo](https://github.com/serverless/examples/) which includes integrations with SQS, DynamoDB or examples of functions that are triggered in `cron`-like manner. For details about configuration of specific `events`, please refer to our [documentation](https://www.serverless.com/framework/docs/providers/aws/events/).

## Usage

### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-project to stage dev (us-east-1)

✔ Service deployed to stack aws-python-project-dev (112s)

functions:
  hello: aws-python-project-dev-hello (1.5 kB)
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```bash
serverless invoke --function hello
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v3.0! Your function executed successfully!\", \"input\": {}}"
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v3.0! Your function executed successfully!\", \"input\": {}}"
}
```

### Bundling dependencies

In case you would like to include third-party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
