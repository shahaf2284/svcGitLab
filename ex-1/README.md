### Hands-On– Lab-03 Dockerfile Dinner Suggestion

#Run the app without dockerfile

py.exe app.py
http://127.0.0.1:5000/

# Run the app with dockerfile

docker build -t dinner_flask_svc_app . <br>
docker images <br>
docker run -d -p 5099:5000 dinner_flask_svc_app <br>
http://localhost:5099/ <br>
