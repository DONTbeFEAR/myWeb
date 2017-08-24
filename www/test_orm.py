from model import User
import asyncio
import orm
import pdb
import time

@asyncio.coroutine
def test_save(loop):
	yield from orm.create_pool(loop,user='www-data',password='www-data',db='awesome')
	u = User(name='hi',email = 'hi@example.com',
			passwd= 'password',image='about:blank')
	yield from u.save()
if __name__=="__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_save(loop))
        __pool=orm.__pool
        __pool.close()
        loop.run_until_complete(__pool.wait_closed())
        loop.close()
