import secrets
import string

from django.core.exceptions import ValidationError

CARD_NUMBER_LENGTH = 16


def generate_card_number() -> str:
    """
        Generate a random 16 digits string
    """
    return ''.join(secrets.choice(string.digits) for _ in range(CARD_NUMBER_LENGTH))


def validate_card_number(number:str):

    if not len(number) == CARD_NUMBER_LENGTH:
        raise ValidationError(f'Number must be {CARD_NUMBER_LENGTH} digits')
    
    if not all([ digit.isdigit() for digit in number]):
        raise ValidationError('Number must be only digit')