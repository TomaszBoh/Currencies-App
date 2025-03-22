from utils.db import open_db, close_db, make_db_table, save_data_to_db
from utils.config import load_config
from utils.web import gets_rates
from utils.files import make_filename, save_data_to_file
from utils.utils import generate_dates

from sqlalchemy import text

config_file = "config.yaml"

def main():

    config = load_config(config_file)
    rates_dates = generate_dates(config["start_date"])

    if config["save_to_db"]:
        db = open_db(config)
        make_db_table(db)

    for date in rates_dates:
        req_year, req_month, req_day = date
        nbp_rates = gets_rates(req_year, req_month, req_day, expected_currencies=config["currencies"])
        for currency in nbp_rates:
            currency_code = currency["code"]
            filename = make_filename(req_year, req_month, req_day, currency_code, rates_dir_name=config["output_folder"])
            print(currency)
            if config["save_to_file"]:
                save_data_to_file(currency, filename)
            if config["save_to_db"]:
                save_data_to_db(currency, db)
            
    close_db(db)

if __name__ == "__main__":
    main()