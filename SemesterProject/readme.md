CMPT-120L-902-21S Semester Project

This website is written using HTML and Python run on a Flask simple server. Different themes are utalized using Jinja templates. 

To start the server, follow the following steps.

1) Download the server files
2) Within the Windows files, open PowerShell within the "SemesterProject" folder
3) Define the main flask folder: $env:FLASK_APP = "hello.py"
4) Activate the server using: python -m flask run
5) View the server at: http://127.0.0.1:5000/
6) Changing the different subpages within the main pages will allow access to the different pages of the server (e.g. /aboutme, /contact, /resume, /index)
7) Follow the PowerShell window for logging changes of webpage changing, user logging, and more

Personal Checklist of required features:
- Templates folder
- Rendering template function 
- Connected stylesheet
- Transition between multiple webpages
- Written readme for starting webpage
- Route all four different pages
- 404 Error Page
- Logging announcing visitor changing pages


Still Need to Do:
- URL Building
- Static vs. Dynamic Files
- 4 different views
- Add linkage between all pages from one another
- Add actual content on the different pages
- Install sonarlint in vscode
