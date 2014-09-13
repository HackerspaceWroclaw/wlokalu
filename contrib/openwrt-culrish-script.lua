#!/usr/bin/env lua

--[[
    Curl-ish script for OpenWRT written in lua.
    Uses "nixio" library - POSIX sockets for lua.

    Copyleft, written by Lucy for HS:Wro
]]--

-- Arguments
local argv = {...}

-- If not enough args, print help
if #argv < 2 then
    print("Usage: curl.lua <method> <address> [data] [debug|quiet|normal]")
    print("Examples of use:")
    print("  curl.lua GET http://foo.example.com/api/v1/add_user")
    print("  curl.lua POST http://wobble.wibble.org/api.php debug")
    print("  curl.lua POST http://wobble.wibble.org/api.php key=abcd&data=Foo%20Bar quiet")
    print("  curl.lua POST http://wobble.wibble.org/api.php debug normal")
    print("The last example sends 'debug' as data. If 'normal' would not be specified,\nthe script would print debug output instead.")
    return 1
end

------------------------------------------------------------------------------
-- Local helper functions
------------------------------------------------------------------------------

--- Check if var is one of modes
function isMode(var)
    for _,v in pairs({'debug', 'normal', 'quiet'}) do
        if v == var then return true end
    end
    return false
end

--- Split URL into four fragments
function splitURL(url)
    local proto, target, path = url:match('^(%a+)://([%w.:-]+)(.*)$')
    if proto == nil then
        return nil
    end

    local host, port = target:match('^([%w.-]+):(%d+)$')
    if host == nil then
        host = target
        port = 80
    end

    if path == "" then
        path = "/"
    end

    return proto, host, port, path
end

-- Prepare HTTP request, with headers, body and all the good stuff
function httpRequest(method, path, headers, content)
    if headers == nil then
        headers = {}
    end

    request = method .. " " .. path .. " HTTP/1.1\r\n"
    for name, value in pairs(headers) do
        request = request .. name .. ": " .. value .. "\r\n"
    end

    if content == nil or content == "" then
        request = request .. "\r\n"
    else
        request = request .. "Content-Length: " .. content:len() .. "\r\n\r\n"
        request = request .. content
    end

    return request
end

function nixioSend(host, port, data)
    -- OpenWrt-specific library
    require "nixio"

    local socket = nixio.connect(host, port)
    socket:write(data)
    response = socket:read(1024)
    socket:close()

    return response
end

------------------------------------------------------------------------------
-- Script's body
------------------------------------------------------------------------------

-- Parse arguments
local proto, host, port, path = splitURL(argv[2])
local method = tostring(argv[1])
local data   = tostring(argv[3] or "")
local mode   = tostring(argv[4] or "")

-- If there is no mode specified, and data is mode, replace data with mode
if mode == "" and isMode(data) then
    mode = data
    data = ""
end

-- Prepare request to send
local headers = {
    ["User-Agent"] = "luaTool/1.0",
    ["Host"] = host,
    ["Content-Type"] = "application/x-www-form-urlencoded",
}
local request = httpRequest(method, path, headers, data)

if mode == "debug" then
    print(request)
end

response = nixioSend(host, port, request)

if mode ~= "quiet" then
    print(response)
end

return 0

------------------------------------------------------------------------------
-- vim:ft=lua
