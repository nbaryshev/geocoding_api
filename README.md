<b>This app is based on the Flask framework, SQLite database. Please, make sure you installed all relevant modelues you need to deal with such kind of applications(Flask, Flask-Uploads, etc.) and set up the SQLite database. It aslo uses ArcGis (```https://developers.arcgis.com/sign-up/```) to geocode locations basing on provided data.</b>

1. The app allows user to upload csv files which consist of: point(name of the place), latitude, longitude. You may find an example of such CSV file in the root folder ("```data_sample.csv```").
2. Before runnning an application, please create a ```static/files``` folders inside the app folder. All the files that you will upload will be automatically stored there.
3. You can run an application from terminal. For example, you can use PyCharm's terminal. To do so, please open the project in Pytcharm, open its terminal.
4. Make sure you are in the root folder. You can navigate inside between the folders using ```cd/ls``` comands.
5. Once you are ready to run an application, please type "flask run" in your oppened terminal.
6. You should see the message "``` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```".
7. Click an active link. The browes should be opened automatically and run the app.
8. In oder to upload the file, please press "Choose file", choose your CSV file and then click "```Upload```"
9. The  file will be save to the ```static/files``` directory and add the pass to the file to ```SQLlite database```.
10. The app will read this file, get the values of ```latitude``` and ```longitude``` and get the results from ```arcgis``` using the ```arcgis``` module. Make sure you installed this module (e.g. ```pip(3) install arcgis``` - in case of using pip(3))
9. The browser will be riderected to the page with results of your request and display the name of requested points and its adresses.

#TODO:
1. Calculate the destinations between the points basing on provided latitudes and longitudes
2. To make API accessable with wget/cURL for Linux machines
