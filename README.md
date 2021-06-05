# [d.py-ext-tasks-loop-group](https://github.com/Req-kun/d.py-ext-tasks-loop-group)

このパッケージは、discord.pyで使用可能なtasks.loopをまとめて実行できるようにしたものです。  
また、ループには同じ関数名を使用することができます。  
引数は`tasks.loop`と同じように指定できます。  
`args`、`kwargs`を指定することができます。  
`tasks.loop`の一部メソッドも使用可能です。(例: before_loop)


## install

※現在はこの方法でのみインストールできます  

```sh
$ git clone https://github.com/Req-kun/d.py-ext-tasks-loop-group.git
$ cd d.py-ext-tasks-loop-group
$ python setup.py install
```

## Example

```py
from discord_py_ext_tasks_loop_group import LoopGroup
loopgroup = LoopGroup()

@loopgroup.loop(seconds=10.0)
async def loop():
    print('10 seconds loop')
```

## Reference

### class LoopGroup()

メインのクラス

```py
lg = LoopGroup()
```

##### Attributes
> loops (list)

##### Methods
> [@ loop](https://github.com/Req-kun/d.py-ext-tasks-loop-group#loopkwargs)  
[def start](https://github.com/Req-kun/d.py-ext-tasks-loop-group#start)  
[def stop](https://github.com/Req-kun/d.py-ext-tasks-loop-group#stop)  
[def setargs](https://github.com/Req-kun/d.py-ext-tasks-loop-group#setargsname-args)  
[def setkwargs](https://github.com/Req-kun/d.py-ext-tasks-loop-group#setkwargsname-kwargs)  
[def find](https://github.com/Req-kun/d.py-ext-tasks-loop-group#findname)  
[def findall](https://github.com/Req-kun/d.py-ext-tasks-loop-group#findallname)

#### loop(**kwargs)

ループを定義

```py
@lg.loop(*, seconds, minutes, hours, time, count, reconnect, loop, name, args, kwargs)
async def Loop(*args, **kwargs):
    ...
```

##### Parameters
・seconds ~ loop - View [here](https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html#discord.ext.tasks.loop)  
・name (Optional[str]) - ループの名前(指定されなかった場合は関数名が代用されます)  
・args (Optional[Union[list, tuple]]) - ループに設定するarg  
・kwargs (Optional[dict]) - ループに設定するkwarg

##### Raises
TypeError - name, args, kwargsのいずれかの型が間違っている

#### start()

設定されたループを開始

```py
lg.start()
```

##### Return Type
Tuple(asyncio.Task)

#### stop()

設定されたループを終了

```py
lg.stop()
```

#### setargs(name, *args)

ループにargsを追加

```py
lg.setargs(name, *args)
```

##### Parameters
・name (str) - 追加するループの名前  
・args (Any) - 追加するargs

##### Raises
TypeError - 渡されたパラメーターの型が間違っている

#### setkwargs(name, **kwargs)

ループにkwargsを追加

```py
lg.setkwargs(name, **kwargs)
```

##### Parameters
・name (str) - 追加するループの名前  
・kwargs (Any) - 追加するkwargs

##### Raises
TypeError - 渡されたパラメーターの型が間違っている

#### find(name)

ループのリストから名称が一致する一番先頭の要素を検索

```
lg.find(name)
```

##### Parameters
・name (str) - 検索する名称

##### Return Type
Optional[Tuple[discord.ext.tasks.Loop, args, kwargs, name]]

#### findall(name)

ループのリストから名称が一致するものをすべて検索

```
lg.findall(name)
```

##### Parameters
・name (str) - 検索する名称

##### Return Type
Tuple[Optional[Tuple[discord.ext.tasks.Loop, args, kwargs, name]]]
