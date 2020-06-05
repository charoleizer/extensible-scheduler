import sys
import os.path
import asyncio
import aioschedule as schedule

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)


async def Extension1Method():
    print("Invocando método [2]")
    # Aqui você implementa a regra de validação que deseja
    # Implemente também uma condição se o retorno deve ou não ser enviado
    # Lembrando que o retorno pode ser negativo ou positivo


schedule.every(5).seconds.do(Extension1Method)
loop = asyncio.get_event_loop()

# É possivel testar o seu agendamento direto por aqui
# loop.run_until_complete(schedule.run_pending())
# time.sleep(1)
