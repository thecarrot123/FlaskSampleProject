from flask import render_template, redirect, url_for
from main import app, db, models, forms

@app.route('/data',methods=['GET','POST'])
def data_page():
    data = models.Data.query.all()
    submitForm = forms.DataSubmitForm()
    clearForm = forms.DataClearForm()
    if clearForm.clear.data and clearForm.validate():
        models.Data.query.delete()
        db.session.commit()
        return redirect(url_for('data_page'))

    if submitForm.submit.data and submitForm.validate():
        new_data = models.Data(
            data=submitForm.data.data
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('data_page'))
    
    if submitForm.errors != {}:
        for err_msg in submitForm.errors.values():
            print(f'Error: {err_msg}')

    
    return render_template("data_page.html",submitForm=submitForm, clearForm=clearForm, data=data)