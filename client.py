from httpx import Client
from pprint import pprint
from typing import TYPE_CHECKING, Optional


# ======================================================================================================================
class Platforms:
    PC = 'pc'
    PS4 = 'ps4'
    XB1 = 'xb1'
    SWI = 'swi'


# ======================================================================================================================
class WarframeClient:
    SUCESS = 200

    def __init__(self, base_url='https://api.warframestat.us') -> None:
        self.base_url = base_url
        self.client = Client()
        self.errors = {}

    # ------------------------------------------------------------------------------------------------------------------
    def __enter__(self):
        return self

    # ------------------------------------------------------------------------------------------------------------------
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    # ------------------------------------------------------------------------------------------------------------------
    def get_alerts(self, platform:str=Platforms.PC) -> Optional[dict]:
        """
        Gets the descriptions and rewards for alerts

        Args:
            platform (str): A platform for which you want the alerts. Defaults to 'pc'.

        Returns:
            Optional[dict]: A json object containing the alert data
        """
        endpoint = f'/{platform}/alerts/'
        url = ''.join([self.base_url, endpoint])

        response = self.client.get(
            url=url,
        )

        if response.status_code != WarframeClient.SUCESS:
            self.errors = response.json()
            return None
        
        return response.json()
    
    # ------------------------------------------------------------------------------------------------------------------
    def get_baro(self, platform:str=Platforms.PC) -> Optional[dict]:
        """
        Gets information on the current Void Trader offerings, or when he will arrive.

        Args:
            platform (str, optional): A platform for which you want Baro's details. Defaults to Platforms.PC.

        Returns:
            Optional[dict]: A json object containing the alert data
        """
        endpoint = f'/{platform}/voidTrader/'
        url = ''.join([self.base_url, endpoint])

        response = self.client.get(
            url=url,
        )

        if response.status_code != WarframeClient.SUCESS:
            self.errors = response.json()
            return None
        
        return response.json()
    
    # ------------------------------------------------------------------------------------------------------------------
    def get_orb_vallis_status(self, platform:str=Platforms.PC) -> Optional[dict]:
        """
        Gets The current cycle of the Orb Vallis warm/cold cycle

        Args:
            platform (str, optional): A platform for which you want the cycle status. Defaults to Platforms.PC.

        Returns:
            Optional[dict]: A json object containing the cycle data
        """
        endpoint = f'/{platform}/vallisCycle/'
        url = ''.join([self.base_url, endpoint])

        response = self.client.get(
            url=url,
        )

        if response.status_code != WarframeClient.SUCESS:
            self.errors = response.json()
            return None
        
        return response.json()
    
    # ------------------------------------------------------------------------------------------------------------------
    def get_cetus_status(self, platform:str=Platforms.PC):
        endpoint = f'/{platform}/cetusCycle/'
        url = ''.join([self.base_url, endpoint])

        response = self.client.get(
            url=url,
        )

        if response.status_code != WarframeClient.SUCESS:
            self.errors = response.json()
            return None
        
        return response.json()
   
    # ------------------------------------------------------------------------------------------------------------------
    def get_cambion_drift_status(self, platform:str=Platforms.PC) -> Optional[dict]:
        endpoint = f'/{platform}/cambionCycle/'
        url = ''.join([self.base_url, endpoint])

        response = self.client.get(
            url=url,
        )

        if response.status_code != WarframeClient.SUCESS:
            self.errors = response.json()
            return None
        
        return response.json()
   
    # ------------------------------------------------------------------------------------------------------------------
    def get_warframe(self, warframe:str, only:str='components,name,polarities,aura,masteryReq,releaseDate') -> Optional[dict]:
        endpoint = f'/warframes/search/{warframe}/'
        url = ''.join([self.base_url, endpoint])
        params = {
            'only': only,
        }

        response = self.client.get(
            url=url,
            params=params,
        )

        if response.status_code != WarframeClient.SUCESS:
            self.errors = response.json()
            return None
        
        return response.json()


if __name__ == '__main__':
    with WarframeClient() as client:
        pprint(client.get_warframe('yareli')[0])
        pprint(client.get_alerts())
        pprint(client.get_baro())
        pprint(client.get_orb_vallis_status())
        pprint(client.get_cetus_status())
        pprint(client.get_cambion_drift_status())