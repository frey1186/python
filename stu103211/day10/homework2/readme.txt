使用rpc的方式实现服务器和客户端之间的执行命令
以下为使用方法：
【client】
C:\Users\Administrator>python rpc_client.py init 0
 [x] Requesting fib(init 0 )
 [.] exce failed...

C:\Users\Administrator>python rpc_client.py type rpc_client.py
 [x] Requesting fib(type rpc_client.py )
 [.] exce done...

C:\Users\Administrator>


【server】
C:\Users\Administrator>python rpc_server.py
 [x] Awaiting RPC requests
 [.] command: init 0
'init' 不是内部或外部命令，也不是可运行的程序或批处理文件。
 [.] command: type rpc_client.py
import pika
import uuid
...

