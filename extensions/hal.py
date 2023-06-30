import asyncio
from interactions import slash_command, slash_option, OptionType, SlashContext, Extension
from characterai import PyAsyncCAI

file = open(file="tokens/caiToken.txt", mode="r", encoding="utf-8")
token = file.read()
file.close()


class hal(Extension):
    @slash_command(name="hal", description="Talk to HAL9000")
    @slash_option(name="message", 
                  description='',
                  opt_type=OptionType.STRING, 
                  required=True)
    
    async def hal(self, ctx: SlashContext, message: str):
        async def hal_backend():
            cai_client = PyAsyncCAI(token)
            await cai_client.start()
            
            char = "bXFRSGkcr0gP3-udUZNWk-JvOr7nfemTFQAfxjUSFjM" # Establish connection to HAL9000
            chat = await cai_client.chat.get_chat(char)
            history_id = chat['external_id']
            participants = chat['participants']
            
            if not participants[0]['is_human']:
                tgt = participants[0]['user']['username']
            else:
                tgt = participants[1]['user']['username']

            while True:
                data = await cai_client.chat.send_message(char, message, history_external_id=history_id, tgt=tgt)
                name = data['src_char']['participant']['name']
                text = data['replies'][0]['text']

                cai_response = f"**{name}:**  `{text}`"
                await asyncio.sleep(5)
                print(cai_response)
                return cai_response  # Return the response from hal_backend
            
        await ctx.defer()
        
        response = await hal_backend()  # Store the response in a variable
        await ctx.send(response)
    
def setup(bot):
    hal(bot)