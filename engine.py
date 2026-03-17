from bitnet import BitLinear, BitNetLlamaForCausalLM
from transformers import AutoTokenizer

def initialize_bitnet_engine(model_id):
    # Chargement du tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    # Chargement du modèle avec l'architecture BitNet spécifique
    # C'est ici que les poids sont gérés en {-1, 0, 1}
    model = BitNetLlamaForCausalLM.from_pretrained(model_id)
    
    return model, tokenizer