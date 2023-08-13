import disnake
from disnake.ext import commands

class Request(commands.Cog):
    @commands.slash_command(name="request", description="Запросы на веб-сервер")
    async def request_command(self, inter):
        ...

    @request_command.sub_command(name="get", description="Отправка GET-запроса")
    async def get_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

    @request_command.sub_command(name="post", description="Отправка POST-запроса")
    async def post_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

    @request_command.sub_command(name="delete", description="Отправка DELETE-запроса")
    async def delete_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

    @request_command.sub_command(name="put", description="Отправка PUT-запроса")
    async def put_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

    @request_command.sub_command(name="head", description="Отправка HEAD-запроса")
    async def head_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

    @request_command.sub_command(name="options", description="Отправка OPTIONS-запроса")
    async def options_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

    @request_command.sub_command(name="trace", description="Отпрака TRACE-запроса")
    async def trace_request_command(self, inter, url: str, *, headers: str = None, body: str = None):
        pass

def setup(bot):
    bot.add_cog(Request(bot))