#from prometheus_client import start_http_server, Summary
import prometheus_client as prom
import random, time, os, subprocess
from dotenv import load_dotenv

load_dotenv(verbose=True)

req_summary = prom.Summary('control_user', 'Controler les utilisateur se connectant')

@req_summary.time()
def process_request(t):
   time.sleep(t)


def getNumberUsers(cmd):
    returned_output = subprocess.check_output(cmd)
    returned_output = returned_output.decode("utf-8").split("\n")[0]
    returned_output = returned_output.split('u')
    number = returned_output[1][len(returned_output[1]) - 2]
    return number

def getListUsers(cmd):
    tabName = []
    tab = subprocess.check_output(cmd).decode("utf-8").split('\n')
    for i in range(2, len(tab) - 1):
        name = tab[i].split('  ')[0]
        tabName.append(name)
    return tabName



if __name__ == '__main__':
   
   counter = prom.Counter('up_time', 'temps de connexion de la machine')
   gauge = prom.Gauge('number_users_connect', 'Le nombre utilisateur connecte')
   histogram = prom.Histogram('python_my_histogram', 'This is my histogram')
   summary = prom.Summary('list_of_users_connect', 'La liste des utilisateurs connecte')

   prom.start_http_server(int(os.getenv("PORT_METRIC")))

   cmd = "w"
   
   liste = getListUsers(cmd)


   print("server start on 8081")
  
   while True:
    #num = getNumberUsers(cmd)
      #print(str(num))
      counter.inc(random.random())
      gauge.set(str(getNumberUsers(cmd))) #random.random() * 15 - 
      histogram.observe(random.random() * 10)
      summary.observe(random.random() * 10)
      process_request(random.random() * 5)

      time.sleep(1)
      