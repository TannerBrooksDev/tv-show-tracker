import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shows.db"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-me")

db = SQLAlchemy(app)

STATUSES = [
    "Watching",
    "On Break / Returning Soon",
    "Want to Watch",
    "Completed",
]


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    next_release = db.Column(db.String(20), nullable=True)
    rating = db.Column(db.Integer, nullable=True)


@app.route("/")
def index():
    shows = Show.query.order_by(Show.title).all()
    return render_template("index.html", shows=shows)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        status = request.form.get("status", "")
        next_release = request.form.get("next_release", "").strip() or None
        rating_value = request.form.get("rating", "").strip()

        try:
            rating = int(rating_value) if rating_value else None
        except ValueError:
            rating = None
            flash("Rating must be a whole number from 1 to 5.", "danger")
            return render_template(
                "add.html", statuses=STATUSES, form_data=request.form
            )

        if not title:
            flash("Please enter a show title.", "danger")
        elif status not in STATUSES:
            flash("Please choose a valid status.", "danger")
        elif rating is not None and not 1 <= rating <= 5:
            flash("Rating must be from 1 to 5.", "danger")
        else:
            show = Show(
                title=title,
                status=status,
                next_release=next_release,
                rating=rating,
            )
            db.session.add(show)
            db.session.commit()
            flash(f"{title} was added to your tracker.", "success")
            return redirect(url_for("index"))

        return render_template("add.html", statuses=STATUSES, form_data=request.form)

    return render_template("add.html", statuses=STATUSES, form_data={})


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    show = db.get_or_404(Show, id)
    db.session.delete(show)
    db.session.commit()
    flash(f"{show.title} was removed from your tracker.", "success")
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
