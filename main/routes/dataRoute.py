from flask import render_template, redirect, url_for
from main import app, db, models, forms

@app.route('/data',methods=['GET','POST'])
def data_page():
    data = models.Data.query.all()
    submitForm = forms.DataSubmitForm()
    clearForm = forms.DataClearForm()

    if submitForm.validate_on_submit():
        new_data = models.Data(
            data=submitForm.data.data
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('data_page'))
    
    if clearForm.validate_on_submit():
        models.Data.query.delete()
        db.session.commit()
        return redirect(url_for('data_page'))
    
    return render_template("data_page.html",submitForm=submitForm, clearForm=clearForm, data=data)