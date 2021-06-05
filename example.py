from discord_py_ext_tasks_loop_group import LoopGroup

loops = LoopGroup()


####################

" 基本的な使い方 "

@loops.loop(hours=1)
async def loop():
    print('１時間経過')

loops.start()

####################

" 複数のループを定義 "

@loops.loop(hours=1)
async def loop():
    print('１時間経過')

@loops.loop(hours=24)
async def loop():
    print('２４時間経過')

loops.start()

####################

" ループに名称をつける "

@loops.loop(hours=1, name='1hourloop')
async def loop():
    print('1hourloop: １時間経過')

loops.start()

####################

" before_loop, after_loop, errorを設定 "

@loops.loop(hours=1)
async def loop():
    print('１時間経過')

@loop.before_loop
async def before_loop():
    print('before')

@loop.after_loop
async def after_loop():
    print('after')

@loop.error
async def error_loop():
    print('error')

loops.start()

####################

" argsを設定 (1/3) "

@loops.loop(hours=1, args=['first arg', 'second arg'])
async def loop(f_arg, s_arg):
    print('1hourloop:', f_arg, s_arg)

loops.start()


" argsを設定 (2/3) "

@loops.loop(hours=1)
async def loop(f_arg, s_arg):
    print('1hourloop:', f_arg, s_arg)

loops.setargs('loop', 'first arg', 'second arg')

loops.start()


" argsを設定 (3/3) "

@loops.loop(hours=1, name='1hourloop')
async def loop(f_arg, s_arg):
    print('1hourloop:', f_arg, s_arg)

loops.setargs('1hourloop', 'first arg', 'second arg')

loops.start()

####################

" kwargsを設定 (1/3) "

@loops.loop(hours=1, kwargs=dict(f_kwarg='first kwarg', s_kwarg='second kwarg'))
async def loop(*, f_kwarg, s_kwarg):
    print('1hourloop:', f_kwarg, s_kwarg)

loops.start()


" kwargsを設定 (2/3) "

@loops.loop(hours=1)
async def loop(*, f_kwarg, s_kwarg):
    print('1hourloop:', f_kwarg, s_kwarg)

loops.setkwargs('loop', f_kwarg='first kwarg', s_kwarg='second kwarg')

loops.start()


" kwargsを設定 (3/3) "

@loops.loop(hours=1, name='1hourloop')
async def loop(*, f_kwarg, s_kwarg):
    print('1hourloop:', f_kwarg, s_kwarg)

loops.setkwargs('1hourloop', f_kwarg='first kwarg', s_kwarg='second kwarg')

loops.start()

####################

" 要素を検索 (1/2) "

@loops.loop(hours=1)
async def loop():
    print('１時間経過')

loops.find('loop')


" 要素を検索 (2/2) "

@loops.loop(hours=1, name='1hourloop')
async def loop():
    print('１時間経過')

loops.find('1hourloop')

####################

" すべての要素を検索 (1/2) "

@loops.loop(hours=1)
async def loop():
    print('１時間経過')

@loops.loop(hours=1)
async def loop():
    print('１時間経過')

@loops.loop(hours=1)
async def loop_():
    print('１時間経過')

loops.findall('loop')


" すべての要素を検索 (2/2) "

@loops.loop(hours=1, name='1hourloop')
async def loop():
    print('１時間経過')

@loops.loop(hours=1, name='1hourloop')
async def loop():
    print('１時間経過')

@loops.loop(hours=1)
async def loop():
    print('１時間経過')


loops.findall('1hourloop')
