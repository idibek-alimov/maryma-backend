import os,sys 
PWD = os.getenv('PWD')
PROJ_MISSING_MSG = """ Set an enviroment variable:/n 
 `DJANGO_PROJECT=myshop`/n
 or call:/n
 `init_django(your_project_name`
 """

def init_django(project_name=None):
    os.chdir(PWD)
    project_name = project_name or os.environ.get("DJANGO_PROJECT") or None
    if project_name == None :
        raise Exception(PROJ_MISSING_MSG)
    sys.path.insert(0,os.getenv("PWD"))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',f'{project_name}.settings')
    os.environ['DJANGO_ALLLOW_ASYNC_UNSAFE'] = 'true'
    import django 
    django.setup()