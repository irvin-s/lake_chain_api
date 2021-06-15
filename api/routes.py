from flask import Flask, request

app = Flask("Open Data Lake")

#App routes

@app.route("/", methods=["GET"])
def getUser():
    msg = "Hello World!"
    return(msg)

if __name__ == "__main__":
    app.run()