from flask import Flask
from flask_cors import CORS
from graphql_server.flask import GraphQLView
from scheme import schema

app = Flask(__name__)
CORS(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True 
    )
)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
