import torch
from torch import cuda, bfloat16
import transformers
import os

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_community.llms import HuggingFacePipeline

def create_localllm(model_id):
    # model_id = 'meta-llama/Meta-Llama-3.1-8B'

    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    # print("device for stopid:",device)
    # set quantization configuration to load large model with less GPU memory
    # # this requires the `bitsandbytes` library
    # bnb_config = transformers.BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_quant_type='nf4',
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_compute_dtype=bfloat16
    # )

    # begin initializing HF items, you need an access token
    # hf_auth = "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"
    # model_config = transformers.AutoConfig.from_pretrained(
    #     model_id,
    #     use_auth_token=hf_auth #
    # )

    # model = transformers.AutoModelForCausalLM.from_pretrained(
    #     model_id,
    #     trust_remote_code=True,
    #     config=model_config,
    #     # quantization_config=bnb_config,
    #     device_map='auto',
    #     use_auth_token=hf_auth
    # )
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    if "mistral" in model_id:
        model = AutoModelForCausalLM.from_pretrained(model_id, attn_implementation="flash_attention_2",torch_dtype=torch.float16, device_map="auto")
    else:
        model = AutoModelForCausalLM.from_pretrained(model_id)

    from transformers import StoppingCriteria, StoppingCriteriaList

    stop_list =['\nHuman','\n```\n']

    stop_token_ids = [tokenizer(x)['input_ids'] for x in stop_list]
    stop_token_ids = [torch.LongTensor(x).to(device) for x in stop_token_ids]


    # define custom stopping criteria object
    class StopOnTokens(StoppingCriteria):
        def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
            for stop_ids in stop_token_ids:
                
                if torch.eq(input_ids[0][-len(stop_ids):], stop_ids).all():
                    return True
            return False

    stopping_criteria = StoppingCriteriaList([StopOnTokens()])

    if 'mistral' in model_id:
        #loading mistral with accelerate, and it doesn't support specify device
        generate_text = transformers.pipeline(
            model=model, 
            tokenizer=tokenizer,
            return_full_text=False,  # langchain expects the full text
            task='text-generation',
            # we pass model parameters here too
            stopping_criteria=stopping_criteria,  # without this model rambles during chat
            temperature=0.05,  # 'randomness' of outputs, 0.0 is the min and 1.0 the max
            max_new_tokens=4096,  # max number of tokens to generate in the output
            repetition_penalty=1.3  # without this output begins repeating
        )
    else:
        generate_text = transformers.pipeline(
            model=model, 
            tokenizer=tokenizer,
            return_full_text=False,  # langchain expects the full text
            task='text-generation',
            device=device,
            # we pass model parameters here too
            stopping_criteria=stopping_criteria,  # without this model rambles during chat
            temperature=0.05,  # 'randomness' of outputs, 0.0 is the min and 1.0 the max
            max_new_tokens=1024,  # max number of tokens to generate in the output
            repetition_penalty=1.3  # without this output begins repeating
        )
    llm = HuggingFacePipeline(pipeline=generate_text)

    return llm
