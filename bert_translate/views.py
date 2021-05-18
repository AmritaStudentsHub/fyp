from django.shortcuts import render, redirect
from .forms import QuestionForm
from .BERTSQuADmaster.bert import QA
from .BERTSQuADmaster.translate import englishToHindiTranslate
from englisttohindi.englisttohindi import EngtoHindi
# Create your views here.
def basic(request):
    if request.method =='POST':
        question1 = request.POST['question1']
        question2 = request.POST['question2']
        para = request.POST['paragraph']
        print(question1)
        model = QA("/home/prahlad/Desktop/final FYP/bert_translate/BERTSQuADmaster/model/")
        english_text1 = model.predict(para,question1)["answer"]
        english_text2 = model.predict(para,question2)["answer"]
        print(english_text1)
        # translated_text = englishToHindiTranslate(english_text)
        # print(translated_text)
        # form = QuestionForm(initial={'input_4':para})
        ans1_t = EngtoHindi(english_text1)
        ans2_t = EngtoHindi(english_text2)
        # ans1_t = '१८ मई १८८२'
        # ans2_t ='१९२०-२१ और १९५९-६०'
        return render(request,'Feedback_Form.html',{'para':para,'question1':question1,'ans1':english_text1,'ans1t':ans1_t.convert,'question2':question2,'ans2':english_text2,'ans2t':ans2_t.convert})
    else:
        form = QuestionForm()
    return render(request,'Feedback_Form.html',{'form':form})

