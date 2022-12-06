import secrets
import string

from django.core.exceptions import ValidationError

CARD_SERIAL_LENGTH = 16


def generate_card_serial() -> str:
    """
        Generate a random 16 digits string
    """
    return ''.join(secrets.choice(string.digits) for _ in range(CARD_SERIAL_LENGTH))


def validate_card_serial(serial:str):

    if not len(serial) == CARD_SERIAL_LENGTH:
        raise ValidationError(f'Serial must be {CARD_SERIAL_LENGTH} digits')
    
    if not all([ digit.isdigit() for digit in serial]):
        raise ValidationError('Serial must be only digit')