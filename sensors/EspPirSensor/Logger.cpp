#include "Logger.h"
#include <cstdarg>

using namespace ::hswro::esppirsensor;

Logger::Logger(HardwareSerial &hardwareSerial):
    hardwareSerial(hardwareSerial)
{
    hardwareSerial.begin(DEBUG_CONSOLE_BAUD);
}

void Logger::debug(const char *format, ...) const
{
    va_list args;
    va_start(args, format);
    formatLog("DBG/", format, args);
    va_end(args);
}

void Logger::info(const char *format, ...) const
{
    va_list args;
    va_start(args, format);
    formatLog("INF/", format, args);
    va_end(args);
}

void Logger::warning(const char *format, ...) const
{
    va_list args;
    va_start(args, format);
    formatLog("WRN/", format, args);
    va_end(args);
}

void Logger::error(const char *format, ...) const
{
    va_list args;
    va_start(args, format);
    formatLog("ERR/", format, args);
    va_end(args);
}

void Logger::flush() const
{
    hardwareSerial.flush();
}

void Logger::formatLog(const char *level, const char *format, va_list args) const
{
    char newFormat[128];
    /* This is the least crappy solution I came up with at 23:40 after a beer.
     * sstream is not available on this platform.
     * CAN YOU SPOT THE BUG? */
    snprintf(newFormat, sizeof(newFormat), "%s%s\n", level, format);

    char buffer[256];
    vsnprintf(buffer, sizeof(buffer), newFormat, args);
    hardwareSerial.print(buffer);
}
