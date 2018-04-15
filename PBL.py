from flask import *
from pymongo import MongoClient

'''Flask '''
app = Flask(__name__)

'''Mongo DB Connection'''

client = MongoClient('mongodb://main:rcb#123@ds257627.mlab.com:57627/pbl_farming')
db = client.pbl_farming

'''Farmer Registeration : pushing data to mlab mongo database'''
@app.route('/', methods=["GET","POST"])
def farmer_registration():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        survey_no=request.form["survey_no"].upper()
        farmer_name=request.form["name"].upper()
        farmer_age=request.form["age"].upper()
        farmer_phno=request.form["phone"].upper()
        agri_area=request.form["area"].upper()
        agri_soil=request.form["soil_type"].upper()
        agri_irrigation=request.form["irrigation_type"].upper()
        agri_ccrop=request.form["current_crop"].upper()
        agri_prev_crop=request.form["prev_crop"].upper()
        agri_cattles=request.form["cattle"].upper()

        #spliting the agri_prev_crop with , as del
        agri_pcrop=agri_prev_crop.split(",")
        print(agri_pcrop)
        print(".........................................................")
        print(survey_no+farmer_age+farmer_name+farmer_phno+agri_area+agri_soil+agri_irrigation+agri_ccrop+agri_prev_crop+agri_cattles)
        print(".........................................................")

        #adding to db
        farmer_details=db.farmer_details

        #create the document for collection
        farmer_details_data={
            "surveyno":survey_no,
            "name":farmer_name,
            "age":farmer_age,
            "phone_no":farmer_phno,
            "area":agri_area,
            "soil_type":agri_soil,
            "irrigation":agri_irrigation,
            "ccrop":agri_ccrop,
            "pcrop":agri_pcrop,
            "no_of_cattles":agri_cattles
        }
        obj_id=farmer_details.insert_one(farmer_details_data).inserted_id;
        print(obj_id)
        return render_template("index.html")
if __name__ == '__main__':
    app.run()