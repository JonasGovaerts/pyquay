# Summary
This git repository contains a python module, pyquay, which allows you to interact with your private instance of Quay trough API.
It has most of the functionallity available which can be discovered via swaggerUI on https://quay-address/api/v1/discovery

## Functions
Following functions are available for use:
- organization
- robot
- team
- team_member
- user
- repository

## Examples
### Creating an organization
```Python
quay = pyquay.quay_client(endpoint,token)
result = quay.organziation(name=organization_name,state=organization_state)
```