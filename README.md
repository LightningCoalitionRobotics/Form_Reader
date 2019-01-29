# Form_Reader

For the time being, the only person that will be using this repository is me, but in the future other people will need to use this project.

This project will make it MUCH easier to do the notebook. Only one person should need to run this at a time, because the rest of the team can fill out the  google form. In this case, if you would like to run this, you will need
to follow these steps:

	Go to the Google APIs Console.

	Create a new project.

	Click Enable API. Search for and enable the Google Drive API.
	
	Create credentials for a Web Server to access Application Data.

	Name the service account and grant it a Project Role of Editor.

	Download the JSON file.

	Copy the JSON file to your code directory and rename it to creds.json


Required Modules:
Gspread (https://github.com/burnash/gspread)

PyLatex (https://jeltef.github.io/PyLaTeX/current/index.html)

Json (https://www.json.org/)

OpenSSL (https://www.openssl.org/)
