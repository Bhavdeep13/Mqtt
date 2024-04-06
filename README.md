# MQTT protocol using Python
Simple pub-sub mechanism using MQTT protocol in python 
Technoloies used
- Paho (MQTT client library)
- MQTT broker (test.mosquitto.org)
- Smart sensors  (Publisher) (temperature, humidity, and CO2 concentration)
- Monitoring system  (Subscriber)



## Create Virtual Env

```bash
#using venv
pip install virtualenv
python<version> -m venv <virtual-environment-name>

source env/bin/activate

#or Using conda
conda create -n <virtual-environment-name> python=<version>

conda activate <virtual-environment-name>
conda deactivate

```


## Install Requirements

```bash
pip install <package name>

python==3.9.13
paho-mqtt==1.6.1

or

pip install -r requirements.txt

``` 

## Run code
- create virtual env
- activate virtual env
- intall dependecies
- run sub.py (python sub.py)
- run pub.py (python pub.py)




