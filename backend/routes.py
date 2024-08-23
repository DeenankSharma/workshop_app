from controllers import read_task, add_task

def configure_routes(app):
    app.route('/read')(read_task)
    app.route('/add', methods=['POST'])(add_task)