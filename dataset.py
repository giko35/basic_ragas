import pandas as pd
import json
 
def extract_rag_data(csv_path: str):
   
    df = pd.read_csv(csv_path)
 
    rag_list = []
    for _, row in df.iterrows():
        qid = row["id"]
        question = row.get("question", "")
       
       
        try:
            gold_blocks = json.loads(row.get("gold_answer", "[]"))
        except json.JSONDecodeError as e:
            raise ValueError(f"Could not parse JSON in gold_answer for id={qid}: {e}")
        try:
            ai_blocks = json.loads(row.get("ai_answer", "[]"))
        except json.JSONDecodeError as e:
            raise ValueError(f"Could not parse JSON in ai_answer for id={qid}: {e}")
 
       
        gold_content = ""
        for block in gold_blocks:
            if block.get("category") == "Final Answer":
                gold_content = block.get("content", "")
                break
 
        ai_content = ""
        for block in ai_blocks:
            if block.get("category") == "Final Answer":
                ai_content = block.get("content", "")
                break
 
       
        chunks = []
        for block in ai_blocks:
            if block.get("category") == "Quotes":
                chunks = [child.get("content", "") for child in block.get("children", [])]
                break
 
       
        rag_list.append({
            "id": qid,
            "user_input": question,
            "reference": gold_content,
            "response": ai_content,
            "retrieved_contexts": chunks
        })
 
    return rag_list

def save_to_json(rag_list, json_path):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rag_list, f, ensure_ascii=False, indent=2)
 
    print(f"✅ Saved {len(rag_list)} items to {json_path}")

 
if __name__ == "__main__":
    rag_list = extract_rag_data(csv_path="ragas/questions_file.csv")
    save_to_json(rag_list, json_path="ragas/ragas_input.json")