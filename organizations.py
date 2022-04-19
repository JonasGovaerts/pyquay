import logging
import yaml
import pyquay
import logging

def main():
    endpoint="https://quay-enterprise.cluster.mgt.int.corp/api/v1"
    token="30m7Z7pfsKhicWj8ccGFtWmp5twigLdVsT8Sc0X5"
    config="./config.yml"
    organizations = []
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

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
        #result = quay.organziation(name=organization_name,state=organization_state)
        #logger.info("Organization "+organization_name+ " "+result)

        #Create robotaccounts
        #for robot in data["robots"]:
        #    robot_name = robot["name"]
        #    robot_state = robot["state"]
        #    result = quay.robot(name=robot_name, state=robot_state, org=organization_name)
        #    logger.info("Robot "+robot_name+" "+result)

        #Create teams
        for team in data["teams"]:
            team_name = team["name"]
            team_state = team["state"]
            role =  team["role"]
            result = quay.team(name=team_name, state=team_state, role=role, org=organization_name, description="")
            logger.info("Team "+team_name+" "+result)

        #Create user
        user_name = data["user"]["name"]
        user_state = data["user"]["state"]
        result = quay.user(name=user_name, state=user_state)
        logger.info("User "+user_name+" "+result)

if __name__ == "__main__":
    main()