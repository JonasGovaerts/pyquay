import logging
#import requests
import re
import logging

class quay_client:
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        headers = {'Authorization': 'Bearer '+token}

    def checkHttpResponse(httpCode,org):
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
        def exists(self):
            return True
        def create(self):
            return True        
        def delete(self):
            return True
        
        if state == "present":
            if not exists:
                create
                return "organzition exists"
        elif state == "absent":
            if exists:
                delete
                return "organization deleted"
        else:
            logging.raiseExceptions("No valid state provided")


    def repository(self, name):
        def exists(self):
            print("Repository "+name+" exists")
        def create(self):
            print("Created repository "+name)
        def delete(self):
            print("Deleted repository "+name)
        def changeMirror(self):
            print("Changed repository "+name+" to mirror")