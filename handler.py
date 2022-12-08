import json
import snowflake.connector as sc
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import os


def consumer(event, context):

    print(f"Snowflake version -->{sc.__version__} , {os.getenv('USER_NAME')}")
    ctx = sc.connect(
                user=os.getenv('USER_NAME'),
                password=os.getenv('PASSWORD'),
                account=os.getenv('ACCOUNT_IDENTIFIER'),
                region=os.getenv('REGION')
            )

    cs = ctx.cursor()
    try:
        cs.execute(f"use database FIVETRAN_DATABASE_DEV;")
        one_row = cs.fetchone()
        print(one_row[0])
    except Exception as ex:
        print(ex)    

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}
