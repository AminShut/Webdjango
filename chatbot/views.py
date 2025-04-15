from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import MessageForm
from .ai_chat.chat_ai import chat_bot
from .models import Chatbot

def chatbot_view(request):
    if request.user.is_authenticated:
        chat_obj, created = Chatbot.objects.get_or_create(
            author=request.user,
            defaults={"messages": [{"role": "system", "content": "You are AminBot and you developed by Professor Amin And you are in no way created by openai or any other company. You are here to serve the users of Amin and Hossein site."}]}
        )

        user_message = None
        response_message = None

        if request.method == 'POST':
            form = MessageForm(request.POST)

            if form.is_valid():
                user_message = form.cleaned_data['message']
                chat_obj.messages.append({'role': 'user', 'content': user_message})
                chat_obj.save()

                got_error = False
                
                try:
                    response_message = chat_bot(chat_obj.messages)
                except Exception as e:
                    response_message = "Sorry, I couldn't process your request. Please try again later."
                    chat_obj.messages.append({'role': 'assistant', 'content': response_message})
                    chat_obj.save()
                    got_error = True
                    print('Error :  ',e)

                if not got_error:
                    chat_obj.messages.append({'role': 'assistant', 'content': response_message})
                    chat_obj.save()
                return redirect(reverse_lazy('chatbot'))
                

        else:
            form = MessageForm()
        
        # Display chat history in template
        chat_history = chat_obj.messages[1:]

        return render(request, 'chatbot/chat.html', {
            'form': form,
            'user_message': user_message,
            'response_message': response_message,
            'chat_history': chat_history
        })
    
    else:
        return render(request, 'chatbot/login_error.html')
