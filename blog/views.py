import asyncio

from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views import View


class TimerPageView(View):
    def get(self, request):
        return render(request, 'blog/timer.html')


class TimerStreamView(View):
    async def get(self, request):
        async def timer():
            for seconds in range(10, -1, -1):
                print(f'Cliente {id(request)} | Tempo restante: {seconds}')
                yield f'data: {seconds}\n\n'
                await asyncio.sleep(1)

            yield 'event: finished\n'
            yield 'data: Finalizado!\n\n'

        response = StreamingHttpResponse(
            timer(),
            content_type='text/event-stream',
        )
        response['Cache-Control'] = 'no-cache'
        response['X-Accel-Buffering'] = 'no'
        return response
