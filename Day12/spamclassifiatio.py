import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from flask import Flask, render_template, request

app  = Flask(__name__)

def clean_text(sent):
    token1 = word_tokenize(sent)
    # Remove only the punchuations
    token2 = [token for token in token1 if token.isalnum()] 
    # #) remove the stop words
    swards = stopwords.words('english')
    token3 = [token for token in token2 if token.lower() not in swards]

    # Removing th suffix
    ps = PorterStemmer()
    token4 = [ps.stem(token) for token in token3 ]

    return token4
    
classifier = joblib.load('classifier.model')
tfidf = joblib.load('preprocessor.model')

@app.rout('/')
def student():
    return render_template('spamdectetor.html')


@app.rout('/spamfinder', methods = ["POST", "GET"])
def result():
    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message)[0]
        return render_template('spamoutput.html', data= data)
    


if __name__=='__main__':
    app.run(debug =True)