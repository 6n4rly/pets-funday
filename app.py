from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/pet-hotel")
def pet_hotel():
    return render_template("pet_hotel.html")

@app.route("/pet-grooming")
def pet_grooming():
    return render_template("pet_grooming.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
