#ifndef LOGGER_H
#define LOGGER_H

#include <Arduino.h>

class HardwareSerial;
namespace hswro { namespace esppirsensor {

class Logger
{
public:
    explicit Logger(HardwareSerial& hardwareSerial);

    void debug(const char *format, ...) const;
    void info(const char *format, ...) const;
    void warning(const char* format, ...) const;
    void error(const char* format, ...) const;

    void flush() const;

private:
    enum {
        DEBUG_CONSOLE_BAUD = 115200
    };

    void formatLog(const char* level, const char* format, va_list args) const;

    HardwareSerial& hardwareSerial;
};

}}
#endif // LOGGER_H
