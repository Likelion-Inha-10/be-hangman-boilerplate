from tkinter import N
from django.shortcuts import get_object_or_404, render
from hangman.models import Hangman_Game
from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPI(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"meessage": "Hello, world!"})
    def post(self, request, *args, **kwargs):
        return Response(request.data['name'])

class New(APIView):
    def post(self, request, *args, **kwargs,):
        hangman = Hangman_Game()
    
        # make default data
        hangman.try_chars = ''
        hangman.point = 0
        hangman.try_count = 0
        
        # input data
        hangman.max_try = request.data["max_try"]
        hangman.word = str(request.data["word"]).lower()
        hangman.hidden_chars = '_' * len(hangman.word)

        if hangman.max_try <= 30 and len(hangman.word) <= 50: 
                hangman.save()
                
        elif hangman.max_try > 30:
            return Response({"error": "Please type max_try under 30"})
        
        elif len(hangman.word) > 50:
            return Response({"error": "Please type length of word under 50"})

        return Response({"id":hangman.id,
                         'word':hangman.word, 
                         "max_try":hangman.max_try})

class Game(APIView):
    def get(self, request, hangmanid):
        hangman=get_object_or_404(Hangman_Game,pk=hangmanid)

        return Response({"word":hangman.hidden_chars, "tried_chars":hangman.try_chars, "max_try":hangman.max_try})

    def post(self,request,hangmanid):
        hangman=get_object_or_404(Hangman_Game,pk=hangmanid)
        
        hangman.answer=str(request.data["char"]).lower()
        
        if len(hangman.answer) > 1 or 'a' > hangman.answer or hangman.answer > 'z':
            return Response({"Error":"잘못된 타입"})
        
        # 중복방지
        if hangman.hidden_chars.find(hangman.answer) != -1 or hangman.try_chars.find(hangman.answer) != -1:   
            return Response({"Error":"시도한 알파벳과 중복"})
        
        elif hangman.word.find(hangman.answer) !=-1:
            for i in range(0, len(hangman.word),1):
                if hangman.word[i]==hangman.answer:
                    List=list(hangman.hidden_chars)
                    List[i]=hangman.answer
                    hangman.hidden_chars=''.join(List)
                    hangman.try_count += 1
                    hangman.save()

            
        else:
            hangman.try_chars +=hangman.answer+', '
            hangman.try_count += 1
            hangman.save()
            
        
        if hangman.hidden_chars==hangman.word:
            return Response({"word":hangman.hidden_chars, "message":"Success!"})
        
        if hangman.max_try<hangman.try_count:
            return Response({"Error":"Game Over"})
        
        return Response({"word":hangman.hidden_chars, "try_chars":hangman.try_chars, "try_count":hangman.try_count, "max_try":hangman.max_try})


        
                