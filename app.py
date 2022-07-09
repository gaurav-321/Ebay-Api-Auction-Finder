from flask import url_for, redirect, Flask, render_template, request, jsonify, session
import os
from main import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()

search_list = []
all_data = []


@app.route("/ebaybidder")
def home():
    auto_update()
    return render_template("home.html", search_list=search_list, all_data=all_data)


@app.route("/add_product", methods=["GET"])
def add_product():
    search_list.append((request.args.get("title"),int( request.args.get("min")), int(request.args.get("max"))))
    return redirect(url_for("home"))


@app.route("/delete", methods=["GET"])
def delete_product():
    del search_list[int(request.args.get("id"))]
    return redirect(url_for("home"))


def auto_update():
    all_data.clear()
    for query in search_list:
        search = Search(query[0], query[1], query[2])
        data = search.get_best_match()
        all_data.extend(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
