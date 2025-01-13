import pickle
import pandas as pd



def cleaned_and_vectorized(code):
    # Рассчитываем меру схожести Жаккара
    code_df = pd.DataFrame({'code': [code]})

    code_df.loc[:, ('code')] = code_df.loc[:, ('code')].astype(str).str.replace(r'@[a-zA-Z0-9/.,:\-\'`_ ]+', ' ', regex=True)
    code_df.loc[:, ('code')] = code_df.loc[:, ('code')].astype(str).str.replace(r'/[a-zA-Z0-9/.,:\-\'`_ ]+', ' ', regex=True)
    code_df.loc[:, ('code')] = code_df.loc[:, ('code')].astype(str).str.replace(r'\*[a-zA-Z0-9/.,:\-\'`_ ]+', ' ', regex=True)
    to_replace = ['\\r', '\\n', '\'', '\"', '', '\r', '\n', '{', '}', '/', '*', ';', ':']
    for substr in to_replace:
        code_df.loc[:, ('code')] = code_df.loc[:, ('code')].astype(str).str.replace(substr, '')

    code_df.loc[:, ('code')] = code_df.loc[:, ('code')].astype(str).str.replace('  ', ' ')
    code_df.loc[:, ('code')] = code_df.loc[:, ('code')].astype(str).str.replace(',', ' ')

    with open('../service/tfidf.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    code_vectorized = vectorizer.transform(code_df)

    return code_vectorized


class ScamPredictor:
    def __init__(self):
            # Загрузка модели

        with open('best_model.pkl', 'rb') as f:
            self.model = pickle.load(f)

    def predict_proba(self, code):
        cleaned_and_vectorized_code = cleaned_and_vectorized(code)
        predicted_proba = self.model.predict_proba(cleaned_and_vectorized_code)[0, :]

        return predicted_proba

    def predict(self, code):
        cleaned_and_vectorized_code = cleaned_and_vectorized(code)
        predicted_label = self.model.predict(cleaned_and_vectorized_code)[0]

        return predicted_label
