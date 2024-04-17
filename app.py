from flask import Flask,jsonify,request,abort

app = Flask(__name__)

countries = [
    {"name": "United States", "population": 331000000},
    {"name": "China", "population": 1444000000},
    {"name": "India", "population": 1380000000},
    {"name": "Brazil", "population": 212000000},
    # Add more countries here
]
@app.get('/')
def get_countries():
    return jsonify(countries)
@app.get('/countries/<name>')
def get_country(name):
    country = next((c for c in countries if c['name'].lower() == name.lower()), None)
    if country:return jsonify(country)
    return [jsonify("something went wrong-", name), 403]
@app.post('/country')
def add_country():
    if not request.json or 'name' not in request.json or 'population' not in request.json:
        ("Invalid request format. 'name' and 'population' fields are required.",
        abort(403,))
    #prepare the data to be store
    data = request.json
    countries.append(data)
    return jsonify(countries),200
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5500,threaded=True,use_reloader=True)