#include "WifiController.h"

using namespace ::hswro::esppirsensor;

WifiController::WifiController()
{
}

bool WifiController::addAP(const std::string &ssid, const std::string &psk)
{
    return wifiDriver.addAP(ssid.c_str(), psk.c_str());
}

bool WifiController::isConnected()
{
    return wifiDriver.run() == WL_CONNECTED;
}
