from http import HTTPStatus
from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector

class RecipePublishResource(Resource) :
    # 레시피를 공개한다

                ## 이런것들은 툴 사용법이다
                ## 외우는것들
    def put(self, recipe_id) :
                ## app.py에 쓴
                ## 경로랑 똑같이
        
        # 해당 레시피아이디를 가지고
        # 데이터베이스에서 publish 컬럼을
        # 1 로 바꿔준다.

        try :
            # 데이터 업데이트
            # 1. DB에 연결
            connection = get_connection()

            
            # 2. 쿼리문 만들기
            query =''' update recipe
                        set is_publish = 1
                        where id = %s;'''

            record = (recipe_id , )
                    ## 튜플이니 ',' 써야 튜플

            # 3. 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서를 이용해서 실행한다
            # 실행
            cursor.execute(query, record)

            # 5. 커넥션을 커밋해줘야한다 => 디비에 영구적으로 반영하는것
            connection.commit()

            # 6. 자원 해제
            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503        
        
        return {'result' : 'success'}, 200

    # 레시피를 임시저장한다.
    def delete(self, recipe_id) :
        
        # is_publish 컬럼을 0으로 변경

        try :
            # 데이터 업데이트
            # 1. DB에 연결
            connection = get_connection()

            
            # 2. 쿼리문 만들기
            query =''' update recipe
                        set is_publish = 0
                        where id = %s;'''

            record = (recipe_id , )
                    ## 튜플이니 ',' 써야 튜플

            # 3. 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서를 이용해서 실행한다
            # 실행
            cursor.execute(query, record)

            # 5. 커넥션을 커밋해줘야한다 => 디비에 영구적으로 반영하는것
            connection.commit()

            # 6. 자원 해제
            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503        
        
        return {'result' : 'success'}, 200