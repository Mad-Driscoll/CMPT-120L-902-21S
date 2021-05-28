# CMPT-120L-902-21S Semester Project

For this final semester project features a web page featuring myself, Madelyn Driscoll. This is setup on a series of pages, written using HTML and [Python](https://www.python.org/) hosted on a [Flask Web Server](https://flask.palletsprojects.com/en/2.0.x/). Featured information includes who I am, contact information, and photos I have taken in an example of my learned coding experience within this course.

To start the server, view the following steps:

1. Download the server files
2. Within the Windows files, open PowerShell within the "SemesterProject" folder
3. Define the main flask folder: $env:FLASK_APP = "hello.py"
4. Activate the server using: python -m flask run
5. View the server at: http://127.0.0.1:5000/ or http://localhost:5000/
6. Click the link to access the main website/HTML files
7. View the PowerShell window for logging changes of user changing between webpages

Website Features:
- 4 different webpages with static HTML content
- Connected stylesheet (Bootstrap) for page content
- Rendering template function for various HTML pages in templates folder
- Ability to navigate between all pages with navigation bar
- 404 Page Error if user is routed incorrectly
- Flask user logging
- Readme with startup instructions
