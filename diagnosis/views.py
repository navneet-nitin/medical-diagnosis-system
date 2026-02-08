from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LUNG_MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml_models",
    "lung_cancer_final_reduced_model.pkl"
)

lung_model = joblib.load(LUNG_MODEL_PATH)

THYROID_MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml_models",
    "thyroid_model_reduced.pkl"
)

thyroid_model = joblib.load(THYROID_MODEL_PATH)

HEART_MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml_models",
    "heart_model.pkl"
)

heart_model = joblib.load(HEART_MODEL_PATH)

KIDNEY_MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml_models",
    "kidney_model.pkl"
)




@login_required
def home(request):
    return render(request, 'diagnosis/index.html')

@login_required
def heart(request):
    result = None

    if request.method == "POST":
        features = [
            int(request.POST['age']),
            int(request.POST['sex']),
            int(request.POST['cp']),
            int(request.POST['trestbps']),
            int(request.POST['chol']),
            int(request.POST['fbs']),
            int(request.POST['restecg']),
            int(request.POST['thalach']),
            int(request.POST['exang']),
            float(request.POST['oldpeak']),
            int(request.POST['slope']),
            int(request.POST['ca']),
            int(request.POST['thal']),
        ]

        prediction = heart_model.predict([features])[0]

        if prediction == 0:
            result = "🟢 No Heart Disease Detected"
        else:
            result = "🔴 Heart Disease Detected"

    return render(request, "diagnosis/heart.html", {"result": result})


@login_required
def diabetes(request):
    result = None

    if request.method == "POST":
        
        obj = joblib.load(os.path.join(BASE_DIR, "ml_models", "diabetes_model_final.pkl"))


        model = obj["model"]
        scaler = obj["scaler"]

        features = [
            float(request.POST["Pregnancies"]),
            float(request.POST["Glucose"]),
            float(request.POST["BloodPressure"]),
            float(request.POST["SkinThickness"]),
            float(request.POST["Insulin"]),
            float(request.POST["BMI"]),
            float(request.POST["DiabetesPedigreeFunction"]),
            float(request.POST["Age"]),
        ]

        scaled_features = scaler.transform([features])
        prediction = model.predict(scaled_features)[0]

        result = "Diabetes Detected" if prediction == 1 else "No Diabetes"

    return render(request, "diagnosis/diabetes.html", {"result": result})


@login_required
def lung(request):
    result = None

    if request.method == 'POST':
        features = [
            int(request.POST['alcohol_use']),
            int(request.POST['dust_allergy']),
            int(request.POST['balanced_diet']),
            int(request.POST['obesity']),
            int(request.POST['smoking']),
            int(request.POST['passive_smoker']),
            int(request.POST['coughing_of_blood']),
            int(request.POST['fatigue']),
            int(request.POST['shortness_of_breath']),
            int(request.POST['wheezing']),
            int(request.POST['swallowing_difficulty']),
            int(request.POST['clubbing_of_finger_nails']),
        ]

        prediction = lung_model.predict([features])[0]

        if prediction == 0:
            result = "🟢 Low Risk of Lung Cancer"
        elif prediction == 1:
            result = "🟠 Medium Risk of Lung Cancer"
        else:
            result = "🔴 High Risk of Lung Cancer"

    return render(request, 'diagnosis/lung.html', {'result': result})

@login_required
def kidney(request):
    result = None

    if request.method == "POST":
        features = [
            float(request.POST['Bp']),
            float(request.POST['Sg']),
            float(request.POST['Al']),
            float(request.POST['Su']),
            float(request.POST['Rbc']),
            float(request.POST['Bu']),
            float(request.POST['Sc']),
            float(request.POST['Sod']),
            float(request.POST['Pot']),
            float(request.POST['Hemo']),
            float(request.POST['Wbcc']),
            float(request.POST['Rbcc']),
            float(request.POST['Htn']),
        ]

        prediction = kidney_model.predict([features])[0]

        if prediction == 0:
            result = "🟢 No Kidney Disease Detected"
        else:
            result = "🔴 Kidney Disease Detected"

    return render(request, "diagnosis/kidney.html", {"result": result})



@login_required
def thyroid(request):
    result = None

    if request.method == "POST":
        features = [
            int(request.POST['age']),
            int(request.POST['sex']),
            int(request.POST['on_thyroxine']),
            int(request.POST['on_antithyroid_medication']),
            int(request.POST['pregnant']),
            int(request.POST['thyroid_surgery']),
            int(request.POST['query_hypothyroid']),
            int(request.POST['query_hyperthyroid']),
            float(request.POST['TSH']),
            float(request.POST['TT4']),
            float(request.POST['T4U']),
            float(request.POST['FTI']),
        ]

        prediction = thyroid_model.predict([features])[0]

        if prediction == 0:
            result = "🟢 Normal Thyroid"
        else:
            result = "🔴 Thyroid Disorder Detected"

    return render(request, "diagnosis/thyroid.html", {"result": result})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
