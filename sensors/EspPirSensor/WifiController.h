#ifndef WIFICONTROLLER_H
#define WIFICONTROLLER_H
#include <string>
#include <ESP8266WiFiMulti.h>

namespace hswro { namespace esppirsensor {

class WifiController
{
public:

    /* The underlying driver is so crappy it doesn't even support disconnection from AP for power saving */
    WifiController();
    bool addAP(const std::string& ssid, const std::string& psk);
    bool isConnected();

private:
    ESP8266WiFiMulti wifiDriver;
};
}}

#endif // WIFICONTROLLER_H
