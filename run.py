from flask import Flask, render_template, url_for, request

import food_math
import json_func

app = Flask(__name__)


items = json_func.open_json("items.json")

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		for item in items:
			if item in request.form:
				if request.form[item] == "add":
					items[item]["count"] += 1
				elif request.form[item] == "sub":
					items[item]["count"] -= 1

	json_func.save_json(items, "items.json")
	total = food_math.add_total(items)
	return render_template("index.html", page="Home", items=items, stats=total)

if __name__ == "__main__":
	app.run()