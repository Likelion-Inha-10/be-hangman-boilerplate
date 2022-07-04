from django.shortcuts import get_object_or_404, render
from .models import Hangman
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class TestAPI(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"meessage": "Hello, world!"})
    def post(self, request, *args, **kwargs):
        return Response(request.data['name'])

class New(APIView):
    def post(self, request, *args, **kwargs,):
        hm = Hangman()
    
        # make default data
        hm.tried_chars = ''
        hm.point = 0
        hm.try_count = 0
        
        # input data
        while True:
            hm.max_try = request.data["max_try"]
            hm.word = str(request.data["word"]).lower()
            hm.hidden = '_' * len(hm.word)

            if hm.max_try <= 30 and len(hm.word) <= 50: 
                hm.save()
                break
            elif hm.max_try > 30:
                return Response({"error": "Please type max_try under 30"})
            elif len(hm.word) > 50:
                return Response({"error": "Please type length of word under 50"})

        return Response({"id":hm.id, 'word':hm.word, "max_try":hm.max_try})

class Game(APIView):
    def get(self, request, hmid):
        hm = get_object_or_404(Hangman, pk=hmid)

        return Response({"word": hm.hidden, "tried_chars":hm.tried_chars, "max_try":hm.max_try})

    def post(self, request, hmid):
        hm = get_object_or_404(Hangman, pk=hmid)

        # input data
        hm.ans = str(request.data["char"]).lower()
        # hm.ans = hm.ans.lower()
        
        if len(hm.ans) > 1:
            raise ValidationError

        # If ans was already typed
        if hm.hidden.find(hm.ans) != -1 or hm.tried_chars.find(hm.ans) != -1:   
            return Response({"error" : "Please type another alphabet"})

        # If ans exists in word
        elif hm.word.find(hm.ans) != -1:
            for i in range(0, len(hm.word), 1):
                if hm.word[i] == hm.ans:
                    l = list(hm.hidden)
                    l[i] = hm.ans
                    hm.hidden = ''.join(l)
                    hm.save()
    
        # If ans doesn't exists in word
        else:
            hm.tried_chars += hm.ans + ', '
            hm.try_count += 1
            hm.save()

        # If user type all alphabets
        if hm.hidden == hm.word:
            return Response({"word" : hm.hidden, "message" : "Congratulation!"})
    
        # If user type word
        if hm.ans == hm.word:
            return Response({"word" : hm.word, "message" : "Congratulation!"})

        # If user tried the maximum amount
        if hm.try_count == hm.max_try:
            return Response({"error": "you have tried the maximum amount"})

        return Response({"word":hm.hidden,"tried_chars":hm.tried_chars,"try_count":hm.try_count,"max_try":hm.max_try})