from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/", methods=["GET"])
def index():
    return "Webhook aktif dan siap menerima POST dari Dialogflow!"

@app.route("/", methods=["POST"])
def webhook():
    req = request.get_json()
    user_query = req.get("queryResult", {}).get("queryText", "")

    # Normalisasi simbol matematika agar sesuai dengan Python
    user_query = user_query.replace("×", "").replace("x", "")  # untuk perkalian
    user_query = user_query.replace("÷", "/").replace(":", "/")  # untuk pembagian

    try:
        result = eval(user_query)
        response_text = f"Hasilnya adalah {round(result, 2)}"
    except ZeroDivisionError:
        response_text = "Maaf, tidak bisa membagi dengan nol."
    except:
        response_text = "Maaf, saya tidak bisa menghitung soal itu."

    return jsonify({"fulfillmentText": response_text})

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=3000)
