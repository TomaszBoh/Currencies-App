from flask import Flask
from flask import jsonify
from flask import render_template
from datetime import datetime, timedelta
from utils.config import load_config
from utils.db import close_db, load_data_from_db, open_db, currency_list

CONFIG_FILE = "config.yaml"

config = load_config(CONFIG_FILE)

#app object
app = Flask("Walutomat")

#adding first routing
@app.route("/")
@app.route("/rate")
@app.route("/rate/<currency>")
@app.route("/rate/<currency>/<start_date>")
@app.route("/rate/<currency>/<start_date>/<end_date>")


def rate(currency="eur", start_date=None, end_date=None):
    today = datetime.now()
    today_30_days_ago = today - timedelta(days=30)

    #if's to assign dates if not pass
    if not start_date:
        start_date = today_30_days_ago.strftime("%Y-%m-%d")
    if not end_date:
        end_date = today.strftime("%Y-%m-%d")

    db = open_db(config) #db connection
    results = load_data_from_db(db, currency, start_date, end_date) #loading data
    cur_list = currency_list(db)
    close_db(db)
    return render_template("page.html", data=results, currencies=cur_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)