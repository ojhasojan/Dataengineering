
import pandas as pd
from sqlalchemy import create_engine
from logger_config import logger   # import the logger

def main():
    logger.info("Starting daily sales load...")

    try:
        # 1) Read CSV
        df = pd.read_csv("daily_sales.csv")
        logger.info("CSV loaded successfully with %d rows and %d columns.", len(df), len(df.columns))

        # 2) Create Postgres engine
        # Using host.docker.internal so your container can reach Postgres running on your Mac via docker-compose
        engine = create_engine(
            "postgresql+psycopg2://demo_user:demo_pass@localhost:5432/salescsv_db"
        )

        # 3) Dump DataFrame to Postgres table
        df.to_sql("daily_sales", engine, if_exists="replace", index=False)
        logger.info("Data successfully loaded into Postgres table 'daily_sales'.")

        # (Optional) show a preview in the console:
        print(df.head())

    except Exception as e:
        logger.error("Error while loading CSV to Postgres: %s", e)
        raise

    logger.info("Process finished.")

if __name__ == "__main__":
    main()

