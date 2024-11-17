from sqlmodel import create_engine

db_url = "mysql+pymysql://study_python:nTMX8sPDSrsHzLC7@106.55.186.222:3306/study_python?charset=utf8"
engine = create_engine(db_url, echo=True, pool_size=8, pool_recycle=60 * 30)
