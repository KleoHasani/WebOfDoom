import click
import requests
from queue import Queue
from threading import Thread
from urllib.parse import urljoin
from multiprocessing import cpu_count

# Worker class.
class Worker:
    def __init__(self, base_url, wordlist_path) -> None:
        self.CPU_THREADS = cpu_count() + 4
        self.base_url: str = base_url
        self.wordlist_path: str = wordlist_path
        self.q: Queue = Queue()
        pass
    

    # Read file and create Queue from endpoints.
    def _build_queue(self) -> None:
        with open(self.wordlist_path, 'r') as file:
            while True:
                line = file.readline()
                
                if not line:
                    break

                self.q.put(line)
        pass

    # Make web request. Print if OK.
    def _make_request(self, endpoint) -> None:
        url = urljoin(self.base_url, endpoint)

        r = requests.get(url)

        if r.ok:
            click.echo(f'{click.style("GET", fg="yellow")} {click.style(200, fg="green")} {url}')
        
        pass

    # Multithread worker.
    def _worker(self) -> None:
        while True:
            endpoint = self.q.get()
            self._make_request(endpoint)
            self.q.task_done()


    # Creat threads and run.
    def run(self) -> None:
        self._build_queue()

        for i in range(self.CPU_THREADS):
            t = Thread(target=self._worker)
            t.setDaemon(True)
            t.start()
        
        self.q.join()
        pass


