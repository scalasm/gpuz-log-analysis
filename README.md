# gpuz-log-analysis
Analyzing GPU-Z logs to troubleshoot my Geforce crashes

# Create your virtual environment

```
mario@Sharkey:~/src/data-science/gpuz-charts$ python -m venv venv/datascience_env
mario@Sharkey:~/src/data-science/gpuz-charts$ source venv/datascience_env/bin/activate
(datascience_env) mario@Sharkey:~/src/data-science/gpuz-charts$ pipenv install
...
```

Now open the project folder with your Visual Studio Code.

# Compress data files

```
zip -9 -r gpuz_sensor_log.zip gpuz_sensor_log.txt
```