import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.clmt07jbjcoe.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe_db',
        user = 'recipe_user',
        # 어드민 유저로 하면 안됨
        password = 'recipe1234'
    )
    return connection