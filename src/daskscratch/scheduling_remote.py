# By default, for the majority of Dask APIs, when you call compute on a Dask object,
# Dask uses the thread pool on your computer (a.k.a threaded scheduler) to run computations in parallel.
# This is true for Dask Array, Dask DataFrame, and Dask Delayed. 
# The exception being Dask Bag which uses the multiprocessing scheduler by default.

# This is how you connect to a cluster that is already running
from dask.distributed import Client


client = Client("<url-of-scheduler>")

print(client)


