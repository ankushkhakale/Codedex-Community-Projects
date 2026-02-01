local Player = require("player")
local Map = require("map")

function love.load()
    love.window.setTitle("RPG Game")
    love.window.setMode(320, 288)
    
    player = Player.new(160, 144)
    map = Map.new()
end

function love.update(dt)
    player:update(dt, map)
end

function love.draw()
    love.graphics.setColor(0.2, 0.2, 0.2)
    love.graphics.rectangle("fill", 0, 0, love.graphics.getWidth(), love.graphics.getHeight())
    
    map:draw()
    player:draw()
end

function love.keypressed(key)
    if key == "escape" then
        love.event.quit()
    end
end