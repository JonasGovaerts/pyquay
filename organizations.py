import logging
import yaml
import pyquay
import logging

def main():
    endpoint="https://quay-enterprise.cluster.mgt.int.corp"
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
        name = data["organization"]["name"]
        state = data["organization"]["state"]
        
        #Create organization
        result = quay.organziation(name=name,state=state)
        logger.info("Organization "+name+ " "+result)

        #Create robotaccounts
        for robot in data["robots"]:
            name = robot["name"]
            state = robot["state"]
            result = quay.robot(name=name, state=state)
            logger.info("Robot "+name+" "+result)

        #Create teams
        for team in data["teams"]:
            name = team["name"]
            state = team["state"]
            result = quay.team(name=name, state=state)
            logger.info("Team "+name+" "+result)

        #Create user
        name = data["user"]["name"]
        state = data["user"]["state"]
        result = quay.user(name=name, state=state)
        logger.info("User "+name+" "+result)

if __name__ == "__main__":
    main()