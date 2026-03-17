import time
import torch
import psutil
import os
from bitnet import BitNetLlamaForCausalLM
from transformers import AutoTokenizer
from rich.console import Console
from rich.table import Table

console = Console()

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 3)  # Conversion en GB

def run_benchmark(model_id="microsoft/bitnet-b1.58-3B"):
    stats = {}
    
    # 1. Mesure mémoire avant chargement
    mem_before = get_memory_usage()
    
    console.print(f"[bold blue]Chargement de {model_id}...[/bold blue]")
    start_load = time.time()
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = BitNetLlamaForCausalLM.from_pretrained(model_id)
    
    end_load = time.time()
    mem_after = get_memory_usage()
    
    # 2. Mesure de la vitesse de génération
    prompt = "The future of AI is"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    start_gen = time.time()
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=50)
    end_gen = time.time()
    
    tokens_generated = len(outputs[0])
    time_taken = end_gen - start_gen
    
    # Compilation des stats
    stats['mem_used'] = mem_after - mem_before
    stats['load_time'] = end_load - start_load
    stats['tokens_per_sec'] = tokens_generated / time_taken

    # Affichage du tableau
    table = Table(title="📊 BitNet Benchmark Results")
    table.add_column("Métrique", style="cyan")
    table.add_column("Valeur", style="magenta")

    table.add_row("Mémoire RAM utilisée (Poids)", f"{stats['mem_used']:.2f} GB")
    table.add_row("Temps de chargement", f"{stats['load_time']:.2f} s")
    table.add_row("Vitesse d'inférence (CPU)", f"{stats['tokens_per_sec']:.2f} t/s")

    console.print(table)
    return stats

if __name__ == "__main__":
    run_benchmark()