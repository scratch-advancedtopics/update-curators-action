from os import environ
from urllib import request
import json, sys

def get_members_with_status(status):
    out = []
    offset = 0
    limit = 24

    while True:
        req = request.urlopen(f"https://api.scratch.mit.edu/studios/30152868/{status}s?offset={offset}&limit={limit}").read()
        members = json.loads(req.decode("utf-8"))

        for member in members:
            print(f"Found {status} \033[96m{member['username']}\033[0m#\033[92m{member['id']}\033[0m - Request #: {int(((offset + limit) / limit))}")
            out.append(member)
        
        if len(members) == 0 or len(members) < 24:
            break

        offset += limit
    
    return out

def main():
    members = [
        get_members_with_status("manager"),
        get_members_with_status("curator")
    ]

    return members

workspace = environ.get("GITHUB_WORKSPACE")

if workspace == None:
    if len(sys.argv) < 1:
        workspace = sys.argv[1] + "/"
    else:
        workspace = ""
else:
    workspace += "/"



with open(f'{workspace}members.json', "w") as file:
    json.dump(main(), file)
