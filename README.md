## About

In order to use this script, you must enable Amazon Resource Explorer. It is a free service provided by Amazon.

Amazon Web Services Resource Explorer is a resource search and discovery service. By using Resource Explorer, you can explore your resources using an internet search engine-like experience. Examples of resources include Amazon Relational Database Service (Amazon RDS) instances, Amazon Simple Storage Service (Amazon S3) buckets, or Amazon DynamoDB tables. You can search for your resources using resource metadata like names, tags, and IDs. Resource Explorer can search across all of the Amazon Web Services Regions in your account in which you turn the service on, to simplify your cross-Region workloads.

For more information, see the documentation
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
