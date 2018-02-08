from bottle import route, run, template, static_file, error
import json, os

with open('bekkur.json', 'r', encoding='utf-8') as f:
    bekkur = json.load(f)

@route('/')
def index():
    return template('index', bekkur=bekkur)

@route("/nemandi/<id>")
def nemandi(id):
    return template('nemandi', kt=id, bekkur=bekkur)

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root='./css')

@error(404)
def error404(error):
    return "<h1>Þessi síða fannst ekki</h1>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
