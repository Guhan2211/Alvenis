#include "ESP8266WiFi.h"
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include "ThingSpeak.h"

// WiFi parameters to be configured
const char* ssid = "***";
const char* password = "**";
int RXPin = 4;
int TXPin = 5;
int GPSBaud = 9600;

unsigned long myChannelNumber = 600627;
const char * myWriteAPIKey = "V*****Q";


WiFiClient  client;
TinyGPSPlus gps;
SoftwareSerial gpsSerial(RXPin, TXPin);

void setup(void)
{ 
  Serial.begin(9600);
  gpsSerial.begin(GPSBaud);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
     delay(500);
     Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
  ThingSpeak.begin(client);
  

  

}
void loop() {
 
  while (gpsSerial.available() > 0)
    if (gps.encode(gpsSerial.read()))
      displayInfo();

  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println("No GPS detected");
    while(true);
  }
}

void displayInfo()
{
  if (gps.location.isValid())
  {
    Serial.print("Latitude: ");
    Serial.println(gps.location.lat(), 6);
    Serial.print("Longitude: ");
    Serial.println(gps.location.lng(), 6);

  //uploading stuff


  
    double latitude = (gps.location.lat());
    double longitude = (gps.location.lng());
    
    String latbuf=String(latitude,6);
    String lonbuf=String(longitude,6);
    
          
                        ThingSpeak.setField(1, latbuf);
                        ThingSpeak.setField(2, lonbuf);
                        int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
                        if(x == 200){
                            Serial.println("Channel update successful.");
                                      }
                        else{
                            Serial.println("Problem updating channel. HTTP error code " + String(x));
                             }
                                                         
  
       
       
  }
 

 else
  {
    Serial.println("Location: Not Available");
  }
      delay(10000);
      Serial.println();
  }
 
  
 



