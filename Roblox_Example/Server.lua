local HttpsSerivce = game:GetService("HttpService")
local Server_Url = "https://discordtorobloxwebhook.herokuapp.com/" --Put your App_URL here. 
local Api_Key = "df0ef802efm2m8f2e-8f82e8f028mfe-" --API key we made here.
local Complete_Url = Server_Url.. "discord"


local function SendDiscord(DscMsg)
	local Req_Url = Complete_Url .."?Key=" ..Api_Key.. "&Message=" ..DscMsg
	print(Req_Url)
	local Request = HttpsSerivce:GetAsync(Req_Url)
	local data = HttpsSerivce:JSONDecode(Request)
end


SendDiscord("Hello from roblox!") --Send a message, customize by editing the string!