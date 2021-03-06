'''
Created on Jul 18, 2014

@author: atiwari
'''
import json 

class AttemptType(object):
    BOOTSTRAP = 'bootstrap'
    OPTIMISTIC = 'optimistic'
    FALLBACK = 'fallback'

class TokenType(object):
    UUID = 'uuid'
    PKI = 'pik'

class OprCode(object):
    VALID = 'valid'
    INVALID = 'invalid'
    INDETERMINATE = 'indeterminate'
    OK = 'ok'
    NOT_FOUND = 'not_found'


class KeyDTO(object):
    """DTO for key"""
    def __init__(self, alg=None,
                 bit_length=None,
                 mode=None,
                 passphrase=None,
                 key=None,
                 public_key_file=None,
                 private_key_file=None):
        self.alg = alg
        self.bit_length = bit_length
        self.mode = mode
        self.passphrase = passphrase
        self.key = key
        self.public_key_file = public_key_file
        self.private_key_file = private_key_file

class SessionDTO(json.JSONEncoder):
    """DTO for session interchange"""
    def __init__(self, json=None):
        self.cloud_id = json.get('cloud_id') if json else None
        self.session_key = json.get('session_key') if json else None
        self.login_time = json.get('login_time') if json else None
        self.valid_till = json.get('valid_till') if json else None
        self.attempt_type = json.get('attempt_type') if json else None

class AuthTokenDTO(json.JSONEncoder):
    """DTO for token interchange"""
    def __init__(self, json=None):
        #self.cloud_id = json.get('cloud_id') if json else None
        self.token_id = json.get('token_id') if json else None
        self.token_type = json.get('token_type') if json else None
        self.token_str = json.get('token_str') if json else None
        self.opr_code = json.get('opr_code') if json else None
        self.details = json.get('details') if json else None

class AuthDTO(json.JSONEncoder):
    """DTO for token interchange"""
    def __init__(self, json=None):
        #self.cloud_id = json.get('cloud_id') if json else None
        self.username = json.get('username') if json else None
        self.user_id = json.get('user_id') if json else None
        self.user_domain_id = json.get('user_domain_id') if json else None
        self.password = json.get('password') if json else None
        self.project_domain_id = json.get('project_domain_id') if json else None
        self.project_id = json.get('project_id') if json else None
        self.project_name = json.get('project_name') if json else None