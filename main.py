import sys
import app

if __name__ == '__main__':

    request_type = sys.argv[1]

    @app.post
    def post_user(request: str):
        return request

    @app.get
    def get_user(request: str):
        return request

    @app.put
    def update_user(request: str):
        return request


    @app.delete
    def delete_user(request: str):
        return request


    req = sys.argv[2]

    match request_type:
        case 'GET':
            print(get_user(req))
        case 'POST':
            print(post_user(req))
        case 'PUT':
            print(update_user(req))
        case 'DELETE':
            print(delete_user(req))
        case _:
            raise Exception("Invalid Request")
