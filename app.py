from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", title="Homepage")

@app.route('/contact')
def contact():  # put application's code here
    return render_template("contact.html", title="Contact Us")

@app.route('/gallery')
def gallery():  # put application's code here
    return render_template("gallery.html", title="Photo Gallery")


@app.route('/history')
def history():  # put application's code here
    return render_template("history.html", title="History of Ngunnawal")

@app.route('/grid')
def grid():  # put application's code here
    return render_template("grid.html", title="Bootstrap Grid")



if __name__ == '__main__':
    app.run()
