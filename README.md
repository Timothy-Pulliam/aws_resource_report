## About

This script takes a search query as input, and generates a CSV file with the following information:

* Resource ARN
* Owning Account ID
* AWS Region
* Resource Type
* Service
* Tags

Amazon Resource Explorer must be enabled. It is a free service provided by Amazon.

To enable Resource Explorer
https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-setting-up.html

## Usage

| Description | Syntax |
| --- | ----------- |
| Get all resources | `./resource_report.py` |
| Get only resources that match the query string | `./resource_report.py queryString='myapp'`|
| List available resource types that can be queried | `./resource_report.py --list-resource-types`|

### Filters

| Description | Syntax |
| --- | ----------- |
| Get resources with a given ARN | `./resource_report.py queryString='id:$ARN` |
| Get resources by account ID |  `./resource_report.py queryString='accountid:$ACCOUNT_ID'` |
| Get resources by region  | `./resource_report.py queryString='region:us-east-1'`|
| Get resources by service | `./resource_report.py queryString='service:ec2'` |
| Get resource by resourcetype  | `./resource_report.py queryString='resourcetype:ec2:vpc'`  |
| Get untagged resources  | `./resource_report.py queryString='tag:none'`  |
| Only get resources that have tags (opposite of above)  | `./resource_report.py queryString='-tag:none'`|
| Combine multiple filters | `./resource_report.py queryString='-tag:none resourcetype:ec2:vpc'`  |

For information on query syntax, see the documentation
https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html

# Additional Resources

resource explorer must be turned on
https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html

resource explorer boto3 docs
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html

resource explorer aws cli docs
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/index.html
