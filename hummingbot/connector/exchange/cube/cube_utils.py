from decimal import Decimal
from typing import Any, Dict

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True
EXAMPLE_PAIR = "BTC-USDT"
DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.001"),
    taker_percent_fee_decimal=Decimal("0.001"),
)


def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    :param exchange_info: the exchange information for a trading pair
    :return: True if the trading pair is enabled, False otherwise
    """
    return exchange_info.get("showStatus") is True


class CubeConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="cube", const=True, client_data=None)
    cube_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Cube API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )
    cube_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Cube API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )

    class Config:
        title = "cube"


KEYS = CubeConfigMap.construct()

OTHER_DOMAINS = ["cube_testnet"]
OTHER_DOMAINS_PARAMETER = {"cube_testnet": "cube_testnet"}
OTHER_DOMAINS_EXAMPLE_PAIR = {"cube_testnet": "BTC-USDT"}
OTHER_DOMAINS_DEFAULT_FEES = {"cube_testnet": DEFAULT_FEES}


class CubeTestnetConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="cube_testnet", const=True, client_data=None)
    cube_testnet_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Cube Testnet API Key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )
    cube_testnet_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Cube Testnet API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "cube_testnet"


OTHER_DOMAINS_KEYS = {"cube_testnet": CubeTestnetConfigMap.construct()}
