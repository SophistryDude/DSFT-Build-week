from .app import create_app

APP = create_app()

if __name__ == '__main__':
    app.run_server(debug=True, port=8077, threaded=True)