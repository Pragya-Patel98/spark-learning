import logging.config
logging.config.fileConfig('properties/configuration/logging.config')

loggers =logging.getLogger("Ingest")

def load_files(spark, file_dir, file_format, header, inferSchema):
    try:
        loggers.info('load files method started............')

        if file_format == 'parquet':
            df = spark.read.format(file_format).load(file_dir)

        elif file_format == 'csv':
            df = spark.read.format(file_format).option(header= header).option(inferSchema= inferSchema).load(file_dir)
    except Exception as e:
        loggers.error(f"An error occured at load file == {e}")
        raise
    else:
        loggers.warning('dataframe created successfully which is of {file_format}')
        return df
    
def display_df(df):
    df_show = df.show()

    return df_show

def show_count(df):
    show_count = df.count()
    loggers.warning('Number of records persent is df are {}'.format(show_count))
    return show_count


