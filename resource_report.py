#!/usr/bin/env python

import boto3
from botocore.exceptions import ClientError
import sys
import re
from pprint import pprint
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("queryString", nargs='?', metavar='queryString', help="only return search results matching query string. If this argument is not set, all resources will be returned.")
parser.add_argument('--list-resource-types', dest='list_resource_types', default=False, action='store_true', help="list available resource types that can be queried.")
args = parser.parse_args()

def extract_tags(resource):
    """Conver tags from format:
        [
            {'Key': 'Name', 'Value': 'CompanyA-igw'},
            {'Key': 'env', 'Value': 'prod'}
        ]
    to the following stringified flat format (for excel):
        Name=CompanyA-igw,env=prod
    """
    stringified_tags = ""
    for p in resource['Properties']:
        if 'Data' in p:
            tags = p['Data']
            for tag in tags:
                key, value = tag.values()
                stringified_tags += "{}={},".format(key, value)
            stringified_tags = stringified_tags[:-1]
    return stringified_tags

try:
    client = boto3.client('resource-explorer-2')
except ClientError as e:
    print("Client Error: {}".format(e))
    exit(1)

if args.list_resource_types:
    print("Listing resource types that can be queried by resource explorer")
    pprint(client.list_supported_resource_types())
    exit(1)

# get search query
try:
    queryString = args.queryString.split('=')[1]
except IndexError as e:
    print("usage: ./resource_report.py queryString=\'resourcetype:ec2:instance\'")
    exit(1)

pages = []
nextPageToken = None
response = client.search(QueryString=queryString, MaxResults=20)
pages.append(response)
while True:
    if 'NextToken' in response.keys():
        nextPageToken = response['NextToken']
        response = client.search(QueryString=queryString, NextToken=nextPageToken, MaxResults=20)
        if response['Resources']:
            pages.append(response)
    else:
        break

# print(len(pages))
# pprint(pages)

resource_dfs = []
for page in pages:
    for resource in page['Resources']:
        tags = extract_tags(resource)
        df = pd.DataFrame({k:[v] for k,v in resource.items()})
        df['Tags'] = tags
        resource_dfs.append(df)
    if 'NextToken' in response:
        nextPageToken = response['NextToken']

if len(resource_dfs) > 0:
    df = pd.concat(resource_dfs)
    print(df)
    df.to_csv("./resource_report.csv")
    print("\nfound {} resources\n".format(df.shape[0]))
else:
    print("found {} resources\n".format(response['Count']['TotalResources']))
    print("no results found matching the query string\n")

