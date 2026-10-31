def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def split_into_chunks(text):
    return text.split("\n\n")
def find_relevant(question, chunks, top_n=3):
    question_lower = question.lower()
    question_words = question_lower.split()
    results = []
    for chunk in chunks:
        chunk_lower = chunk.lower()
        chunk_words = chunk_lower.split()
        
        count = 0
        for word in question_words:
            if word in chunk_words:
                count += 1
                
        results.append((chunk, count))
        
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_n]
def main():
    text = load_text("knowledge.txt")
    chunks = split_into_chunks(text)
    question = input("Введите вопрос:" )
    top3 = find_relevant(question, chunks)
    if top3[0][1] == 0:
        print ("Ничего не найдено")
    else:
        for chunk, score in top3:
            print(chunk)
            print()
main()