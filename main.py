import os
import platform
from application.logic import IndexLogic
from application.config.ServerConfig import ServerConfig
from asgiref.wsgi import WsgiToAsgi
from application import app

# 将app转换为asgi
asgi_app: WsgiToAsgi = WsgiToAsgi(app)


# 定义启动命令
command: str = (f"hypercorn main:asgi_app --log-level debug -b {ServerConfig.host}:{ServerConfig.port} -w "
                f"{ServerConfig.workers}")

if __name__ == "__main__":
    with app.app_context():
        # 创建超级用户及其角色
        IndexLogic.create_admin_user()

    # 如果系统是windows，则使用flask自带的服务器启动
    if platform.system().lower() == "windows":
        app.run(host=ServerConfig.host, port=ServerConfig.port, workers=ServerConfig.workers, debug=True)
    else:
        # 启动hypercorn服务器
        os.system(command=command)
