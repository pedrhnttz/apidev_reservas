from config import app, db
from controllers.reserva_route import reserva_bp

app.register_blueprint(reserva_bp)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
