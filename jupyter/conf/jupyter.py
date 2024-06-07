import os
c = get_config()
# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook
# Notebook config
c.NotebookApp.notebook_dir = 'nbs'
c.NotebookApp.allow_origin = u'https://inprof-chat.web.app/' # put your public IP Address here
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
# ipython -c "from notebook.auth import passwd; passwd()" - deprecated
# ipython -c "from jupyter_server.auth import passwd; passwd()"
# python -c "from jupyter_server.auth import passwd; print(passwd())"
c.NotebookApp.password = u"argon2:$argon2id$v=19$m=10240,t=10,p=8$qa9V8SvxCARkbxzSj1v/iQ$L/6I8jBgD2l3JoT10s56wUCmo7eM11g6w6rBFbTbCQY"
c.NotebookApp.port = int(os.environ.get("PORT", 8888))
c.NotebookApp.allow_root = True
c.NotebookApp.allow_password_change = True
c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--redirect-port', '80']
c.JupyterHub.db_url = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@postgres:5432/{os.environ['POSTGRES_DB']}"
