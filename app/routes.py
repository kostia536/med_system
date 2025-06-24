
from flask import Blueprint, render_template, request, redirect
from .models import Patient
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        test_name = request.form['test_name']

        results = ""
        if test_name == "Загальний аналіз крові":
            results = f"Гемоглобін: {request.form.get('hemoglobin')} г/л\n" \
                      f"Еритроцити: {request.form.get('erythrocytes')} ×10¹²/л\n" \
                      f"Лейкоцити: {request.form.get('leukocytes')} ×10⁹/л\n" \
                      f"Тромбоцити: {request.form.get('platelets')} ×10⁹/л"
        elif test_name == "Біохімічний аналіз крові":
            results = f"Глюкоза: {request.form.get('glucose')} ммоль/л\n" \
                      f"Білірубін: {request.form.get('bilirubin')} мкмоль/л\n" \
                      f"АЛТ: {request.form.get('alt')} од/л\n" \
                      f"АСТ: {request.form.get('ast')} од/л"
        elif test_name == "Аналіз сечі":
            results = f"Колір: {request.form.get('color')}\n" \
                      f"Прозорість: {request.form.get('clarity')}\n" \
                      f"Щільність: {request.form.get('density')} г/см³\n" \
                      f"pH: {request.form.get('ph')}"

        patient = Patient(
            full_name=request.form['full_name'],
            gender=request.form['gender'],
            birth_date=datetime.strptime(request.form['birth_date'], '%Y-%m-%d'),
            test_name=test_name,
            results=results
        )
        db.session.add(patient)
        db.session.commit()
        return redirect('/success')
    return render_template('register.html')

@main.route('/success')
def success():
    return "Пацієнта зареєстровано успішно!"
