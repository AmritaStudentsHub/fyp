from django.shortcuts import render, redirect
from .forms import QuestionForm
from .BERTSQuADmaster.bert import QA
from .BERTSQuADmaster.translate import englishToHindiTranslate

# Create your views here.
def basic(request):
    if request.method =='POST':
        question = request.POST['question']
        para = request.POST['paragraph']
        print(question)
        model = QA("/home/prahlad/Desktop/final FYP/bert_translate/BERTSQuADmaster/model/")
        english_text = model.predict(para,question)["answer"]
        print(english_text)
        # translated_text = englishToHindiTranslate(english_text)
        # print(translated_text)
        # form = QuestionForm(initial={'input_4':para})
        return render(request,'Feedback_Form.html',{'para':para,'question':question,'ans':english_text})
    else:
        form = QuestionForm()
    return render(request,'Feedback_Form.html',{'form':form})

