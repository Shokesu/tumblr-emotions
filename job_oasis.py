# Import necessary packages
from image_text_model.im_text_rnn_model import oasis_evaluation

checkpoint_dir = 'image_text_model/deep_sentiment_model'
scores = oasis_evaluation(checkpoint_dir)

# Save output and parameters to text file in the localhost node, which is where the computation is performed.
#with open('/data/localhost/not-backed-up/ahu/jobname_' + str(slurm_id) + '_' + str(slurm_parameter) + '.txt', 'w') as text_file:
	#text_file.write('Parameters: {0} Result: {1}\n'.format(parameter, output))