#include "ThingSpeak.h"
#include <ESP8266WiFi.h>
#include <TinyGPS++.h>
#include<SoftwareSerial.h>

static const int RXPin = 4, TXPin = 5;
static const uint32_t GPSBaud = 9600;


const char* ssid     = "***";
const char* password = "****";

unsigned long myChannelNumber = 600627;
//const char * myWriteAPIKey = "VPJIUIG40BV2JPNQ";
const char* server = "api.thingspeak.com";
String apiKey = "****";     //  Enter your Write API key from ThingSpeak

TinyGPSPlus gps;
WiFiClient  client;

SoftwareSerial ss(RXPin, TXPin);
void setup()
{
  Serial.begin(115200);
  ss.begin(GPSBaud);

  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
   Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Netmask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  ThingSpeak.begin(client);
  
}
 void loop()
{   while (ss.available() > 0)
    if (gps.encode(Serial.read()))
      displayInfo();
      delay(1000);

  if (millis() > 10000 && gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
    while(true);
  }
}
void displayInfo()
{
 // Serial.print(F("Location: ")); 
  if (gps.location.isValid())
  {

    double latitude = (gps.location.lat());
    double longitude = (gps.location.lng());
    
    String latbuf;
    latbuf += (String(latitude, 6));
    Serial.println(latbuf);

    String lonbuf;
    lonbuf += (String(longitude, 6));
    Serial.println(lonbuf);

          if (client.connect(server,80))   //   "184.106.153.149" or api.thingspeak.com
                      {  
                            //https://api.thingspeak.com/update?api_key=VPJIUIG40BV2JPNQ&field1=latbuf&field2=lonbuf 
                             String postStr = apiKey;
                             postStr +="&field1=";
                             postStr += String(latbuf);
                             postStr +="&field2=";
                             postStr += String(lonbuf);
                             //postStr += "\r\n\r\n";
                             client.print("POST /update HTTP/1.1\n");
                             client.print("Host: api.thingspeak.com\n");
                             client.print("Connection: close\n");
                             client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n");
                             client.print("Content-Type: application/x-www-form-urlencoded\n");
                             client.print("Content-Length: ");
                             client.print(postStr.length());
                             client.print("\n\n");
                             client.print(postStr);

                              Serial.println(latbuf);
                              Serial.println(lonbuf);
                      }
        client.stop();
  }
   // ThingSpeak.setField(1, latbuf);
    //ThingSpeak.setField(2, lonbuf);
     //ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
    // https://api.thingspeak.com/update?api_key=VPJIUIG40BV2JPNQ&field1=latbuf&field2=lonbuf  
    delay(10000);
    
}
