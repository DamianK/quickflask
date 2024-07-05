from flask import render_template, Blueprint

main = Blueprint("main", __name__, template_folder="templates/main", url_prefix="/")


@main.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")
