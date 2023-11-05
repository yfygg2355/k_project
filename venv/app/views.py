#!/usr/bin/python3

from flask import flash, redirect, render_template, url_for, request

from app import app, db
from app import Reviews

from forms import Form

@app.route('/', methods=["GET", "POST"])
def reviews():
    
    form = Form()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            text = form.text.data
            dataReviews = Reviews(name=name, text=text)
            db.session.add(dataReviews)
            db.session.commit()
            flash('Відгук збережено', 'success')
            return redirect(url_for('reviews_data'))
        else:
            flash('Відгук не збережено', 'danger')
    return render_template('reviews.html', form=form)


@app.route('/reviews_data')
def reviews_data():
    dataReviews = Reviews.query.all()
    return render_template('reviews_data.html', dataReviews=dataReviews)