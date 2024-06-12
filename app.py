# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# # Create flask app
# flask_app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods = ["GET","POST"])
# def predict():
#     render_template("submit.html")
#     age = request.form['Age']
#     print(age)
#     sex = request.form['Sex']
#     if sex == 'Male':
#         sex = 1
#     if sex == 'Female':
#         sex = 0
#     bp = request.form['BP']
#     if bp == 'Low':
#         bp = 0
#     if bp == 'Normal':
#         bp = 1
#     if bp == 'High':
#         bp = 2
#     chol = request.form['Cholesterol']
#     if chol == 'Normal':
#         chol = 0
#     if chol == 'High':
#         chol = 1
#     na = float(request.form['Na_to_K'])
#     t = [[int(age), int(sex), int(bp), int(chol), float(na)]]
#     print(t)
#     pred = model.predict(t)
#     print(pred)
#     return render_template("submit.html", prediction_text = "{}".format(pred))

# if __name__ == "__main__":
#     flask_app.run(debug=True)




# from flask import Flask, request, render_template
# import pickle

# app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))  # Load the trained model

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         try:
#             age = int(request.form["Age"])
#             sex = request.form["Sex"]
#             if sex == "Male":
#                 sex = 1
#             else:
#                 sex = 0
#             bp = request.form["BP"]
#             if bp == "Low":
#                 bp = 0
#             elif bp == "Normal":
#                 bp = 1
#             else:
#                 bp = 2
#             cholesterol = request.form["Cholesterol"]
#             if cholesterol == "Normal":
#                 cholesterol = 0
#             else:
#                 cholesterol = 1
#             na_to_k = float(request.form["Na_to_K"])
#             t = [[age, sex, bp, cholesterol, na_to_k]]
#             pred = model.predict(t)
#             prediction_text = "The predicted drug is {}".format(pred[0])
#             return render_template("submit.html", prediction_text=prediction_text)
#         except Exception as e:
#             error_message = "Error: {}".format(str(e))
#             return render_template("submit.html", error_message=error_message)
#     else:
#         return render_template("submit.html")

# if __name__ == "__main__":
#     app.run(debug=True)








# app.py

# import numpy as np
# from flask import Flask, request, render_template
# import pickle

# # Create flask app
# flask_app = Flask(__name__)

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         try:
#             age = int(request.form["Age"])
#             sex = request.form["Sex"]
#             if sex == "Male":
#                 sex = 1
#             else:
#                 sex = 0
#             bp = request.form["BP"]
#             if bp == "Low":
#                 bp = 0
#             elif bp == "Normal":
#                 bp = 1
#             else:
#                 bp = 2
#             cholesterol = request.form["Cholesterol"]
#             if cholesterol == "Normal":
#                 cholesterol = 0
#             else:
#                 cholesterol = 1
#             na_to_k = float(request.form["Na_to_K"])
#             t = [[age, sex, bp, cholesterol, na_to_k]]
#             pred = model.predict(t)  # Use the loaded model for prediction
#             prediction_text = "The predicted drug is {}".format(pred[0])
#             return render_template("submit.html", prediction_text=prediction_text)
#         except Exception as e:
#             error_message = "Error: {}".format(str(e))
#             return render_template("submit.html", error_message=error_message)
#     else:
#         return render_template("submit.html")

# if __name__ == "__main__":
#     flask_app.run(debug=True)



#main

# import numpy as np
# import pandas as pd
# from flask import Flask, request, render_template
# import pickle
# from sklearn.preprocessing import LabelEncoder

# # Create flask app
# flask_app = Flask(__name__)

# # Load the dataset
# data = pd.read_csv('drug200.csv')

# # Encode the target variable 'Drug'
# le = LabelEncoder()
# y = le.fit_transform(data['Drug'])

# # Save the label encoder
# pickle.dump(le, open("label_encoder.pkl", "wb"))

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Load the label encoder
# le = pickle.load(open("label_encoder.pkl", "rb"))

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         try:
#             age = int(request.form["Age"])
#             sex = request.form["Sex"]
#             if sex == "Male":
#                 sex = 1
#             else:
#                 sex = 0
#             bp = request.form["BP"]
#             if bp == "Low":
#                 bp = 0
#             elif bp == "Normal":
#                 bp = 1
#             else:
#                 bp = 2
#             cholesterol = request.form["Cholesterol"]
#             if cholesterol == "Normal":
#                 cholesterol = 0
#             else:
#                 cholesterol = 1
#             na_to_k = float(request.form["Na_to_K"])
#             t = [[age, sex, bp, cholesterol, na_to_k]]
#             pred = model.predict(t)  # Use the loaded model for prediction
#             drug_name = le.inverse_transform(pred)[0] # Decode the predicted label
#             prediction_text = "The predicted drug is {}".format(drug_name)
#             return render_template("submit.html", prediction_text=prediction_text)
#         except Exception as e:
#             error_message = "Error: {}".format(str(e))
#             return render_template("submit.html", error_message=error_message)
#     else:
#         return render_template("submit.html")

