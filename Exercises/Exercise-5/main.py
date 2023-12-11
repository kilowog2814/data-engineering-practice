import psycopg2
import pandas as pd
import os
import glob
from sqlalchemy import create_engine

diretorio = "Exercises\\Exercise-5\\data"


def main():
    host = "data-engineeing-practice.cshgsmdghizi.sa-east-1.rds.amazonaws.com"
    database = "exercise_5"
    user = "postgres"
    pas = "postgresql"
    conn = psycopg2.connect(
        host=host, database=database, user=user, password=pas, port="5432"
    )

    engine = create_engine(f"postgresql://{user}:{pas}@{host}:5432/exercise_5")

    cur = conn.cursor()

    with open("Exercises\\Exercise-5\\tables.sql", "r") as file:
        query = file.read()

    cur.execute(query)

    conn.commit()

    csv_files = glob.glob(os.path.join(diretorio, "*.csv"))

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)

        if "accounts" in csv_file:
            postgres_table = "tb_accounts"

        elif "products" in csv_file:
            postgres_table = "tb_products"

        elif "transactions" in csv_file:
            postgres_table = "tb_transactions"

        df.to_sql(postgres_table, con=engine, if_exists="append", index=False)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
