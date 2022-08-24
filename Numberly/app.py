from flask import Flask , render_template ,request,redirect
import requests , json

app = Flask(__name__)
  
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/response",methods=["POST"])
def response():
        category = request.form.get("category")
        number = request.form.get("number", type=int)
        if not number or isinstance(number, int) == False or category == "Category":
            print("Error , You  have to choose a category and must enter a number")
            print(category , number)
            return redirect("/") 
    
        url = "https://numbersapi.p.rapidapi.com/"+str(number)+"/"+str(category)
        
        if category == "math" or "year":
            querystring = {"fragment":"true","json":"true"}

        if category == "trivia":
            querystring = {"fragment":"true","notfound":"floor","json":"true"}

        if category == "random":
            url = "https://numbersapi.p.rapidapi.com/random/trivia"
            querystring = {"min":"10","max":"20","fragment":"true","json":"true"}

        headers = {
	"X-RapidAPI-Key": "34e978368amsh047a1f6690b415cp190ec7jsnf30c999da0b6",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}
        response = requests.request("GET", url, headers=headers, params=querystring)
        text = json.loads(response.text)
        print("text : "+ text["text"])
        print(category , number)
        return render_template("response.html",text=text, number= number , category=category)
