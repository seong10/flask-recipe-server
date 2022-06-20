from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource
from resources.user import UserLoginResource, UserRegisterResource


app = Flask(__name__)
## falsk가 서버인데
## falsk 서버로 Api를 개발할것이다

# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 라이브러리 만들기 
jwt = JWTManager(app)

api = Api(app)

# 경로와 리소스(API 코드)를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
    # 경로는 1대1 처리해야 한다 아래와 같이 안됨
#api.add_resource(RecipeListResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')
                                                # 숫자가 바뀌니 변수처리
api.add_resource(UserRegisterResource, '/users/register')
api.add_resource(UserLoginResource, '/users/login')




if __name__ == '__main__' :
    app.run()