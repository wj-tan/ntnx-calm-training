import requests

IP_PC = "@@{ip_pc}@@"
USER_PC = "@@{pc_cred.username}@@"
PASS_PC = "@@{pc_cred.secret}@@"

NAME_VPC = "@@{vpc_name}@@"
UUID_UNDERLAY_SUBNET = "@@{underlay_uuid}@@"
NAME_UNDERLAY_SUBNET = "@@{underlay_name}@@"

def create_vpc(ip_pc, user_pc, pass_pc, name_vpc, uuid_external_subnet):
    url = "https://{}:9440/api/nutanix/v3/vpcs".format(ip_pc)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "spec": {
            "name": name_vpc,
            "resources": {
                "common_domain_name_server_ip_list":[],
                "external_subnet_list": [{
                    "external_subnet_reference": {
                        "kind": "subnet",
                        "uuid": uuid_external_subnet
                    }
                }]
            }
        },
        "metadata": {
            "kind": "vpc",
        },
        "api_version": "3.1.0"
    }

    response = requests.request("POST", url, auth=(user_pc, pass_pc), headers=headers, data=json.dumps(payload), verify=False)
    print(response.text)
    response = response.json()
    uuid_vpc = response["metadata"]["uuid"]

uuid_vpc = create_vpc(IP_PC, USER_PC, PASS_PC, NAME_VPC, UUID_UNDERLAY_SUBNET)

print "vpc_uuid={}".format(uuid_vpc)