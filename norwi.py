import asyncio
import httpx
from googletrans import Translator
from httpx_curl_cffi import AsyncCurlTransport


import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext


async def translate(text):
    # Workaround for 429 errors (ssut/py-googletrans#457): swap googletrans' HTTP
    # transport for curl-cffi impersonating Chrome.
    translator = Translator(service_urls=['translate.googleapis.com'], raise_exception=True)
    original_client = translator.client
    translator.client = httpx.AsyncClient(
        transport=AsyncCurlTransport(impersonate='chrome', default_headers=True),
        headers={
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/140.0.0.0 Safari/537.36'
            ),
        },
    )
    # The TokenAcquirer was created with the original client.
    translator.token_acquirer.client = translator.client
    try:
        return await translator.translate(text, src='no', dest='en')
    finally:
        await translator.client.aclose()
        await original_client.aclose()


root = tk.Tk()
root.title('Norwi')
root.geometry('600x200')

style = ttk.Style()
style.theme_use('clam')

content = root.selection_get()
output = asyncio.run(translate(content))

text_area = scrolledtext.ScrolledText(root)
text_area.grid(column = 0, pady = 10, padx = 10)
text_area.pack()
text_area.insert(tk.INSERT, output.text)
text_area.configure(state ='disabled')
#w = tk.Label(scrollable_frame, text=output.text, wraplength=500)
#w.pack()

root.mainloop()
