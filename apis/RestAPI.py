from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter
from sqlalchemy import MetaData,Table,func
from connection_db import db_connection,db_class


import uvicorn

data = db_class.Newdata
metadata = MetaData()
engine = db_connection.engineconn()
session = engine.sessionmaker()
router = APIRouter()

#------------------Class 선언 부분------------------


#------------------Class 선언 부분------------------

#-------------------Api 실행 부분-------------------

# 뉴스 내용 전체 호출
@router.get('/news')
async def newsdata():
    table = Table('newdata', metadata, autoload=True, autoload_with=engine.engine)
    newslist = session.query(table).all()

    return newslist

@router.get('/news/newslist')
async def news_list():
    table1 = Table('news_link', metadata, autoload=True, autoload_with=engine.engine)
    newslist = session.query(table1).all()
    return newslist


# 뉴스 리스트 호출
# @app.get("/newslist")
# async def Newslist():
#     connect_cursor = dbconn('News')
#     develop_cursor = connect_cursor.conn_cursor()
#
#     news_link_search = "SELECT * FROM news_link"
#     develop_cursor.execute(news_link_search)
#     newslist = develop_cursor.fetchall()
#
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#     return newslist
#
# # db에 새로운 링크 집어 넣는 곳
# @app.post("/addnews")
# async def UpdateNews(addnews : addNews):
#
#     connect_cursor = dbconn('News')
#     develop_cursor = connect_cursor.conn_cursor()
#
#     new_News = []
#
#     updates =" INSERT INTO news_link VALUES(default,%s,%s)"
#     add_new_Data = dict(addnews)
#
#     new_News.append(add_new_Data['name'])
#     new_News.append(add_new_Data['link'])
#     develop_cursor.execute(updates,new_News)
#
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#
#     return HTTPException(status_code=200, detail="SUCCESS INSERT DATA")
#
# # 뉴스 이름별로
# @app.get("/news/{newsname}")
# async def News(newsname: str):
#     connect_cursor = dbconn('News')
#     develop_cursor = connect_cursor.conn_cursor()
#
#     findDB = "SELECT * FROM newdata WHERE newsname ="+f'\'{newsname}\''
#     develop_cursor.execute(findDB)
#     SelectNews = develop_cursor.fetchall()
#
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#     return SelectNews
#
# # 뉴스 날짜별로
# @app.get("/news/{newsname}/{date}")
# async def NewsDate(date: str):
#     connect_cursor = dbconn('News')
#     develop_cursor = connect_cursor.conn_cursor()
#
#     findDATE = f"SELECT * FROM newdata WHERE DATE(recordtime) =" +f'\'{date}\''
#     develop_cursor.execute(findDATE)
#     SelectNews = develop_cursor.fetchall()
#
#     connect_cursor.conn_commit()
#     connect_cursor.conn_close()
#
#     return SelectNews
#
# #주소입력을 잘 못했으면? 어떻게 표현 할건가?
#
# @app.get("/")
# async def main():
#     main = "fastapi 메인페이지 입니다."
#     return main

#-------------------Api 실행 부분-------------------
if __name__ == '__main__':
    uvicorn.run(router)
