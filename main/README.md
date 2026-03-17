###Hands-On– Lab-03 Dockerfile Dinner Suggestion

#Run the app without dockerfile

py.exe app.py
http://127.0.0.1:5000/

#Run the app with dockerfile

docker build -t dinner_flask_svc_app .
docker images
docker run -d -p 5099:5000 dinner_flask_svc_app
http://localhost:5099/
