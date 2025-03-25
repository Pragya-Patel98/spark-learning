import os

os.environ['envn']= 'DEV'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

header = os.environ['header']
inferSchema = os.environ['inferSchema']
envn = os.environ['envn']

appName = "Spark_Project"

# to get currend_dir 
# print(os.getcwd())
current = os.getcwd() #'C:\Users\pragy\Desktop\spark_poc\spark-learning'

src_olap = current +  "\source\olap"
src_oltp = current +  "\source\oltp"
