# importing libraries
from flask import Blueprint, g, jsonify, request
from flask_mail import Mail, Message
from . import auth
from . import utils
from flaskr.db import get_db
from . import constants

errors = constants.errors

extract_dict_from_keys = utils.extract_dict_from_keys

bp = Blueprint('mail', __name__, url_prefix='/mail')


@bp.route("/send")
def send_mail():
    msg = Message(
        'Hello',
        sender='noreply.smartbilling@gmail.com',
        recipients=['vsnkrl2000@gmail.com']
    )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    g.mail.send(msg)
    return 'Sent'
