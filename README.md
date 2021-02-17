# gpuz-log-analysis
Analyzing GPU-Z logs to troubleshoot my Geforce crashes

# Create your virtual environment

```
mario@Sharkey:~/src/data-science/gpuz-log-analysis$ mkdir .venv && pipenv --python 3.8
mario@Sharkey:~/src/data-science/gpuz-log-analysis$ source .venv/bin/activate
(gpuz-log-analysis) mario@Sharkey:~/src/data-science/gpuz-log-analysis$ pipenv install --dev
...
```

Now open the project folder with your Visual Studio Code.

# Create your settings.json for VS Code

```json
{
    "python.venvPath": "${workspaceFolder}/.venv/bin/python",
    "python.pythonPath": ".venv/bin/python",
    "python.envFile": "${workspaceFolder}/.env",
    "python.analysis.autoSearchPaths": true,
    "python.testing.pytestArgs": [
        "test"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": true,
    "jupyter.jupyterServerType": "local"
}
```

# Compress data files

```
zip -9 -r gpuz_sensor_log.zip gpuz_sensor_log.txt
```