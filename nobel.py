from flask import Flask, json, render_template, request, redirect, url_for
import os
#create instance of Flask app
app = Flask(__name__)
#decorator 
@app.route("/")
def echo_hello():
    return "<p>Hello Nobel Prize Homepage - latest !</p>"
@app.route("/all")
def all():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    #render_template is always looking in templates folder
    #return render_template('user_nobel.html',data=data_json)
    return json.jsonify({"Nobel Prizes Data":data_json})
@app.route("/<year>", methods = ["GET","POST"])
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']
    if request.method == "GET":
        output_data = [x for x in data if x['year']==year]
    #render_template is always looking in templates folder
        return render_template('user_nobel.html',data=output_data)
        #return json.jsonify({"Nobel Prizes Data by year":output_data})
    elif request.method == "POST":
        category = request.form['category']
        id = request.form['id']
        firstname = request.form['firstname']
        surname = request.form['surname']
        motivation = request.form['motivation']
        share = request.form['share']
        create_row_data= {'year': year, 'category': category, 'laurates': [{'id': id, 'firstname': firstname, 'surname': surname, 'motivation': motivation, 'share': share }]}
        print (create_row_data)
        filename='./static/nobel.json'
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data['prizes'].append(create_row_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        return render_template('user_nobel.html',data=create_row_data)
if __name__ == "__main__":
    app.run(debug=True)
