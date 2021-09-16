# -*- coding: utf-8 -*-
"""
Generic Constants and Classes
"""
import sys
from collections import namedtuple


FALSY = (False, 0, "?0", "no", "false", "False", "off")
TRUTHY =  (True, 1, "?1", "yes" "true", "True", 'on')

Versionage = namedtuple("Versionage", "major minor")

Version = Versionage(major=1, minor=0)  # KERI Protocol Version

SEPARATOR =  "\r\n\r\n"
SEPARATOR_BYTES = SEPARATOR.encode("utf-8")


Schemage = namedtuple("Schemage", 'tcp http https')
Schemes = Schemage(tcp='tcp', http='http', https='https')

Rolage = namedtuple("Rolage", 'controller witness registrar watcher judge juror')
Roles = Rolage(controller='controller', witness='witness', registrar='registrar',
               watcher='watcher', judge='judge', juror='juror')



class KeriError(Exception):
    """
    Base Class for keri exceptions

    To use   raise KeriError("Error: message")
    """


class ClosedError(KeriError):
    """
    Error attempting to use closed (unopened) resource such as file, database etc that is

    Usage:
        raise ClosedError("error message")
    """

class ConfigurationError(KeriError):
    """
    Error configuring or initing KERI component (Controller etc)

    Usage:
        raise ConfigurationError("error message")
    """

class AuthError(KeriError):
    """
    Error authenticating AuthN or authorizing AuthZ

    Usage:
        raise AuthError("error message")
    """

class AuthNError(AuthError):
    """
    Error authenticating

    Usage:
        raise AuthNError("error message")
    """

class AuthZError(AuthError):
    """
    Error authorizing

    Usage:
        raise AuthZError("error message")
    """

class DecryptError(AuthZError):
    """
    Error when attempting decryption

    Usage:
        raise DecryptError("error message")
    """

# errors associated with databases
class DatabaseError(KeriError):
    """
    Error accessing database

    Usage:
        raise DatabaseError("error message")
    """


class MissingEntryError(DatabaseError):
    """
    Error Missing entry or entry not found in database

    Usage:
        raise MissingEntryError("error message")
    """


# Errors when initing cryptographic material
class MaterialError(KeriError):
    """
    Base class for errors related to initing cryptographic material object instances
    """


class RawMaterialError(MaterialError):
    """
    Not Enough bytes in buffer bytearray for raw material
    Usage:
        raise ShortageError("error message")
    """


class EmptyMaterialError(MaterialError):
    """
    Empty or Missing Crypto Material
    Usage:
        raise EmptyMaterialError("error message")
    """


class UnknownCodeError(MaterialError):
    """
    Unknown or unrecognized code encountered during crypto material init
    Usage:
        raise UnknownCodeError("error message")
    """


class InvalidCodeIndexError(MaterialError):
    """
    Invalid code index encountered during crypto material init
    Usage:
        raise UnknownCodeError("error message")
    """


class InvalidCodeSizeError(MaterialError):
    """
    Invalid code size encountered during crypto material init
    Usage:
        raise UnknownCodeError("error message")
    """


# Errors validating  event messages and attachements
class ValidationError(KeriError):
    """
    Validation related errors
    Usage:
        raise ValidationError("error message")
    """


class MissingSignatureError(ValidationError):
    """
    Error At least One but Missing Enough Signatures for Threshold
    Usage:
        raise MissingSignatureError("error message")
    """


class MissingDestinationError(ValidationError):
    """
    Destination field ("i") mising from exn message
    Usage:
        raise MissingDestinationError("error message")
    """


class MissingWitnessSignatureError(ValidationError):
    """
    Error Missing Enough Witness Signatures for Threshold
    Usage:
        raise MissingWitnessSignatureError("error message")
    """


class MissingDelegationError(ValidationError):
    """
    Error Missing Event with Delegation source attachments
    Usage:
        raise MissingDelegationError("error message")
    """


class OutOfOrderError(ValidationError):
    """
    Error prior event missing from log so can't verify sigs on this event
    Usage:
        raise OutOfOrderError("error message")
    """


class LikelyDuplicitousError(ValidationError):
    """
    Error event is likely duplicitous
    Usage:
        raise LikelyDuplicitousError("error message")
    """


class UnverifiedWitnessReceiptError(ValidationError):
    """
    Error witness receipt is unverfied  event not yet in database
    Usage:
        raise UnverifiedWitnessReceiptError("error message")
    """


class UnverifiedReceiptError(ValidationError):
    """
    Error receipt is unverfied because event not yet in database
    Usage:
        raise UnverifiedReceiptError("error message")
    """


class UnverifiedTransferableReceiptError(ValidationError):
    """
    Error reciept from transferable identifier (validator) is unverfied
    Usage:
        raise UnverifiedTransferableReceiptError("error message")
    """


class UnverifiedProofError(ValidationError):
    """
    Error signature from credential CESR proof is unverfied
    Usage:
        raise UnverifiedProofError("error message")
    """


class DerivationError(ValidationError):
    """
    Derivation related errors
    Usage:
        raise DerivationError("error message")
    """

class UnverifiedReplyError(ValidationError):
    """
    Error Reply message not verified usually missing sigs
    Usage:
        raise UnverifiedReplyError("error message")
    """


# Stream Parsing and Extraction Errors
class ExtractionError(KeriError):
    """
    Base class for errors related to extracting messages and attachments
    from message streams. Rasised in stream processing when extracted data
    does not meet expectations.
    """


class ShortageError(ExtractionError):
    """
    Not Enough bytes in buffer for complete message or material
    Usage:
        raise ShortageError("error message")
    """


class ColdStartError(ExtractionError):
    """
    Bad tritet in first byte of cold start of incoming message stream

    Usage:
        raise ColdStartError("error message")
    """


class SizedGroupError(ExtractionError):
    """
    Error while extracted within sized group. Assumes sized group already
    deleted from stream before raise

    Usage:
        raise SizedGroupError("error message")
    """


class VersionError(ExtractionError):
    """
    Bad or Unsupported Version

    Usage:
        raise VersionError("error message")
    """


class DeserializationError(ExtractionError):
    """
    Error deserializing message
    Usage:
        raise DeserializationError("error message")
    """


class ConversionError(ExtractionError):
    """
    Problem with Base64 to Binary conversion

    Usage:
        raise ConversionError("error message")
    """


class DerivationCodeError(ExtractionError):
    """
    Derivation Code cryppto material conversion errors
    Usage:
        raise DerivationCodeError("error message")
    """


class UnexpectedCodeError(DerivationCodeError):
    """
    Unexpected or unknown or unsupported derivation code during extraction
    Usage:
        raise UnexpectedCodeError("error message")
    """


class UnexpectedCountCodeError(DerivationCodeError):
    """
    Encountered count code start char "-" unexpectantly
    Usage:
        raise DerivationCodeError("error message")
    """


class UnexpectedOpCodeError(DerivationCodeError):
    """
    Encountered opcode code start char "_" unexpectantly
    Usage:
        raise DerivationCodeError("error message")
    """


class MissingAnchorError(ValidationError):
    """
    Error TEL event missing anchor to validating KEL event
    Usage:
        raise MissingAnchorError("error message")
    """


class ExchangeError(KeriError):
    """
    Error handling an `exn` message
    Usage:
        raise ExchangeError("error message")
    """


class InvalidEventTypeError(KeriError):
    """
    Error trying to process an unexpected event type
    Usage:
        raise InvalidEventTypeError("error message")
    """
