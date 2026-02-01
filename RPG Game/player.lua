local Player = {}
Player.__index = Player

function Player.new(x, y)
    local self = setmetatable({}, Player)
    self.x = x
    self.y = y
    self.speed = 120
    self.size = 30
    self.sprite = love.graphics.newImage("Hungry-dino 2.png")
    -- Scale sprite to roughly match the existing collision size
    local maxDim = math.max(self.sprite:getWidth(), self.sprite:getHeight())
    self.spriteScale = self.size / maxDim
    return self
end

function Player:update(dt, map)
    local moveX, moveY = 0, 0

    -- Input handling
    if love.keyboard.isDown("w", "up") then moveY = -1 end
    if love.keyboard.isDown("s", "down") then moveY = 1 end
    if love.keyboard.isDown("a", "left") then moveX = -1 end
    if love.keyboard.isDown("d", "right") then moveX = 1 end

    -- Normalize diagonal movement
    if moveX ~= 0 and moveY ~= 0 then
        moveX = moveX * 0.7071
        moveY = moveY * 0.7071
    end

    -- Proposed movement
    local newX = self.x + moveX * self.speed * dt
    local newY = self.y + moveY * self.speed * dt

    -- Check collision separately on X and Y
    if not map:collides(newX, self.y, self.size) then
        self.x = newX
    end
    if not map:collides(self.x, newY, self.size) then
        self.y = newY
    end
end

function Player:draw()
    love.graphics.setColor(1,1,1)
    love.graphics.draw(
        self.sprite,
        self.x,
        self.y,
        0,
        self.spriteScale,
        self.spriteScale,
        self.sprite:getWidth()/2,
        self.sprite:getHeight()/2
    )
end

return Player