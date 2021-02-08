# gpuz-log-analysis
Analyzing GPU-Z logs to troubleshoot my Geforce crashes

# Create your virtual environment

```
mario@Sharkey:~/src/data-science/gpuz-charts$ python -m venv datascience_env
mario@Sharkey:~/src/data-science/gpuz-charts$ source ./datascience_env/bin/activate
(datascience_env) mario@Sharkey:~/src/data-science/gpuz-charts$ pip install pandas matplotlib numpy ipykernel
...
...
```

Now open the project folder with your Visual Studio Code.

# Compress data files

```
zip -9 -r gpuz_sensor_log.zip gpuz_sensor_log.txt
```