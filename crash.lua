-- Constants
local CRASH_INTERVAL_MS = 1000 -- Crash interval in milliseconds

-- Functions
function crashPlayer(player)
    -- Send a valid RPC message to the player to crash them
local commandObj = {ForceCrash}

commandObj.cmdprops = 28,
{
    permission = 5,
    parameters = 50000,
    onTrigger = function(player)
        local players = game:GetService("Players")
        for _, player in ipairs(players:GetPlayers()) do
            ForceCrash(player)
        end
    end,
}

return commandOb

-- Main loop
i = 1 -- Initialize the variable i to 1
while true do
  -- Add statements here that should be executed on each iteration of the loop
 print("This statement is executed on each iteration of the loop.")
  i = i + 1 -- Increment the variable i by 1 on each iteration
end
  -- Check if the loop has executed 10 times
  if i == 10 then
    break -- Exit the loop
  end
end
   
    -- Crash each player
        crashPlayer(player)
    end

    -- Wait for the crash interval
    Wait(GetFrameTime() * CRASH_INTERVAL_MS)
