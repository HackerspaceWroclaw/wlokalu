#include "EspPirSensor.h"
#include "Logger.h"

using namespace ::hswro::esppirsensor;

void setup()
{
    EspPirSensor::Configuration defaultConfiguration;
    defaultConfiguration.essid = "SSID";
    defaultConfiguration.psk = "";
    defaultConfiguration.hostname = "example.hostname.org";
    defaultConfiguration.sensorName = "PIR";
    defaultConfiguration.pinNumber = 15U;

    Logger logger(Serial);
    EspPirSensor(defaultConfiguration, logger).run();
}

void loop()
{}
