from base64 import b64decode, b64encode
from binascii import hexlify, unhexlify
from functools import wraps
from hashlib import blake2b
from json import dumps, loads

from .exceptions import (InvalidBalance, InvalidBlock, InvalidBlockType, InvalidBlockHash, InvalidSignature, InvalidWork)

BLOCKTYPE = (
    "State",
    "Send",
    "Receive",
	"Change",
	"Open",
	"ContractReward",
	"ContractSend",
	"ContractRefund",
	"ContractError",
	"SmartContract",
	"Online",
	"Invalid"
)

WORKTHRESHOLD = "0xfffffe0000000000" #18446741874686296064
WORKTHRESHOLD_TESTNET = "0x0000000000fffffe" #16777214

class StateBlock:
    """ WIP """

    __slots__ = (
        "__Type", "__Token", "__Address", "__Balance",
        "__Vote", "__Network", "__Storage", "__Oracle",
        "__Previous", "__Link", "__Sender", "__Receiver",
        "__Message", "__Data", "__PoVHeight", "__Timestamp",
        "__Extra", "__Representative", "__Work", "__Signature"
    )

    def __init__(self, Type, **kwargs):
        pass