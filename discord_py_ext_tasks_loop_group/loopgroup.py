from discord.ext.tasks import Loop
from discord.utils import MISSING
from collections.abc import Sequence
from typing import Union, Optional
from datetime import time as dt_time
from asyncio import AbstractEventLoop


class LoopGroup:
    def __init__(self):
        self.loops = []
    
    def loop(self, *,
        seconds: float = MISSING,
        minutes: float = MISSING,
        hours: float = MISSING,
        time: Union[dt_time, Sequence[dt_time]] = MISSING,
        count: Optional[int] = None,
        reconnect: bool = True,
        loop: Optional[AbstractEventLoop] = None,
        
        name: str = '',
        args: Union[tuple, list] = (),
        kwargs: dict = {}
    ):
        if not isinstance(name, str):
            raise TypeError('name type must be str not %s' % name.__class__.__name__)
        
        if not any([isinstance(args, list), isinstance(args, tuple)]):
            raise TypeError('args type must be list or tuple not %s' % args.__class__.__name__)
        
        if not isinstance(kwargs, dict):
            raise TypeError('kwargs type must be dict not %s' % kwargs.__class__.__name__)
            
        def decorator(func):
            _kwargs = {
                'seconds': seconds,
                'minutes': minutes,
                'hours': hours,
                'count': count,
                'time': time,
                'reconnect': reconnect,
                'loop': loop,
            }
            
            # [loop, args, kwargs, name]
            l = Loop(func, **_kwargs)
            self.loops.append([l, args, kwargs, (name if not name == '' else func.__name__)])
            return l
        return decorator
    
    def start(self):
        result = []
        for loop in self.loops:
            loop[0].start(*loop[1], **loop[2])
            result.append(loop[0]._task)
        
        return tuple(result)
    
    def stop(self):
        for loop in self.loops:
            loop[0].stop()
    
    def setargs(self, name: str, *args):
        if not isinstance(name, str):
            raise TypeError('name type must be str not %s' % name.__class__.__name__)
        
        for index, loop in enumerate(self.loops):
            if loop[3] == name:
                self.loops[index][1] = args
                return
    
    def setkwargs(self, name: str, **kwargs):
        if not isinstance(name, str):
            raise TypeError('name type must be str not %s' % name.__class__.__name__)
            
        for index, loop in enumerate(self.loops):
            if loop[3] == name:
                self.loops[index][2] = kwargs
                return
    
    def find(self, name: str):
        if not isinstance(name, str):
            raise TypeError('name type must be str not %s' % name.__class__.__name__)
            
        for loop in self.loops:
            if loop[3] == name:
                return loop
    
    def findall(self, name: str):
        if not isinstance(name, str):
            raise TypeError('name type must be str not %s' % name.__class__.__name__)
            
        result = []
        for loop in self.loops:
            if loop[3] == name:
                result.append(loop)
        
        return tuple(result)
