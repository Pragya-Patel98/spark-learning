import logging
import logging.config
import os
import load_env as env
from  create_spark import get_spark_object
from validate import get_current_date
from ingest import load_files, display_df, show_count


logging.config.fileConfig('properties/configuration/logging.config')


def main():
    try:
        # logging("i am inside main function")
        # logging(env.header)
        # logging(env.src_olap)
        spark = get_spark_object(env.envn, env.appName)
        logging.info(f"Environment: {env.envn}, AppName: {env.appName}")
        # logging.info(f"spark***-> {spark}")
        # logging.info("Spark Object Created")
        get_current_date(spark)
        if spark is None:
            raise ValueError("Failed to create SparkSession")
        
        for file in os.listdir(env.src_olap):
            print(f"File : {file}")
            file_dir= env.src_olap + "\\" + file
            print("**",file_dir)
            if file.endswith('.parquet'):
                file_format = 'parquet'
                header = "NA"
                inferSchema = "NA"

            elif file.endswith('csv'):
                file_format = 'csv'
                header = "True"
                inferSchema = "True"
        logging.info(f"reading file of {file_format}")
        df = load_files(spark, file_dir, file_format, header, inferSchema)
        display_df(df)
        show_count(df)
    except Exception as E:
        logging.error("Exception-{E}")

if __name__ == '__main__':
    main()

