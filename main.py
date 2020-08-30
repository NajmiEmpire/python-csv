import requests
import csv
import logging
from getpass import getpass
import sys

logging.basicConfig(level = logging.DEBUG)

username = input('*Enter your username : \t')
password = getpass()

orgName = input("*Enter your organization name : \t")
repoName = input("Enter your repository name : \t")

while orgName == '':
	orgName = input('Enter the org name : \t')

if repoName:
	url = "https://api.github.com/orgs/{}/repos/{}".format(orgName, repoName)


url = "https://apsi.github.com/orgs/{}/repos".format(orgName)
headers = {'Accept':'application/vnd.github.v3+json','Content-Type':'application/json' }

r = requests.get(url, headers = headers, auth=(username,password))


status =  r.status_code

if status == 200:
	repos = r.json()
	f = open('data.csv', 'w', newline='')
	csv_writer = csv.writer(f)
	csv_writer.writerow(['id', 'name', 'url', 'language', 'owner', 'created_at'])

	for item in repos:
		csv_writer.writerow([item['id'], item['name'], item['url'], item['language'], item['owner']['login'], item['created_at']])
	f.close()
	logging.debug('Process finished successufly !')
else:
	logging.error(r.text)
sys.exit()
