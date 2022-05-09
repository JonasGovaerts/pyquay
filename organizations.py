#!/bin/python3.10

import logging
import yaml
import pyquay
import logging

def main():
    #endpoint="https://quay-enterprise.cluster.mgt.int.corp/api/v1"
    endpoint="https://quay.io/api/v1"
    token="30m7Z7pfsKhicWj8ccGFtWmp5twigLdVsT8Sc0X5"
    config="./config.yml"
    organizations = []
    
    logger = logging
    logger.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    quay = pyquay.quay_client(endpoint,token)
    
    with open(config, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile) # Open config.yaml file where organizations with their state and user are defined

    for section in cfg:
        organizations.append(section) # Create a dict from the loaded config.yaml file

    for organization in organizations:
        data = cfg[organization]
        organization_name = data["organization"]["name"]
        organization_state = data["organization"]["state"]
        
        #Create organization
        result = quay.organziation(name=organization_name,state=organization_state)
        logger.info(result)

        #Create robotaccounts
        for robot in data["robots"]:
            robot_name = robot["name"]
            robot_state = robot["state"]
            result = quay.robot(name=robot_name, state=robot_state, org=organization_name)
            logger.info(result)

        #Create teams
        for team in data["teams"]:
            team_name = team["name"]
            team_state = team["state"]
            role =  team["role"]
            result = quay.team(name=team_name, state=team_state, role=role, org=organization_name, description="")
            logger.info("Team "+team_name+" in organization "+organization_name+" "+result)

            ## add members to team
            for member in team["members"]:
                name = member["name"]
                state = member["state"]
                result = quay.team_member(name=name, team_name=team_name, state=state, org=organization_name)
                logger.info(result)

        #Create user
        user_name = data["user"]["name"]
        user_state = data["user"]["state"]
        user_email = data["user"]["email"]
        #logger.info("User "+user_name+" "+result)

if __name__ == "__main__":
    main()