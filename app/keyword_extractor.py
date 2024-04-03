def keyword_extractor(sentence, tokenizer, model):
    inputs = tokenizer(sentence, return_tensors="pt", max_length=512, truncation=True)

    outputs = model.generate(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'], max_new_tokens=40)

    decoded_outputs = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded_outputs
