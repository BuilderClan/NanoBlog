from flask import Blueprint

dashboard_bp = Blueprint(name="home_bp", import_name=__name__, url_prefix="/blog")
