import aiohttp
from typing import Optional, Union
from . import __version__
from .enums import ApiVersion, RequestTypes, Routes

import platform
if int(platform.python_version().split('.')[1]) <= 8:
    from typing import Dict

class BaseHTTP:    
    __slots__ = ['id', 'ver']
    
    def __init__(self, id, api_ver: Optional[Union[ApiVersion, int]]):
        self.id = id
        self.ver = api_ver or ApiVersion.current
        self.user_agent = f"async_fateslist/{__version__}"       
    
    async def request(
        self, 
        method: RequestTypes, 
        endpoint: Routes,
        api_ver: Union[ApiVersion, int],
        json: Optional[dict], 
        headers: Optional[dict], 
        retry: bool = False
    ):
        """Makes a API request"""
        headers = {} if not headers else headers
                
        headers["Authorization"] = self.api_token
        headers["User-Agent"] = self.user_agent
        headers['FL-API-Version'] = self.ver if isinstance(self.var, int) else self.ver.value
        
        async with aiohttp.ClientSession() as session:
            async with sess.request(str(method).upper(), f'https://fateslist.xyz/api/{str(endpoint)}',headers=headers,json=json) as response:
                return await response
     
