import neptune

# The init() function called this way assumes that 
# NEPTUNE_API_TOKEN environment variable is defined.

neptune.init('charag/Littlefoot')
neptune.create_experiment(name='hello_world')

# log some metrics

for i in range(100):
    neptune.log_metric('loss', 0.95**i)

neptune.log_metric('AUC', 0.96)