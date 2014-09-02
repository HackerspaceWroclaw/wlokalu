#!/usr/bin/env lua

--[[
    Curl-ish script for OpenWRT written in lua.
    Uses "nixio" library - POSIX sockets for lua.
    
    Copyleft, written by Lucy for HS:Wro
]]--

require "nixio"

-- Arguments
local argv = {...}

-- If not enough args, print help
if #argv < 2 then
    print("Usage: <request-type> <address> [data] [debug|quiet|normal]")
    print('Address: Without "http://"')
    print("  Ex. GET foo.bar.buz.com/api/v1/add_user")
    print("  Ex. POST wobble.wibble.org/api.php debug")
    print("  Ex. POST wobble.wibble.org/api.php key=abcd&data=Foo%20Bar quiet")
    print("  Ex. POST wobble.wibble.org/api.php debug normal")
    print("  Example above sends 'debug' as data. If 'normal' would not be specified, it would print debug output instead.")
    return 1
end

-- Local API

--- Add string to buffer
function s(buffer, x)
    buffer = buffer .. x .. "\r\n"
end

--- Check if var is one of modes
function isMode(var)
    for _,v in pairs({'debug', 'normal', 'quiet'}) do
        if v == var then return true end
    end
    return false
end

--- Get path from string
function getPath(addr)
    local x = addr:find("/")
    return (x == nil and "/" or addr:sub(x, #addr))
end

-- Parse arguments
local address = tostring(argv[2])
local host    = address:sub(1, (address:find("/") or #address + 1) - 1)
local path    = getPath(address)
local request = tostring(argv[1])
local data    = tostring(argv[3] or "")
local mode    = tostring(argv[4] or "")

-- Start buffer
local buffer  = ""

-- If there is no mode specified, and data is mode, replace data with mode
if mode == "" and isMode(data) then
    mode = data
    data = ""
end

-- Add stuff to buffer
s(buffer, request.." "..path.." HTTP/1.1")
s(buffer, "User-Agent: luaTool/1.0")
s(buffer, "Host: "..host)
s(buffer, "Accept: */*")

-- If there is data to be sent, add data-specific stuff
if data ~= "" then
    s(buffer, "Content-Type: application/x-www-form-urlencoded")
    s(buffer, "Content-Length: "..#data)
end

-- Trailing empty line
s("")

-- Add data (if there is any)
if data ~= "" then
    s(data)
    s("")
end

-- Connect and send
local socket = nixio.connect(host, 80)
socket:write(buffer)

-- Debug
if mode == "debug" then
    print(buffer)
end

-- If not quiet, print response
if mode ~= "quiet" then
    print(socket:read(1024))
end

-- Disconnect, close
socket:close()
return 0