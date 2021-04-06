"""Admin endpoints for SILA.
"""
from flask import Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy
from sila.models import db, Project, Phase, PhaseTypeEnum

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/initdb', methods=['GET'])
def initdb():
    print(current_app.config)
    db.drop_all()
    db.create_all()

    fp = Project(name='bla project', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.')
    db.session.add(fp)
    db.session.commit()

    p1 = Phase(type=PhaseTypeEnum.image_moderate, description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.', project_id=1, order=1)
    db.session.add(p1)
    p2 = Phase(type=PhaseTypeEnum.image_crop, description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.', project_id=1, order=2)
    db.session.add(p2)
    db.session.commit()

    return 'DB for SILA initialize'