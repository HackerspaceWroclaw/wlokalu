#ifndef SENSORUPDATER_H
#define SENSORUPDATER_H
#include <string>
#include "Logger.h"

namespace hswro { namespace esppirsensor {

class SensorUpdater
{
public:
    enum class Status
    {
        OK,
        ConnectionError,
        HttpError
    };

    SensorUpdater(const std::string& hostName, const std::string& sensorName, const Logger& logger);

    Status update(const std::string& value) const;
private:
    static std::string createSensorUrl(const std::string& hostName, const std::string& sensorName);
    static std::string createValueMessage(const std::string& value);
    Status checkReturnCode(int httpResultCode) const;

    const std::string sensorUrl;
    const Logger& logger;
};

}}

#endif // SENSORUPDATER_H
