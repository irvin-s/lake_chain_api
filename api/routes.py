from flask import Flask, request

app = Flask("Open Data Lake")

# App routes


@app.route("/", methods=["GET"])
def getUser():
    msg = "Hello World!"
    return(msg)

# User routes
@app.route("/newuser", methods=["GET"])
def newUser():
    msg = "Hello World!"
    return(msg)

# Node routes
@app.route("/newnode", methods=["GET"])
def newNode():
    msg = "Hello World!"
    return(msg)


if __name__ == "__main__":
    app.run()
