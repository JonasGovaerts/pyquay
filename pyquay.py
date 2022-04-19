import logging
import requests
import re
import logging
import json

class quay_client:
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        headers = {'Authorization': 'Bearer '+token}

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

    def organziation(self, name, state):
        def exists():
            r = requests.get(self.endpoint+"/organization/"+name,headers=self.headers)
            if self.checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False
        def create():
            payload = {'name': name}
            r = requests.post(self.endpoint+"/organization/",data=json.dumps(payload),headers=self.headers)
            if self.checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False        
        def delete():
            r = requests.delete(self.endpoint+"/organization/"+name,headers=self.headers)
            if self.checkHttpResponse(str(r.status_code)):
                return True
            else:
                return False
        
        if state == "present":
            if exists:
                if create:
                    result = "created"
        elif state == "absent":
            if exists:
                if delete:
                    result = "deleted"
        else:
            result = "error"
        
        return result


    def robot(self,name, state):
        def exists():
            return True
        def create():
            return True
        def delete():
            return True

        if state == "present":
            if exists:
                if create:
                    result = "created"
        elif state == "absent":
            if exists:
                if delete:
                    result = "deleted"
        else:
            result = "error"
        
        return result

    def team(self,name, state):
        def exists():
            return True
        def create():
            return True
        def delete():
            return True

        if state == "present":
            if exists:
                if create:
                    result = "created"
        elif state == "absent":
            if exists:
                if delete:
                    result = "deleted"
        else:
            result = "error"
        
        return result

    def repository(self,name, state):
        def exists():
            return True
        def create():
            return True
        def delete():
            return True

        if state == "present":
            if exists:
                if create:
                    result = "created"
        elif state == "absent":
            if exists:
                if delete:
                    result = "deleted"
        else:
            result = "error"
        
        return result

    def user(self,name, state):
        def exists():
            return True
        def create():
            return True
        def delete():
            return True

        if state == "present":
            if exists:
                if create:
                    result = "created"
        elif state == "absent":
            if exists:
                if delete:
                    result = "deleted"
        else:
            result = "error"
        
        return result