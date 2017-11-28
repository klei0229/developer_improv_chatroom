CSc 47300 Fall 2017 Project: Improv-Chatroom-master

Front-End: Html/CSS
Server: FLASK
Back-end: Python

To Run The App:
First: install flask, and flask-wtf (may need create a venv mode)
Second: python application.py

To Run the Test:
First: Install pytest
second: run py.test or pytest, either of them work!
(notes: someone may received error of version problem of flask that related to blinker.
Solution is install blinker by using pip)

Deploy Using Heroku:
https://limitless-island-91246.herokuapp.com/create

Warning: to add/change new style in external file, don't be worried about if the page
didn't make any change. You need to refresh the css file in website in order make it work in html,
if this still didn't work, you need to inspect element -> source -> find the css file -> fresh.
For exmaple, if you change/add something in chatroom.css. Refresh the page of 127.../static/css/chatroom.css
make sure the change/addition you made is in there, refresh the html page.
