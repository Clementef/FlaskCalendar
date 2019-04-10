import requests
from app.routes import app
from flask import render_template, session, redirect, request
from requests_oauth2.services import GoogleClient
from requests_oauth2 import OAuth2BearerToken
from .Classes import User

google_auth = GoogleClient(
    client_id=("488526633771-4jb5b2vsckq58it9nggon8n3v0lblr29"
                ".apps.googleusercontent.com"),
    client_secret="GwP7kmTDGcsJKfuyDup4oLB6",
    redirect_uri="http://localhost:5000/oauth2callback"
    # "http://localhost:5000/oauth2callback"
    # "https://computerinv-216303.appspot.com/oauth2callback"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    if not session.get("access_token"):
        return redirect("/oauth2callback")
    with requests.Session() as s:
        s.auth = OAuth2BearerToken(session["access_token"])
        r = s.get("https://www.googleapis.com/plus/v1/people/me?access_token={}".format(
            session.get("access_token")))
    r.raise_for_status()
    data = r.json()

    # Save Necessary variables
    session["displayName"] = data["displayName"]
    session["image"] = data["image"]["url"]

    user = User()

    # check if user exists
    for i in User.objects:
        if i.name == session["displayName"]:
            return redirect("/")

    #if not, create a new one
    user.name = data["displayName"]
    user.image = data["image"]["url"]
    user.save()

    return redirect("/")


@app.route("/oauth2callback")
def google_oauth2callback():
    code = request.args.get("code")
    error = request.args.get("error")
    if error:
        return "error :( {!r}".format(error)
    if not code:
        return redirect(google_auth.authorize_url(
            scope=["profile", "email"],
            response_type="code",
        ))
    data = google_auth.get_token(
        code=code,
        grant_type="authorization_code",
    )
    session["access_token"] = data.get("access_token")
    return redirect("/login")


@app.route("/logout")
def logout():
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']

    return redirect("/")
