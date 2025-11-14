# By default, for the majority of Dask APIs, when you call compute on a Dask object,
# Dask uses the thread pool on your computer (a.k.a threaded scheduler) to run computations in parallel.
# This is true for Dask Array, Dask DataFrame, and Dask Delayed. 
# The exception being Dask Bag which uses the multiprocessing scheduler by default.

# setup a cluster that uses only your own computer
from dask.distributed import Client

client = Client()
print(client)

# Once you create a client, any computation will run on the cluster that it points to.

# disgnostics
client.dashboard_link
