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
result = quay.organziation(name=name,state=state) # state = "present" or state = "absent"
```
### Creating a robot account inside an organization
```Python
quay = pyquay.quay_client(endpoint,token)
result = quay.robot(name=name, state=tate, org=organization_name) # state = "present" or state = "absent"
```

### Creating a team inside an organization
```Python
quay = pyquay.quay_client(endpoint,token)
result = quay.team(name=name, state=state, role=role, org=organization_name, description=description) # state = "present" or state = "absent" : role = "member"  or role = "creator" or role = "admin"
```

### Creating a user
```Python
quay = pyquay.quay_client(endpoint,token)
result = quay.user(name=user, state=state, email=email) # state = "present" or state = "absent"
```


