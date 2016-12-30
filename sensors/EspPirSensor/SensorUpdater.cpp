#include "SensorUpdater.h"
#include <ESP8266HTTPClient.h>

using namespace ::hswro::esppirsensor;
class HTTPClient;

SensorUpdater::SensorUpdater(const std::string &hostName, const std::string &sensorName, const Logger &logger):
    sensorUrl(createSensorUrl(hostName, sensorName)),
    logger(logger)
{
}

SensorUpdater::Status SensorUpdater::update(const std::string& value) const
{
    HTTPClient httpClient;

    logger.debug("%s: begin, url=%s", __PRETTY_FUNCTION__, sensorUrl.c_str());
    httpClient.begin(sensorUrl.c_str());

    const std::string message = createValueMessage(value);
    logger.debug("%s: POST, message=%s", __PRETTY_FUNCTION__, message.c_str());
    int postResultCode = httpClient.POST(message.c_str());

    httpClient.end();

    return checkReturnCode(postResultCode);
}

std::string SensorUpdater::createSensorUrl(const std::string &hostName, const std::string &sensorName)
{
    return "http://" + hostName + "/api/v1/sensor/" + sensorName;
}

//TODO: Implement variant type for int, float and string to support full JSON semantics
std::string SensorUpdater::createValueMessage(const std::string &value)
{
    return  "{ \"state\": \"" + value +"\" }";
}

SensorUpdater::Status SensorUpdater::checkReturnCode(int httpResultCode) const
{
    if(httpResultCode > 0) {
        if(httpResultCode == HTTP_CODE_OK) {
            logger.info("%s: Request OK", __PRETTY_FUNCTION__);
            return Status::OK;
        }
        else
        {
            logger.error("%s: HTTP error: %s", __PRETTY_FUNCTION__, HTTPClient::errorToString(httpResultCode).c_str());
            return Status::HttpError;
        }
    } else {
        logger.error("%s: Connection error: %s\n", __PRETTY_FUNCTION__, HTTPClient::errorToString(httpResultCode).c_str());
        return Status::ConnectionError;
    }
}
