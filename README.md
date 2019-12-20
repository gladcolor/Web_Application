# Web_Application
For IS601

Part3

Website: [http://web-application-part3-huan.herokuapp.com/](http://web-application-part3-huan.herokuapp.com/)
![](screenshots/part3_1.png)

export port=5432


Run the following from your terminal to set system environment variables:

export FLASK_ENV=development

export DATABASE_URL=postgres://postgres:passwd@localhost:5432/mydb

export JWT_SECRET_KEY=hhgaghhgsdhdhdd


#Everytime to run:

```python

heroku ps:exec -a web-application-part3-huan

```

```
export port=5432

export FLASK_ENV=development

export JWT_SECRET_KEY=hhgaghhgsdhdhdd

export DATABASE_URL=postgres://sctmsvabejjcpn:eb40e4a07b0d79811a76fc3c3b14244a3e4a337f6c224023f2f8771629fd6210@ec2-174-129-254-249.compute-1.amazonaws.com:5432/d5cm77f30vr6qr

```