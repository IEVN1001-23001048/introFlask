from bluepints.alumnos.routes import alumnos_bp
from bluepints.maestros.routes import maestros_bp


def registrar_blueprints(app):
    app.registrar_blueprint(alumnos_bp)
    app.registrar_blueprint(maestros_bp)