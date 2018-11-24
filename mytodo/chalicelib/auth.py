import hashlib
import hmac
import datetime
from uuid import uuid4

import jwt
from chalice import UnauthorizedError


_SECRET = b'\xf7\xb6k\xabP\xce\xc1\xaf\xad\x86\xcf\x84\x02\x80\xa0\xe0'


def get_jwt_token(username, password, record):
    actual = hashlib.pbkdf2_hmac(
        record['hash'],
        password.encode('utf-8'),
        record['salt'].value,
        record['rounds']
    )
    expected = record['hashed'].value
    if hmac.compare_digest(actual, expected):
        now = datetime.datetime.utcnow()
        unique_id = str(uuid4())
        payload = {
            'sub': username,
            'iat': now,
            'nbf': now,
            'jti': unique_id,
            # NOTE: We can also add 'exp' if we want tokens to expire.
        }
        return jwt.encode(payload, _SECRET, algorithm='HS256')
    raise UnauthorizedError('Invalid password')


def decode_jwt_token(token):
    return jwt.decode(token, _SECRET, algorithms=['HS256'])
