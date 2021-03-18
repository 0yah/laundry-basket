### Laundry Basket

This system offers On-demand Laundry services.It is built with pure django

### Windows Setup
https://docs.djangoproject.com/en/3.1/ref/contrib/gis/install/#windows

https://get.enterprisedb.com/postgresql/postgresql-13.2-1-windows-x64.exe

http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86_64.exe 

```python

if os.name == 'nt':
    import platform
    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

```

TODO: Containerize the django app