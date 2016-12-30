#ifndef ESPPIRSENSOR_H
#define ESPPIRSENSOR_H

#include <string>
#include <atomic>
#include "WifiController.h"
#include "Logger.h"
#include "SensorUpdater.h"
#include "PirSensor.h"

namespace hswro { namespace esppirsensor {

class EspPirSensor
{
public:
    struct Configuration
    {
        std::string essid;
        std::string psk;
        std::string hostname;
        std::string sensorName;
        unsigned int pinNumber;
    };

    explicit EspPirSensor(const Configuration& configuration, const Logger& logger);
    void run();

private:
    enum {
        SAMPLE_DELAY_MS = 500,
        SAMPLES_PER_PERIOD = 120
    };

    void performPolling();
    void pushUpdateOverWifi();

    const Configuration& configuration;
    const Logger& logger;
    const SensorUpdater pirSensorUpdater;
    PirSensor pirSensor;
    WifiController wifiController;
};

}}

#endif // ESPPIRSENSOR_H
