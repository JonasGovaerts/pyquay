import logging
import requests
import re
import logging
import json

def checkHttpResponse(httpCode):
    try:
        reg_200 = re.compile("20.")
        reg_300 = re.compile("30.")
        reg_400 = re.compile("40.")
        reg_500 = re.compile("50.")
	
        if bool(re.match(reg_200,httpCode )):
            return True
        if bool(re.match(reg_300,httpCode )):
            return False
        if bool(re.match(reg_400,httpCode )):
            return False
        if bool(re.match(reg_500,httpCode )):
            return False
        else:
            return False
    except Exception as e:
        return False

class quay_client:
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.headers = {'content-type': 'application/json', 'Authorization': 'Bearer '+self.token}

    def organziation(self, name, state):
        def exists(name):
            r = requests.get(self.endpoint+"/organization/"+name,headers=self.headers)
            print(str(r.status_code))
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
                    result = "created"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
        else:
            result = "error"
        
        return result


    def robot(self,name, state, org):
        def exists(name):
            r = requests.get(self.endpoint+"/organization/"+org+"/robots?token=false&permissions=false",headers=self.headers)
            data = json.loads(r.text)
            robots = []

            for i in data["robots"]:
                robots.append(i["name"])
            
            for robot in robots:
                if robot == org+"+"+name:
                    robot_exists = True
                    break
            
            if robot_exists:
                return True
            else:
                return False
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
                    result = "created"
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
        else:
            result = "error"
        
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
        elif state == "absent":
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
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
        else:
            result = "error"
        
        return result

    def user(self,name, state):
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
        elif state == "absent":
            if exists(name):
                if delete(name):
                    result = "deleted"
        else:
            result = "error"
        
        return result