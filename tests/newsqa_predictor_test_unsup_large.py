from data_loaders.language_model_loader import LanguageModelLoader 
from models.language_model import LanguageModel
from models.language_trainer import LanguageTrainer
from models.language_wrapper import LanguageWrapper 
from helpers import constants 
import torch 
from helpers import torch_utils, utils
from torch.autograd import variable

dataset_path = 'datasets/newsqa_unsupervised_large_verb_filtered'
load_path = 'logs/squad_saved_data/model_8.pyt7' # CHANGE THIS TO WHATEVER YOU WANT

language_model_loader = LanguageModelLoader(dataset_path, tokenizer_type=constants.TOKENIZER_TAB)
language_model = torch_utils.load_model(load_path).cuda()
language_model.config['save_directory'] = 'logs/newsqa_unsupervised_saved_data'

language_wrapper = LanguageWrapper(language_model, language_model_loader.get_vocab())
language_trainer = LanguageTrainer(language_model.config, language_wrapper, language_model_loader)

##test_predictions = language_trainer.predict(dataset_type=constants.DATASET_TEST,
#            epoch_num=10, max_length=20, beam_size=5)
#dev_predictions = language_trainer.predict(dataset_type=constants.DATASET_VALIDATION,
#            epoch_num=10, max_length=10, beam_size=5)
train_predictions = language_trainer.predict(dataset_type=constants.DATASET_TRAIN,
            epoch_num=10, max_length=10)

utils.save_lines(train_predictions, 'logs/newsqa_saved_data/train_predictions_epoch_6.txt')
#utils.save_lines(dev_predictions, 'logs/newsqa_saved_data/validation_predictions_epoch_6.txt')
#utils.save_lines(test_predictions, 'logs/newsqa_saved_data/test_predictions_epoch_6.txt')




