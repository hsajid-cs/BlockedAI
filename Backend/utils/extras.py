from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "mrm8488/bert-tiny-finetuned-url-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()
label_map = {0: "Benign", 1: "Defacement", 2: "Phishing", 3: "Malware"}

def prediction(url):
    try:
        inputs = tokenizer(url, return_tensors="pt", truncation=True, padding=True, max_length=128)
        with torch.no_grad():
            outputs = model(**inputs)
            predict = torch.argmax(outputs.logits).item()
        if predict == 3:
            return True
        return False
    
    except Exception as e:
        return str(e)
