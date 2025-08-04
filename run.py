from flask import Flask
from app.routes import bp

app = Flask(_name_)
app.register_blueprint(bp)

if _name_ == "_main_":
    app.run(debug=True)
