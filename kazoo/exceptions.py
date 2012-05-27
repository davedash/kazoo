"""Zookeeper exceptions and mappings"""
import zookeeper
from zookeeper import (
    SystemErrorException,
    RuntimeInconsistencyException,
    DataInconsistencyException,
    ConnectionLossException,
    MarshallingErrorException,
    UnimplementedException,
    OperationTimeoutException,
    BadArgumentsException,
    ApiErrorException,
    NoNodeException,
    NoAuthException,
    BadVersionException,
    NoChildrenForEphemeralsException,
    NodeExistsException,
    InvalidACLException,
    AuthFailedException,
    NotEmptyException,
    SessionExpiredException,
    InvalidCallbackException
)

# this dictionary is a port of err_to_exception() from zkpython zookeeper.c
_ERR_TO_EXCEPTION = {
    zookeeper.SYSTEMERROR: SystemErrorException,
    zookeeper.RUNTIMEINCONSISTENCY: RuntimeInconsistencyException,
    zookeeper.DATAINCONSISTENCY: DataInconsistencyException,
    zookeeper.CONNECTIONLOSS: ConnectionLossException,
    zookeeper.MARSHALLINGERROR: MarshallingErrorException,
    zookeeper.UNIMPLEMENTED: UnimplementedException,
    zookeeper.OPERATIONTIMEOUT: OperationTimeoutException,
    zookeeper.BADARGUMENTS: BadArgumentsException,
    zookeeper.APIERROR: ApiErrorException,
    zookeeper.NONODE: NoNodeException,
    zookeeper.NOAUTH: NoAuthException,
    zookeeper.BADVERSION: BadVersionException,
    zookeeper.NOCHILDRENFOREPHEMERALS: NoChildrenForEphemeralsException,
    zookeeper.NODEEXISTS: NodeExistsException,
    zookeeper.INVALIDACL: InvalidACLException,
    zookeeper.AUTHFAILED: AuthFailedException,
    zookeeper.NOTEMPTY: NotEmptyException,
    zookeeper.SESSIONEXPIRED: SessionExpiredException,
    zookeeper.INVALIDCALLBACK: InvalidCallbackException,
}


def err_to_exception(error_code, msg=None):
    """Return an exception object for a Zookeeper error code
    """
    try:
        zkmsg = zookeeper.zerror(error_code)
    except Exception:
        zkmsg = ""

    if msg:
        if zkmsg:
            msg = "%s: %s" % (zkmsg, msg)
    else:
        msg = zkmsg

    exc = _ERR_TO_EXCEPTION.get(error_code)
    if exc is None:

        # double check that it isn't an ok resonse
        if error_code == zookeeper.OK:
            return None

        # otherwise generic exception
        exc = Exception
    return exc(msg)


class CancelledError(Exception):
    """Raised when a process is cancelled by another thread"""