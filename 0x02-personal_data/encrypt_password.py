#!/usr/bin/env python3
''' module contains function to incrypt '''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' Hashes password by bcrypt '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' checks password with hashed password '''
    return bcrypt.checkpw(password.encode(), hashed_password)
