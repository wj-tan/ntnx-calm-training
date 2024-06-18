# Credential and IP for making API Calls
IP_PC = "@@{ip_pc}@@"
USER_PC = "@@{pc_cred.username}@@"
PASS_PC = "@@{pc_cred.secret}@@"

# Network variables for creating subnet
UUID_VPC = "@@{vpc_uuid}@@"
OVERLAY_NAME = "@@{subnet_name}@@"
OVERLAY_PREFIX_LEN = "@@{prefix_length}@@"
OVERLAY_IP = "@@{ip_subnet}@@"
OVERLAY_GATEWAY = "@@{ip_gateway}@@"
OVERLAY_POOL = "@@{ip_pool_range}@@"

def define_ip_config(ip_prefix_length, ip_subnet, ip_gateway, ip_pool_range):
    return {
        "subnet_ip": ip_subnet,
        "prefix_length": int(ip_prefix_length),
        "default_gateway_ip": ip_gateway,
        "pool_list": [{
            "range": ip_pool_range
        }]
    }

def create_subnet(ip_pc, user_pc, pass_pc, vpc_uuid, subnet_name, ip_config):
    url = "https://{}:9440/api/nutanix/v3/subnets".format(ip_pc)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "spec": {
            "name": subnet_name,
            "resources": {
                "subnet_type": "OVERLAY"
                "vpc_reference": {
                    "kind": "vpc",
                    "uuid": vpc_uuid
                },
                "ip_config": ip_config
            }
        },
        "metadata": {
            "kind": "subnet"
        },
        "api_version": "3.1.0"
    }

    response = requests.request("POST", url, auth=(user_pc, pass_pc), headers=headers, data=json.dumps(payload), verify=False)
    print(response.text)
    
user_subnet_config = define_ip_config(OVERLAY_PREFIX_LEN, OVERLAY_IP, OVERLAY_GATEWAY, OVERLAY_POOL)
create_subnet(IP_PC, USER_PC, PASS_PC, UUID_VPC, OVERLAY_NAME, user_subnet_config)