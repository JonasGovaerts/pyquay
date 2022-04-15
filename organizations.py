import yaml
import pyquay

def main():
    endpoint="https://quay-enterprise.cluster.mgt.int.corp"
    token="30m7Z7pfsKhicWj8ccGFtWmp5twigLdVsT8Sc0X5"
    config="./config.yaml"
    
    with open(config) as f:
        data = yaml.safe_load(f)
    
    quay = pyquay.quay_client(endpoint,token)

    for block in data:
        name = block[0]
        state = block[1]
        organization = quay.organziation(name=name,state=state)
        print(organization)


if __name__ == "__main__":
    main()