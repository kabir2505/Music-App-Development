broker_url="redis://localhost:6379/1" #can be rabbitmq/redis #bydefault redis runs on 6379 
result_backend="redis://localhost:6379/2" #can be database(sql alchemy)/ redis/cache
broker_connection_retry_on_startup=True
timezone="Asia/kolkata"
