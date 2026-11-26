from flask import Blueprint, current_app, jsonify

from ..db import connect, execute


def list_students_blueprint():
    blueprint = Blueprint("list_students", __name__)

    @blueprint.route("/students", methods=["GET"])
    def list_students():
        connection = connect(current_app.config["DATABASE_URL"])
        try:
            rows = execute(
                connection,
                "SELECT * FROM students ORDER BY id ASC",
            ).fetchall()
            students = [dict(row) for row in rows]
        finally:
            connection.close()
        return jsonify(students)

    return blueprint
