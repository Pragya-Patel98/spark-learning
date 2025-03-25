import logging.config
import sys
logging.config.fileConfig('properties/configuration/logging.config')

loggers =logging.getLogger("Validate")

def get_current_date(spark):
    try:
        loggers.warning(f'started the get_current_date method')
        query = "SELECT current_date"
        loggers.warning(f'Type of query: {type(query)}, Value: {query}')
        output = spark.sql(query)  # Ensure it's a single string
        output.show()
        current_date = output.collect()[0][0]
        loggers.warning(f'Validating spark object with current date -{current_date}')

    except Exception as e:
        loggers.error(f'Exception- {e}')
        sys.exit(1)

    else:
        loggers.warning(f"Validation Done, go forward...")