# if __name__ == "__main__":
#     flask_app.run(debug=True)


# import numpy as np
# from flask import Flask, request, render_template
# import pickle

# # Create flask app
# flask_app = Flask(__name__)

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Create a dictionary to map the integer labels to drug names
# drug_names = {0: "DrugA", 1: "DrugB", 2: "DrugC", 3: " DrugX", 4: "DrugY" } # Replace with the actual drug names

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         try:
#             age = int(request.form["Age"])
#             sex = request.form["Sex"]
#             if sex == "Male":
#                 sex = 1
#             else:
#                 sex = 0
#             bp = request.form["BP"]
#             if bp == "Low":
#                 bp = 0
#             elif bp == "Normal":
#                 bp = 1
#             else:
#                 bp = 2
#             cholesterol = request.form["Cholesterol"]
#             if cholesterol == "Normal":
#                 cholesterol = 0
#             else:
#                 cholesterol = 1
#             na_to_k = float(request.form["Na_to_K"])
#             t = [[age, sex, bp, cholesterol, na_to_k]]
#             pred = model.predict(t)[0]  # Use the loaded model for prediction
#             predicted_drug = drug_names[pred]  # Get the drug name from the dictionary
#             prediction_text = f"The predicted drug is {predicted_drug}"
#             return render_template("submit.html", prediction_text=prediction_text)
#         except Exception as e:
#             error_message = "Error: {}".format(str(e))
#             return render_template("submit.html", error_message=error_message)
#     else:
#         return render_template("submit.html")

# if __name__ == "_main_":
#     flask_app.run(debug=True)




# import numpy as np
# import pandas as pd
# from flask import Flask, request, render_template
# import pickle
# from sklearn.preprocessing import LabelEncoder

# # Create flask app
# flask_app = Flask(__name__)

# # Load the dataset
# data = pd.read_csv('drug200.csv')


# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))
# drug_names = {0: "DrugA", 1: "DrugB", 2: "DrugC", 3: " DrugX", 4: "DrugY" } # Replace with the actual drug names



# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods=["GET", "POST"])
# def predict():
#     if request.method == "POST":
#         try:
#             age = int(request.form["Age"])
#             sex = request.form["Sex"]
#             if sex == "Male":
#                 sex = 1
#             else:
#                 sex = 0
#             bp = request.form["BP"]
#             if bp == "Low":
#                 bp = 0
#             elif bp == "Normal":
#                 bp = 1
#             else:
#                 bp = 2
#             cholesterol = request.form["Cholesterol"]
#             if cholesterol == "Normal":
#                 cholesterol = 0
#             else:
#                 cholesterol = 1
#             na_to_k = float(request.form["Na_to_K"])
#             t = [[age, sex, bp, cholesterol, na_to_k]]

#             pred = model.predict(t)[0]
#             predicted_drug_label = int(pred)  # Convert NumPy scalar to Python int
#             predicted_drug = drug_names[predicted_drug_label]  # Get the drug name from the dictionary
#             prediction_text = f"The predicted drug is {predicted_drug}"

#             # pred = model.predict(t)  # Use the loaded model for prediction
#             # predicted_drug = drug_names[pred]  
#             # prediction_text = f"The predicted drug is {predicted_drug}"
#             return render_template("submit.html", prediction_text=prediction_text)
#         except Exception as e:
#             error_message = "Error: {}".format(str(e))
#             return render_template("submit.html", error_message=error_message)
#     else:
#         return render_template("submit.html")

# if __name__ == "__main__":
#     flask_app.run(debug=True)



import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            age = int(request.form["Age"])
            sex = request.form["Sex"]
            sex = 1 if sex == "Male" else 0

            bp = request.form["BP"]
            bp = 0 if bp == "Low" else 1 if bp == "Normal" else 2

            cholesterol = request.form["Cholesterol"]
            cholesterol = 0 if cholesterol == "Normal" else 1

            na_to_k = float(request.form["Na_to_K"])
            na_to_k = np.log(na_to_k)  # Ensure the input is transformed

            t = [[age, sex, bp, cholesterol, na_to_k]]
            pred = model.predict(t)
            prediction_text = "The predicted drug is {}".format(pred[0])
            return render_template("submit.html", prediction_text=prediction_text)
        except Exception as e:
            error_message = "Error: {}".format(str(e))
            return render_template("submit.html", error_message=error_message)
    else:
        return render_template("submit.html")

if __name__ == "__main__":
    app.run(debug=True)
