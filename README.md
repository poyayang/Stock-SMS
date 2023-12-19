# stock_tickers
Automation for stock tickers
The project is to create an automation for users get to know latest stock prices.

In this project, Render is the Python Host to deploy the project automation.

## Preparation
1.	Make sure that Flask is imported to the main file
`from flask import Flask, request`
`app=Flask(__name__)`

2.	Install requirement.txt, and save it in the same folder, 
`pip3 install -r requirements.txt`
NOTE. Render may not support some of the latest versions of libraries, this will have to refer to the instruction in the building process.

## Connect Github to Render

1.	Register on Render and click `New+` to create a Web Service
2.	Choose “Build and deploy from a Git repository”, to connect Github to Render
3.	Select the repository, make sure the repository is set as `Public` on Github
4.	Go to Render – Settings, fill in the information 
Repository – The URL of the repository on Github
Branch – The project is in the `Main` Branch
Build Command - `pip install -r requirements.txt`
Start Command - python app.py (the main file of the project)
5.	Hit `Create Web Service`


https://github.com/poyayang/stock_tickers/assets/136909810/d70559e1-3db6-4b1a-a204-fe56dbb7af1f




