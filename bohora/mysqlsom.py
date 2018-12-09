import pymysql

# db = pymysql.connect("localhost", "root", "root", "companydb")
#
# cursor = db.cursor()
# #
# # cursor.execute("SELECT VERSION()")
# #
# # data = cursor.fetchone()
# #
# # print("Database version : %s " % data)
#
#
# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE2")
#
# # Create table as per requirement
# sql = """CREATE TABLE EMPLOYEE3 (
#    FIRST_NAME  CHAR(20) NOT NULL,
#    LAST_NAME  CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT )"""
#
# # cursor.execute(sql)
#
# # Read
# sql_read = "SELECT * FROM employee \
#               WHERE salary > '%d'" % (75000)
#
# cursor.execute(sql_read)
# results = cursor.fetchall()
#
# db.close()

########## POSTGRESQL #####
# from sqlalchemy import create_engine, select, Table, MetaData
# engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5433/testDB') # works without +psycopg2 as well
# # engine = create_engine('postgresql://postgres:root@localhost:5433/dvdrental')
#
# print(engine.table_names())
# metadata = MetaData()
# actor = Table('actor', metadata, autoload=True, autoload_with=engine)
#
# stmt = select([actor])
#
# print(engine.execute(stmt).fetchone())
#
# for result in engine.execute(stmt).fetchmany(5):
#     print(result.actor_id, result.first_name, result.last_name)
#

######### MYSQL ########
# Import create_engine function
from sqlalchemy import create_engine, MetaData, select, Table

# Create an engine to the census database
engine = create_engine('mysql+pymysql://root:root@localhost:3306/companydb')
# Print the table names
print(engine.table_names())

metadata = MetaData()
employee = Table('employee', metadata, autoload = True, autoload_with = engine)

stmt = select([employee])

results = engine.execute(stmt).fetchall()

print(repr(metadata.tables['employee']))

print(engine.execute(stmt).fetchone())

for result in engine.execute(stmt).fetchmany(10):
    print(result.emp_id, result.first_name, result.last_name, result.birth_day)


# SQLAlchemy and Pandas
import pandas as pd
df = pd.DataFrame(results)
print(results[0].keys())  #assign column names

print("_____________________________________________________________________")
df.columns = results[0].keys()
print(df)

