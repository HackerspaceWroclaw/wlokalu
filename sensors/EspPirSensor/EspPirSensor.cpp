#include "EspPirSensor.h"
#include "Helpers.h"

using namespace ::hswro::esppirsensor;

EspPirSensor::EspPirSensor(const Configuration& configuration, const Logger& logger):
    configuration(configuration),
    logger(logger),
    pirSensorUpdater(configuration.hostname, configuration.sensorName, logger),
    pirSensor(configuration.pinNumber)
{
    for(uint8_t t = 4; t > 0; t--) {
        logger.info("%s: WAIT %d...", __PRETTY_FUNCTION__, t);
        logger.flush();
        delay(1000);
    }

    wifiController.addAP(configuration.essid, configuration.psk);
}

void EspPirSensor::run()
{
    logger.info("%s: Starting polling.", __PRETTY_FUNCTION__);
    for(;;)
    {
        pushUpdateOverWifi();
        performPolling();
    }
}

void EspPirSensor::performPolling()
{
    for(auto sampleIndex = 0U; sampleIndex < SAMPLES_PER_PERIOD; ++sampleIndex)
    {
        pirSensor.poll();
        delay(SAMPLE_DELAY_MS);
    }
}

void EspPirSensor::pushUpdateOverWifi()
{
    if(wifiController.isConnected()) {
        auto pulsesInLastPeriod = pirSensor.getAndClearPulseCount();

        logger.debug("%s: Wifi connected, sending update, %u pulses.", __PRETTY_FUNCTION__, pulsesInLastPeriod);
        if(pulsesInLastPeriod > 0)
            pirSensorUpdater.update("Ruch: " + helpers::toString(pulsesInLastPeriod) + " imp/min");
        else
            pirSensorUpdater.update("Brak ruchu");
    }
    else
    {
        logger.warning("%s: Wifi not connected, skipping update!", __PRETTY_FUNCTION__);
    }
    yield();
}
