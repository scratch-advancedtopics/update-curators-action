import urllib.request
import json
import os

def get_users(status):
	offset = 0
	out = []
	while True:
		contents = urllib.request.urlopen(f"https://api.scratch.mit.edu/studios/30152868/{status}?offset={offset}").read()
		contents = contents.decode('utf-8')
		if contents == '[]':
			break
		out.append(contents)
		offset += 20
	return out

def main():
	out = []
	for i in get_users('curators'):
		i = json.loads(i)
		out.append(i)
	for i in get_users('managers'):
		i = json.loads(i)
		out.append(i)
	return out


with open(f'{os.environ.GITHUB_WORKSPACE}/members.json','w') as f:
	json.dump(main(), f)