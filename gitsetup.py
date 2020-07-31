import os
from github import Github

'''Get your own access token from github
Refer this : https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
'''
access_token = "YOUR_ACCESS_TOKEN"
g = Github(access_token)
BASE_URL = "https://github.com/"


#To validate input 
while True:

    repo_name  =input("Repository name: ")
    if len(repo_name) <1:
        print("Repository name is required!")
        continue
    else:
        break

repo_desc  =input("Repository description: ")

#To validate input
while True:


    repo_private = input("Is Private (y/n) : ")
    repo_private = repo_private.lower()
    if repo_private not in ('y','n'):
        print("Enter only y or n")
        continue
    else:
        break

#To validate input
while True:
    repo_readme = input("Start with readme (y/n) : ")
    repo_readme = repo_readme.lower()
    if repo_readme not in ('y', 'n'):
        print("Enter only y or n")
        continue
    else:
        break


#Converting repo_private and repo_readme into bool
if repo_private== "y":
    repo_private = True
else:
    repo_private =False

if repo_readme == "y":
    repo_readme = True
else:
    repo_readme = False

#Creating a repository and returning a Repository object
a = g.get_user().create_repo(name=repo_name, description=repo_desc,private=repo_private,auto_init=repo_readme)


repo_path = BASE_URL+a.full_name+".git"  # https://github.com/<USERNAME>/<REPOSITORYNAME>.git
print("Cloning repo.....")
os.system(f"git clone {repo_path}")
print("SUCCESS! \nRepository ready to use!")
