import logging
import requests
import re
import logging
import json

def checkHttpResponse(httpCode):
    logger = logging
    logger.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    try:
        reg_200 = re.compile("20.")
        reg_300 = re.compile("30.")
        reg_400 = re.compile("40.")
        reg_500 = re.compile("50.")
	
        if bool(re.match(reg_200,httpCode)):
            logger.info(httpCode)
            logger.debug("HTTP ERROR CODE: "+httpCode)
            return True
        if bool(re.match(reg_300,httpCode)):
            logger.debug("HTTP ERROR CODE: "+httpCode)
            return False
        if bool(re.match(reg_400,httpCode)):
            logger.debug("HTTP ERROR CODE: "+httpCode)
            return False
        if bool(re.match(reg_500,httpCode)):
            logger.debug("HTTP ERROR CODE: "+httpCode)
            return False
        else:
            logger.debug("No valid HTTP code given")
            return False
    except Exception as e:
        logger.info("No valid HTTP code given")
        return False

class quay_client:
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.headers = {'content-type': 'application/json', 'Authorization': 'Bearer '+self.token}

    def organziation(self, name, state):
        def exists(name):
            r = requests.get(self.endpoint+"/organization/"+name,headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False
        def create(name):
            payload = {'name': name}
            r = requests.post(self.endpoint+"/organization/",data=json.dumps(payload),headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False        
        def delete(name):
            r = requests.delete(self.endpoint+"/organization/"+name,headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False
        
        if state == "present":
            if not exists(name):
                if create(name):
                    result = "Organization "+name+" created successfully"
                else:
                    result = "Failed to create organization "+name
            else:
                    result = "Organization "+name+" already exists"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "Organization "+name+"deleted sucessfully"
            else:
                result = "Can't delete organization"+name+" as it doesn't exist"
        else:
            result = "error - enable debug logging for more information"
        
        return result


    def robot(self,name, state, org):
        def exists(name):
            r = requests.get(self.endpoint+"/organization/"+org+"/robots?token=false&permissions=false",headers=self.headers)
            data = json.loads(r.text)
            robots = []

            if "robots" in data:
                for i in data["robots"]:
                    robots.append(i["name"])
            
                for robot in robots:
                    if robot == org+"+"+name:
                        robot_exists = True
                        break
                    else:
                        robot_exists = False
            else:
                robot_exists = False
            
            return robot_exists
            
        def create(name):
            r = requests.put(self.endpoint+"/organization/"+org+"/robots/"+name,headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False

        def delete(name):
            r = requests.delete(self.endpoint+"/organization/"+org+"/robots/"+name,headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False

        if state == "present":
            if not exists(name):
                if create(name):
                    result = "Robot "+name+" created successfully"
                else:
                    result = "Failed to create robot "+name
            else:
                    result = "Robot "+name+" already exists"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "Robot "+name+"deleted sucessfully"
            else:
                result = "Can't delete robot"+name+" as it doesn't exist"
        else:
            result = "error - enable debug logging for more information"
        
        return result

    def team(self,name, state, role, org, description):
        def exists(name):
            r = requests.get(self.endpoint+"/organization/"+org+"/team/"+name,headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False
        def create(name):
            payload = {"role": role,"description": description}
            r = requests.put(self.endpoint+"/organization/"+org+"/team/"+name,data=json.dumps(payload),headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False
        def delete(name):
            r = requests.delete(self.endpoint+"/organization/"+org+"/team/"+name,headers=self.headers)
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False

        if state == "present":
            if not exists(name):
                if create(name):
                    result = "created"
                else:
                    result = "failed"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
        else:
            result = "error"
        
        return result
    
    def team_member(self,name,team_name,state,org):
        def exists(name):
            memberFound = False
            r = requests.get(self.endpoint+"/organization/"+org+"/team/"+team_name+"/members",headers=self.headers)
            data = json.loads(r.text)
            if "members" in data:
                for member in data["members"]:
                    if member["name"] == name:
                        memberFound = True
                        break
            else:
                memberFound = False

            return memberFound
            
        def add(name):
            return True
        def delete(name):
            return True
        
        if state == "present":
            if not exists(name):
                if add(name):
                    result = "created"
                else:
                    result = "failed"
        elif state == "non-member":
            if exists(name):
                if delete(name):
                    result = "deleted"
        else:
            result = "error"
        
        return result

    def repository(self,name, state):
        def exists(name):
            return True
        def create(name):
            return True
        def delete(name):
            return True

        if state == "present":
            if exists(name):
                if create(name):
                    result = "created"
                else:
                    result = "failed"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
                else:
                    result = "failed"
        else:
            result = "error"
        
        return result

    def user(self,name, state, email):
        def exists(name):
            userExists = False
            r = requests.get(self.endpoint+"/superuser/users",headers=self.headers)
            
            if 'application/json' in r.headers.get('Content-Type'):
                data = json.loads(r.text)

                if "users" in data:
                    for i in data["users"]:
                        if i["username"] == name:
                            userExists = True
                            break
                else:
                    userExists = "failed"
            else:
                userExists = "Failed"
             
            return userExists

        def create(name,email):
            payload = {"username": name,"email": email}
            r = requests.post(self.endpoint+"/superuser/users",headers=self.headers,data=json.dumps(payload))
            if checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False

        def delete(name):
            return True

        if state == "present":
            if exists(name):
                if create(name,email):
                    result = "created"
                else:
                    result = "failed"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
                else:
                    result = "failed"
        else:
            result = "error"
        
        return result