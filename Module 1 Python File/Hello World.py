import requests
import json
requests.packages.urllib3.disable_warnings() # Disable warnings
  
  
CONTROLLER_IP="devnetapi.cisco.com/sandbox/apic_em"
GET="get"
POST="post"
  
  
def getServiceTicket():
  ticket=None
  #specify the username and password which will be included in the data.  Replace ‘xxxx’ with 
  #your username and password
  payload = {"username":"devnetuser","password":"Cisco123!"}
  
  #This is the URL to get the service ticket.  
  #The base IP call is https://[Controller IP]/api/v1
  #The REST function is ‘ticket’
  url = "https://" + CONTROLLER_IP + "/api/v1/ticket"
  
  #Content type must be included in the header
  header = {"content-type": "application/json"}
  
  #Format the payload to JSON and add to the data.  Include the header in the call. 
  #SSL certification is turned off, but should be active in production environments
  response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
  
  #Check if a response was received. If not, print an error message.
  if(not response):
      print ("No data returned!")
  else:
      #Data received.  Get the ticket and print to screen.
      r_json=response.json()
      ticket = r_json["response"]["serviceTicket"]
      print ("ticket: ", ticket)
  return ticket
  
#Make the REST call using the service ticket, command, http url, data for the body (if any)
def doRestCall(aTicket,command,url,aData=None):
  response_json=None
  payload=None
  try:
  
      #if data for the body is passed in put into JSON format for the payload
      if(aData != None):
           payload=json.dumps(aData)
  
      #add the service ticket and content type to the header
      header = {"X-Auth-Token": aTicket, "content-type" : "application/json"}
      if(command==GET):
           r = requests.get(url, data=payload, headers=header, verify=False)
      elif(command==POST):
           r = requests.post(url, data=payload, headers=header, verify=False)
      else:
           #if the command is not GET or POST we don’t handle it.
           print ("Unknown command!")
           return
  
      #if no data is returned print a message; otherwise print data to the screen
      if(not r):
           print("No data returned!")
      else:
           print ("Returned status code: %d" % r.status_code)
  
           #put into dictionary format
           response_json = r.json()
           print(response_json)
  except:
      err = sys.exc_info()[0]
      msg_det = sys.exc_info()[1]
      print( "Error: %s  Details: %s StackTrace: %s" % 
(err,msg_det,traceback.format_exc()))
  
  
  
#the main function
def main():
      #Call the function to get the service ticket
      ticket=getServiceTicket()
  
      #If ticket received get the users
      if(ticket):
           #Get user types in the system
           doRestCall(ticket,GET, "https://" + CONTROLLER_IP + "/api/v1/user")
  
           #Create a new application
           doRestCall(ticket, POST, "https://" + CONTROLLER_IP + "/api/v1/topology/application",[{"id":"1","description":"cool app","name":"appABC"}])
      else:
           print("No service ticket was received.  Ending program!")
  
#Calls the main function to start the application
main()
