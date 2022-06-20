from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource


app = Flask(__name__)
# falsk가 서버인데
# falsk 서버로 Api를 개발할것이다
api = Api(app)

# 경로와 리소스(API 코드)를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
    # 경로는 1대1 처리해야 한다 아래와 같이 안됨
#api.add_resource(RecipeListResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')
                                                # 숫자가 바뀌니 변수처리

if __name__ == '__main__' :
    app.run()